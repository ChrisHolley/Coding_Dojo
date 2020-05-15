import React, { useState } from 'react';
import './App.css';
import UserForm from './component/UserForm'
import UserResults from './component/UserResults'

function App() {
  const [read, write] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: ""
  });

  return (
    <div className="App">
      <UserForm inputs={read} writeInputs={write} />
      <UserResults data={read}/>
    </div>
  );
}

export default App;
