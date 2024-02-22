// GyroscopeHandler.js
// Please be mindful, the .js file is called GyroscopeHandler.js, the component that's called is referred to as GyroManager
import React, { useState, useEffect } from 'react';
import { Gyroscope } from 'expo-sensors';

const GyroManager = ({ setGyroData }) => { //Manager that contains everything involved in running GyroManager
  const [subscription, setSubscription] = useState(null);

  Gyroscope.setUpdateInterval(1000); //Change this line to adjust how quickly the gyroscope will visibly update. 

  const makeSubscribe = () => {
    setSubscription(
      Gyroscope.addListener(gyroscopeData => { //This allows us to see  what the gyroscope is doing. 
        setGyroData(gyroscopeData);
      })
    );
  };

  useEffect(() => {
    makeSubscribe(); // Call makeSubscribe to start listening to the gyroscope

    return () => {
      subscription && subscription.remove(); // Remove the gyroscope listener when component unmounts
    };
  }, []);

  return null; // GyroManager doesn't render anything
};

export default GyroManager;
