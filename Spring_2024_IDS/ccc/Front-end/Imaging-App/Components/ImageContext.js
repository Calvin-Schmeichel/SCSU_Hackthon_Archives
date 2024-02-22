// ImageContext.js
import React, { createContext, useContext, useState } from 'react';

const ImageContext = createContext();

export const ImageProvider = ({ children }) => {
    const [beforePhoto, setBeforePhoto] = useState(null);
    const [afterPhoto, setAfterPhoto] = useState(null);
    const [gyroscopeDataBefore, setGyroscopeDataBefore] = useState(null);
    const [gyroscopeDataAfter, setGyroscopeDataAfter] = useState(null);

    const values = {
        beforePhoto,
        setBeforePhoto,
        afterPhoto,
        setAfterPhoto,
        gyroscopeDataBefore,
        setGyroscopeDataBefore,
        gyroscopeDataAfter,
        setGyroscopeDataAfter,
    };

    return <ImageContext.Provider value={values}>{children}</ImageContext.Provider>;
};

export const useImageContext = () => {
    const context = useContext(ImageContext);
    if (!context) {
        throw new Error('useImageContext must be used within an ImageProvider');
    }
    return context;
};
