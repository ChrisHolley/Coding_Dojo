import React, { useState } from 'react';
import './App.css';
import TodoList from './components/TodoList';
import Create from './components/Create';

function App() {
  const [todos, setTodos] = useState([{
    description: "Create Defaults",
    isComplete: false
  },
  {
    description: "Show Defaults",
    isComplete: true
  }
  ])

  const toggleIsComplete = (idx) => {
    const copyTodos = [...todos];

    const selectedTodo = copyTodos[idx];
    selectedTodo.isComplete = !selectedTodo.isComplete;

    setTodos(copyTodos);
  }

  return (
    <div className="App">
      <Create todos={todos} setTodos={setTodos} />
      <TodoList todos={todos} toggleIsComplete={toggleIsComplete}  />
    </div>
  );
}

export default App;
