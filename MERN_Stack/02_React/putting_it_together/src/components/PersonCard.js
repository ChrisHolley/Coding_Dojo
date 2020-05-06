import React, { Component } from 'react';
const Button = (props) => {
    return (
        <button onClick={props.handleClick}>Birthday Button for {props.name}</button>
    );
}
class PersonCard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            ageCount: props.age
        }
    }
    handleClick = () => {
        this.setState({
            ageCount: this.state.ageCount+=1
        })
    }
    render() {
        const {firstName, lastName, age, hairColor} = this.props;
        
        return (
            <div>
                <h2>{lastName}, {firstName}</h2>
                <p>Age: {this.state.ageCount}</p>
                <p>Hair Color: {hairColor}</p>
                <Button handleClick={this.handleClick} name={firstName}/>
            </div>
        );
    }
}
export default PersonCard;