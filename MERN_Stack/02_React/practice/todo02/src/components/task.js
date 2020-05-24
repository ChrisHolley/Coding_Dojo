import React from 'react';

const Task = props => {
    const { task, setList, index, list } = props;

    const onClick = () => {
        setList(() => {
            list.filter(task => task !== index)
        });
    }

    return(
        <div>
            <h4>{task.name}</h4>
            <label htmlFor="checkbox">Complete?</label>
            <input type="checkbox" name="" />
            <button onClick={onClick}>X</button>
        </div>
    );
}


export default Task;