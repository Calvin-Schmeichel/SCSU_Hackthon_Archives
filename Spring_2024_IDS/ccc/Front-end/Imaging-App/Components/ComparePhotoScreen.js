import React, { useEffect, useState } from 'react';
import { View, Image, StyleSheet, Text, PanResponder } from 'react-native';
import { useImageContext } from './ImageContext';

const ComparePhotosScreen = () => {
    const { beforePhoto, afterPhoto, gyroscopeDataBefore, gyroscopeDataAfter } = useImageContext();
    const [similarityPercentage, setSimilarityPercentage] = useState(null);
    const [swipePosition, setSwipePosition] = useState(0);

    useEffect(() => {
        // Function to calculate Euclidean distance between two points in 3D space
        const euclideanDistance = (x1, y1, z1, x2, y2, z2) => {
            return Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2) + Math.pow(z2 - z1, 2));
        };

        // Function to compare gyroscope values and return a similarity percentage
        const compareGyroscopeData = (before, after) => {
            const distance = euclideanDistance(before.x, before.y, before.z, after.x, after.y, after.z);

            // Define a threshold value based on your requirements
            const threshold = 0.25; // Adjust this value based on your use case

            // Calculate the similarity percentage
            const similarityPercentage = Math.max(0, 100 - (distance / threshold) * 100);

            return similarityPercentage;
        };

        if (gyroscopeDataBefore && gyroscopeDataAfter) {
            const percentage = compareGyroscopeData(gyroscopeDataBefore, gyroscopeDataAfter);
            setSimilarityPercentage(percentage);
        }
    }, [gyroscopeDataBefore, gyroscopeDataAfter]);

    // PanResponder for handling touch gestures
    const panResponder = PanResponder.create({
        onStartShouldSetPanResponder: () => true,
        onPanResponderMove: (evt, gestureState) => {
            // Calculate the swipe position based on the gestureState
            const newPosition = Math.max(0, Math.min(1, gestureState.dx / 200));
            setSwipePosition(newPosition);
        },
    });

    return (
        <View style={styles.container}>
            <View style={styles.photoContainer}>
                <Image source={{ uri: beforePhoto }} style={styles.photo} />
                {afterPhoto && (
                    <Image
                        source={{ uri: afterPhoto }}
                        style={[styles.photo, { marginLeft: swipePosition * 200 }]}
                    />
                )}
            </View>
            {similarityPercentage !== null && (
                <Text>{`Gyroscope Similarity: ${similarityPercentage.toFixed(2)}%`}</Text>
            )}
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    photoContainer: {
        flexDirection: 'row',
        overflow: 'hidden',
    },
    photo: {
        flex: 1,
        height: 300,
        margin: 5,
        resizeMode: 'cover',
    },
});

export default ComparePhotosScreen;
