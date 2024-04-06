import React from "react";
import "./Aside.css";

function Aside(props) {
    return (
        <div className="aside">
            <div className="asideContent">
                <div className="walletDisplay">
                    <h1 className="walletTotal">${props.save} <span style={{fontSize: `1rem`, textTransform: `uppercase`}}>FOS</span></h1>
                    <h2>${props.saveTotal} <span style={{fontSize: `1rem`, textTransform: `uppercase`}}>Total</span></h2>
                </div>
            </div>
        </div>
    );
}

export default Aside;
