// CurrentPhotoScreen.js
import React from 'react';
import { View, Button, Image, StyleSheet } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import { useImageContext } from './ImageContext';

const CurrentPhotoScreen = () => {
    const { beforePhoto } = useImageContext();
    const navigation = useNavigation();

    const navigateToAfterPhoto = () => {
        navigation.navigate('AfterPhoto');
    };

    return (
        <View style={styles.container}>
            <Image source={{ uri: beforePhoto }} style={styles.image} />
            <Button title="Take After Photo" onPress={navigateToAfterPhoto} />
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    image: {
        width: 200,
        height: 200,
    },
});

export default CurrentPhotoScreen;