import React, { useState } from 'react';

const PersonCard = props => {
    const [age, setAge] = useState({
        ageCount: props.age
    });
    const handleClick = () => {
        setAge(age+1);
    }
    return(
        <div>
            <h1>{props.lastName}, {props.firstName}</h1>
            <p>Age: {age.ageCount}</p> 
            <p>hair Color: {props.hairColor}</p>
            <button onClick={ handleClick }>This is the birthday button for {props.firstName} {props.lastName}</button>
        </div>
    );
} 
export default PersonCard;