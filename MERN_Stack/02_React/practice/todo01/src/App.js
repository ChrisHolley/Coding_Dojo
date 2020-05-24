import React, { useState } from 'react';
import './App.css';
import Input from './components/input'
import Task from './components/task';

function App() {
  const [ list, setList ] = useState([]) //setting list to an empty array using useState
  return (
    <div className="App container" style={{ width: '500px'}}>
      {list.map((task, i) => (
        <Task task={task} setList={setList} index={i} list={list}/>
      ))}
      <Input list={list} setList={setList} /> 
      {/* //sending list as list and setList as setList to Input component */}
    </div>
  );
}

export default App;
