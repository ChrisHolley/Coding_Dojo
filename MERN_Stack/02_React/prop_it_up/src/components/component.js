import React, { Component } from 'react';

class PersonCard extends Component {
    constructor(props) {
        super(props);
        this.age = this.props.age
    }
    render() {
        return <div style={{textAlign:"justify"}}>
            <h2 style={{}}>{this.props.lastName}, {this.props.firstName} </h2>
            <p>Age: {this.age}</p>
            <p>Hair Color: {this.props.hairColor}</p>
            <button onClick = { () => {
                this.age += 1;
                this.setState({ age: this.age});
                
                } }>Birthday Button for {this.props.firstName} {this.props.lastName}</button>
            {/* <button onClick = { () => {
                this.setState({ age: this.age})
                
                } }>Birthday Button for {this.props.firstName} {this.props.lastName}</button> */}

        </div>;
    }
}
export default PersonCard;

// Create a component called PersonCard that accepts the following props: 

// firstName
// lastName
// age
// hairColor