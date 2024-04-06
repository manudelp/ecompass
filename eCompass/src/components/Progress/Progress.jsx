import React, { useState, useEffect } from "react";
import "./Progress.css";

function Progress(props) {
    const [progressWidth, setProgressWidth] = useState(0);

    useEffect(() => {
        const estimatedAmountPercentage = (props.totalAmount / props.estimatedAmount) * 100;
        var progressBarFill = document.querySelector(".progressBarFill");
        progressBarFill.style.width = estimatedAmountPercentage + "%";
        setProgressWidth(estimatedAmountPercentage);
    }, [props.estimatedAmount, props.totalAmount]);

    return (
        <div className="progress">
            <h2 className="progressTitle">{props.name}</h2>
            <div className="progressGraph">
                <h2 className="amountProgress">{props.totalAmount}</h2>
                <div className="progressBar">
                    <div className="progressBarFill"></div>
                </div>
            </div>
            <h2 className="progressPercentage">{Math.floor(progressWidth)}%</h2>
        </div>
    );
}

export default Progress;
