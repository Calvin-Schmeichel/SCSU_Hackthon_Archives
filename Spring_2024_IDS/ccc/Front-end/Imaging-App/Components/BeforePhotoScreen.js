// BeforePhotoScreen.js
import React, { useState, useEffect } from 'react';
import { StyleSheet, View, Button, Text, Image } from 'react-native';
import { Camera } from 'expo-camera';
import { useNavigation } from '@react-navigation/native';
import { useImageContext } from './ImageContext';
import GyroManager from './GyroscopeHandler';

const BeforePhotoScreen = () => {
    const [cameraPermission, setCameraPermission] = useState(null);
    const [camera, setCamera] = useState(null);
    const { setBeforePhoto, setGyroscopeDataBefore } = useImageContext(); // Include setGyroscopeDataBefore from the context
    const navigation = useNavigation();

    const [{ x, y, z }, setGyroData] = useState({
        x: 0,
        y: 0,
        z: 0,
    });

    const requestPermissions = async () => {
        const { status: gyroStatus } = await Gyroscope.requestPermissionsAsync();
        const { status: cameraStatus } = await Camera.requestCameraPermissionsAsync();
        setCameraPermission(cameraStatus === 'granted');

        if (cameraStatus !== 'granted' || gyroStatus !== 'granted') {
            alert('Permission for camera access and gyroscope is needed.');
        }
    };

    const takeBeforePhoto = async () => {
        if (camera) {
            const { uri } = await camera.takePictureAsync(null);
            const gyroscopeDataBefore = { x, y, z };

            // Save gyroscope data and before photo in the context
            setGyroscopeDataBefore(gyroscopeDataBefore);
            setBeforePhoto(uri);

            navigation.navigate('CurrentPhoto');
        }
    };

    useEffect(() => {
        requestPermissions();
    }, []);

    return (
        <View style={styles.container}>
            <View style={styles.cameraContainer}>
                <Camera ref={(ref) => setCamera(ref)} style={styles.fixedRatio} type={Camera.Constants.Type.back} ratio={'1:1'} />
            </View>
            <GyroManager setGyroData={setGyroData} />

            <Text style={styles.text}>Gyroscope Information:</Text>
            <Text style={styles.text}>x: {x}</Text>
            <Text style={styles.text}>y: {y}</Text>
            <Text style={styles.text}>z: {z}</Text>

            <Button title="Take Before Photo" onPress={takeBeforePhoto} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    cameraContainer: {
        flex: 1,
        flexDirection: 'row',
    },
    text: {
        textAlign: 'center',
        textAlignVertical: 'bottom',
    },
    fixedRatio: {
        flex: 1,
        aspectRatio: 1,
    },
});

export default BeforePhotoScreen;
