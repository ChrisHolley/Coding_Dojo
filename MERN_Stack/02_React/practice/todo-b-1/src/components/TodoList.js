import React from 'react';
import Todo from './Todo';

const TodoList = ({todos, toggleisComplete}) => {

    return(
        <div>
            {todos.map((val, i) =>
                <Todo key={i} isComplete={val.isComplete} description={val.description} toggleisComplete={toggleIsComplete}/>
            )}
        </div>
    )
}
export default TodoList;