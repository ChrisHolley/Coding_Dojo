import React from 'react';

const Input = (props) => {
    const { list, setList } = props; // destructures props into list and setList
    let task = { //create the list called task with a blank name and not complete boolean set to false
        name: "",
        isComplete: false
    };

    const onChange = (e) => {
        task.name = e.target.value;  // updates name as function is called
    };

    const onClick = (e) => {
        setList([...list, task]) //spread list and add new item 'task' to the array
        // e.target.value = ""; //reset task to blank
        // task = ""; //is this needed?
    };

    return(
        <div className="container w-50 mt-3">
            <input onChange={onChange} className="form-control" type="text" name="task" />
            <button onClick={onClick} className="btn btn-primary btn-block mt-1">
                add task
            </button>

        </div>
    );
}
export default Input;