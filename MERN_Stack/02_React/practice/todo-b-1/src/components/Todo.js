import React from 'react';

const Todo = ({description, isComplete, key, toggleIsComplete}) => {

    return(
        <div>
            <p>
                {description}
                <input type="checkbox" value={isComplete} checked={isComplete} onClick={toggleIsComplete(key)}></input>
                <button>Delete</button>
            </p>
        </div>

    )
}
export default Todo;