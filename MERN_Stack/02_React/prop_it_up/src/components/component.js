import React, { Component } from 'react';

class PersonCard extends Component {
    render() {
        return <div style={{textAlign:"justify"}}>
            <h2 style={{}}>{this.props.lastName}, {this.props.firstName} </h2>
            <p>Age: {this.props.age}</p>
            <p>Hair Color: {this.props.hairColor}</p>


        </div>;
    }
}
export default PersonCard;

// Create a component called PersonCard that accepts the following props: 

// firstName
// lastName
// age
// hairColor