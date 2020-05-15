import React, { useState } from 'react';

const BoxGenerator = props => {
    const { color, height, width } = props

    
    return(
        <div style={{ 
            backgroundColor: color,
            width: width,
            height: height,
            marginLeft: 10,
        }}>
            test boxgen
        </div>
    );
}
export default BoxGenerator;