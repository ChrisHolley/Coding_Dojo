import React from "react";

class Counter extends React.Component {
    constructor(prop){
        super(prop);        

        this.state = {
            clickCount: 0
        }
    }

    clickHandler = event => {
        this.setState({
            clickCount: this.state.clickCount +1
        })
    }

    render() {
        return (
            <div>
                <button onClick={this.clickHandler}>
                    Clicked: {this.state.clickCount} times
                </button>
                
            </div>
        )
    }
}

export default Counter;