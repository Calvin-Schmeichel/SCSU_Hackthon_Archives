from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from skimage.metrics import structural_similarity
import cv2
import numpy as np
import firebase_admin
from firebase_admin import credentials, storage
from pydantic import BaseModel
import base64
import asyncio

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./ccc-hackathon-77a0d-firebase-adminsdk-7lcy1-5d870cc01a.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://ccc-hackathon-77a0d-default-rtdb.firebaseio.com/', 'storageBucket': 'ccc-hackathon-77a0d.appspot.com'})

app = FastAPI()

# Allow all origins for demonstration purposes. You may want to restrict this in production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ImageKeys(BaseModel):
    before_key: str
    after_key: str

def download_image_from_firebase(image_path):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(image_path)
        content = blob.download_as_bytes()
        return np.frombuffer(content, dtype=np.uint8)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error downloading image: {str(e)}")

def upload_image_to_firebase(image_path, content):
    try:
        bucket = storage.bucket()
        blob = bucket.blob(image_path)

        # Upload the content as bytes
        blob.upload_from_string(content, content_type='image/png')

        # Explicitly check if the blob exists to ensure the upload is complete
        if not blob.exists():
            raise Exception("Error: Blob does not exist. Upload may not be complete.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading image: {str(e)}")

async def compute_and_upload_difference(before_img, after_img):
    # Convert images to grayscale
    before_gray = cv2.cvtColor(before_img, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after_img, cv2.COLOR_BGR2GRAY)

    # Compute SSIM between the two images
    (score, diff) = structural_similarity(before_gray, after_gray, full=True)
    print("Image Similarity: {:.4f}%".format(score * 100))

    # The diff image contains the actual image differences between the two images
    # and is represented as a floating point data type in the range [0,1] 
    # so we must convert the array to 8-bit unsigned integers in the range
    # [0,255] before we can use it with OpenCV
    diff = (diff * 255).astype("uint8")

    # Threshold the difference image to obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # Find contours in the difference image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the after_img to highlight the differences
    cv2.drawContours(after_img, contours, -1, (0, 0, 255), 2)

    # Save the highlighted difference image
    diff_highlighted_filename = 'diffhighlighted.jpg'
    cv2.imwrite(diff_highlighted_filename, after_img)

    # Wait for a short period (adjust as needed)
    await asyncio.sleep(1)

    # Upload the highlighted difference image to Firebase Storage
    with open(diff_highlighted_filename, 'rb') as diff_file:
        diff_content = diff_file.read()
        upload_image_to_firebase('diffhighlighted.jpg', diff_content)

    # Optionally, you can remove the local file after uploading
    # os.remove(diff_highlighted_filename)

@app.post("/processImages")
async def process_images(keys: ImageKeys):
    try:
        # Download images from Firebase Storage
        before_content = download_image_from_firebase(keys.before_key)
        after_content = download_image_from_firebase(keys.after_key)

        before_img = cv2.imdecode(before_content, cv2.IMREAD_COLOR)
        after_img = cv2.imdecode(after_content, cv2.IMREAD_COLOR)

        # Run the compute_and_upload_difference function asynchronously
        await compute_and_upload_difference(before_img, after_img)

        return {"message": "Processing completed successfully"}

    except HTTPException as e:
        raise e  # Re-raise HTTPException to maintain the original status code and detail
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
