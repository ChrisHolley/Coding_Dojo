import React, { useState } from 'react';

const Create = ({todos, setTodos}) => {
    
    const [newTodoDesc, setNewTodoDesc] = useState("")

    const handleSubmit = (event) => {
        event.preventDefault();
        setTodos([
            ...todos,
            {
                description: newTodoDesc,
                isComplete: false
            }
        ])
        setNewTodoDesc("");
    }
    
    return(
        <div>
            { newTodoDesc }
            <form onSubmit={handleSubmit}>
                <input type="text" value={newTodoDesc} onChange={event => setNewTodoDesc(event.target.value)}></input>
                <input type="submit" value="create todo"></input>
            </form>
        </div>
    )
}
export default Create;