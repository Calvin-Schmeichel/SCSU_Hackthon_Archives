import tkinter as tk
from PIL import ImageTk, Image
import time
import random

from duck_curve import main_output

def test():

    mylist = ["apple", "banana", "cherry"]
    num = (random.randint(0, 2))
    print(num)
    word = mylist[num]

    return word

counter = 0
# Define the image file paths
image_files = ['discharge.png', 'charging.png', 'full.png']
# Define the delay between image changes in milliseconds
delay = 1000

# Create the tkinter window
window = tk.Tk()

# Load the images using Pillow
images = [ImageTk.PhotoImage(Image.open(filename)) for filename in image_files]

# Create the label for the image
image_label = tk.Label(window)

# Define the function to update the image
def update_image(index):
    # Update the image label with the current image
    image_label.configure(image=images[index])
    # Schedule the next image update after the specified delay
    #window.after(delay, update_image, (index + 1) % len(images))

# Start the image loop
    #print(main_output)


frame = tk.Frame(window)
frame.pack(side=tk.LEFT)
text = tk.Text(frame, width=40, height=10)
text.configure(font=("Arial", 30))
text.pack()
text.insert(tk.END, "")

n=0
while n <= 24:

    if n == 24:
        n = 0

    #update_image(random.randint(0, 2))
    n=n+1
    print(n)
    input("")
    if main_output[n][1] == 'can discharge':
        update_image(2)
        text.delete('1.0', tk.END)
        text.insert(tk.END, f"can discharge at {n}:00 (24 Hour Time)")
    elif main_output[n][1] == 'can charge':
        update_image(0)
        text.delete('1.0', tk.END)
        text.insert(tk.END, f"can charge at {n}:00 (24 Hour Time)")
    elif main_output[n][1] == 'idling':
        update_image(1)
        text.delete('1.0', tk.END)
        text.insert(tk.END, f"is idling at {n}:00 (24 Hour Time)")
    else:
        print("Something went wrong!")

    #image_label.pack()
    #time.sleep(1)
    image_label.pack()



# Pack the image label into the window
#image_label.pack()

# Start the tkinter event loop

#window.mainloop()

