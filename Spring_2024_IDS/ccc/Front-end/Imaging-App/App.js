// App.js
import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import BeforePhotoScreen from './Components/BeforePhotoScreen';
import CurrentPhotoScreen from './Components/CurrentPhotoScreen';
import AfterPhotoScreen from './Components/AfterPhotoScreen';
import ComparePhotosScreen from './Components/ComparePhotoScreen';
import { ImageProvider } from './Components/ImageContext';

const Stack = createStackNavigator();

const App = () => {
    return (
        <NavigationContainer>
            <ImageProvider>
                <Stack.Navigator initialRouteName="BeforePhoto">
                    <Stack.Screen name="BeforePhoto" component={BeforePhotoScreen} />
                    <Stack.Screen name="CurrentPhoto" component={CurrentPhotoScreen} />
                    <Stack.Screen name="AfterPhoto" component={AfterPhotoScreen} />
                    <Stack.Screen name="ComparePhotos" component={ComparePhotosScreen} />
                </Stack.Navigator>
            </ImageProvider>
        </NavigationContainer>
    );
};

export default App;
