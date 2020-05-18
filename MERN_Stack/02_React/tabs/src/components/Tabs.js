import React from 'react';

const Tabs = props => {
    return(
        <button onClick={props.changeValue}>{props.tabLabel}</button>
    );
}
export default Tabs;