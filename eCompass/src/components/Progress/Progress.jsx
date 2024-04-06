import React, { useState, useEffect } from "react";
import "./Progress.css";

function Progress(props) {
    const [progressWidth, setProgressWidth] = useState(0);

    useEffect(() => {
        const estimatedAmountPercentage = (props.totalAmount / props.estimatedAmount) * 100;
        setProgressWidth(estimatedAmountPercentage);
    }, [props.estimatedAmount, props.totalAmount]);

    var timeLeft = props.estimatedEndDate;
    var timeLeftString = convertDays(timeLeft);

    return (
        <div className="progress">
            <h4 className="progressTitle">{props.name}</h4>
            <div className="progressGraph">
                <h2 className="amountProgress" style={{width: `${progressWidth}%`}}>${props.totalAmount}</h2>
                <h2 className="amountTotal">${props.estimatedAmount}</h2>
                <div className="progressBar">
                    <div className="progressBarFill" style={{width: `${progressWidth}%`}}></div>
                </div>
            </div>
            <h2 className="progressPercentage">{Math.floor(progressWidth)}%</h2>
            <h2 className="timeLeft">{timeLeftString}</h2>
        </div>
    );

    function convertDays(time){
        let timeString = "";

        const today = new Date();
        const endDate = new Date(time);
        const timeDifference = endDate - today;
        const daysDifference = timeDifference / (1000 * 60 * 60 * 24);
        const yearsDifference = Math.floor(daysDifference / 365);
        const monthsDifference = Math.floor((daysDifference % 365) / 30);

        if (yearsDifference >= 5) {
            timeString = "+5 years";
        } else if(yearsDifference > 0){
            timeString = `${yearsDifference} years`;
        } else if(monthsDifference > 0){
            timeString = `${monthsDifference} months`;
        } else{
            timeString = "Less than a month";
        }

        return timeString;
    }
}


export default Progress;
