import React, { useState } from 'react';

const UserForm = (props) => {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [cfmPassword, setcfmPassword] = useState("");

    const createUser = (e) => {
        e.preventDefault();
        const newUser = { firstName, lastName, email, password };
        console.log(`Welcome, ${newUser}`)
    }
        

    return(
        <div>
            <form onSubmit={ createUser }>
                <div>
                    <label> First Name: </label>
                    <input type="text" onChange={ (e) => setFirstName(e.target.value)} />
                </div>
                <div>
                    <label> Last Name: </label>
                    <input type="text" onChange={ (e) => setLastName(e.target.value)} />
                </div>
                <div>
                    <label> Email: </label>
                    <input type="text" onChange={ (e) => setEmail(e.target.value)} />
                </div>
                <div>
                    <label> Password: </label>
                    <input type="password" onChange={ (e) => setPassword(e.target.value)} />
                </div>
                <div>
                    <label> Comfirm Password: </label>
                    <input type="password" onChange={ (e) => setcfmPassword(e.target.value)}/>
                </div>
                <div>
                    Your Form Data
                </div>
                <div>
                    <p>
                        First Name   {firstName}
                    </p>
                    <p>
                        Last Name   {lastName}
                    </p>
                    <p>
                        Email   {email}
                    </p>
                    <p>
                        Password   {password}
                    </p>
                    <p>
                        Confirm   {cfmPassword}
                    </p>
                </div>

            </form>
        </div>
    );
};

export default UserForm;
