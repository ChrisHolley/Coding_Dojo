import React from 'react';

const UserForm = props => {
    const { inputs, writeInputs } = props;

    const onChangeHandler = e => {
        writeInputs({
            ...inputs,
            [e.target.name]: e.target.value
        });
    };
    return(
        <form>
            <div>
                {
                    inputs.firstName.length > 2 || inputs.firstName.length == 0 ?
                    <p></p> : <p>Name must be greater than 2 characters</p>
                }
            <label htmlFor="firstName">First Name:</label>
            <input type="text" onChange={onChangeHandler} name="firstName" />
            </div>
            <div>
                {
                    inputs.lastName.length > 2 || inputs.lastName.length == 0 ?
                    <p></p> : <p>Last name must be greater than 2 characters</p>
                }
            <label htmlFor="lastName">Last Name:</label>
            <input type="text" onChange={onChangeHandler} name="lastName" />
            </div>
            <div>
            {
                    inputs.email.length > 4 || inputs.email.length == 0 ?
                    <p></p> : <p>Email must be at least 5 characters</p>
                }
            <label htmlFor="email">Email:</label>
            <input type="text" onChange={onChangeHandler} name="email" />
            </div>
            <div>
            {
                    inputs.password.length > 7 || inputs.password.length == 0 ?
                    <p></p> : <p>Password must be greater than 8 characters</p>
                }
            {
                    inputs.password == inputs.confirmPassword ?
                    <p></p> : <p>Passwords do not match</p>
                }
            <label htmlFor="password">Password:</label>
            <input type="password" onChange={onChangeHandler} name="password" />
            </div>
            <div>
            <label htmlFor="confirmPassword">Confirm Password:</label>
            <input type="password" onChange={onChangeHandler} name="confirmPassword" />
            </div>
        </form>
    );
}
export default UserForm;