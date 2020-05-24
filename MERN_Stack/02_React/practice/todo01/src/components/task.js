import React from 'react';

const Task = (props) => {
    const { task, index, list, setList } = props;
    const onClick = () => {
        setList(() => {
            return list.filter(task => list.indexOf(task) !== index)
        });
    }    
    const onChange = () => {
        list[index].isComplete = !list[index].isComplete;
        setList([...list]);
    };
//pull isComplete from array
//change it
//put it back
    
    return(
        <div className="container">
            {
            task.isComplete ?
            <h4 style={{textDecoration: "line-through"}}>{task.name}</h4> :
            <h4>{task.name}</h4>
        }
            <div>
                <label htmlFor="checkbox">Completed?</label>
                <input onChange={onChange} type="checkbox" checked={task.isComplete}/>
                <button onClick={onClick} className="btn btn-sm btn-danger">X</button>
            </div>
        </div>
    );
}
export default Task;