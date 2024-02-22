// AfterPhotoScreen.js
import React, { useState, useEffect } from 'react';
import { View, Button, StyleSheet, Text } from 'react-native';
import { Camera } from 'expo-camera';
import { useNavigation } from '@react-navigation/native';
import { useImageContext } from './ImageContext';
import GyroManager from './GyroscopeHandler';

const AfterPhotoScreen = () => {
    const [cameraPermission, setCameraPermission] = useState(null);
    const [camera, setCamera] = useState(null);
    const { setAfterPhoto, setGyroscopeDataAfter } = useImageContext();
    const navigation = useNavigation();

    const [{ x, y, z }, setGyroData] = useState({
        x: 0,
        y: 0,
        z: 0,
    });

    useEffect(() => {
        requestPermissions();
    }, []);

    const requestPermissions = async () => {
        const { status: gyroStatus } = await Gyroscope.requestPermissionsAsync();
        const { status: cameraStatus } = await Camera.requestCameraPermissionsAsync();
        setCameraPermission(cameraStatus === 'granted');

        if (cameraStatus !== 'granted' || gyroStatus !== 'granted') {
            alert('Permission for camera access and gyroscope is needed.');
        }
    };

    const takeAfterPhoto = async () => {
        if (camera) {
            const { uri } = await camera.takePictureAsync(null);
            const gyroscopeDataAfter = { x, y, z };
            setGyroscopeDataAfter(gyroscopeDataAfter);
            setAfterPhoto(uri);
            navigation.navigate('ComparePhotos');
        }
    };

    return (
        <View style={styles.container}>
            <Camera ref={(ref) => setCamera(ref)} style={styles.fixedRatio} type={Camera.Constants.Type.back} ratio={'1:1'} />
            <GyroManager setGyroData={setGyroData} />

            <Text style={styles.text}>Gyroscope Information:</Text>
            <Text style={styles.text}>x: {x}</Text>
            <Text style={styles.text}>y: {y}</Text>
            <Text style={styles.text}>z: {z}</Text>

            <Button title="Take After Photo" onPress={takeAfterPhoto} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
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

export default AfterPhotoScreen;
