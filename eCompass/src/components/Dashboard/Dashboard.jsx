import React, { useEffect, useState } from "react";
import "./Dashboard.css";

import Progress from "../Progress/Progress";

function Dashboard() { 
    
    const [dashboardData, setDashboardData] = useState(false);
    return (
        <div className="dashboard">
            <DashboardHeader click={setDashboardData}/>
            <DashboardAll is={dashboardData} />
        </div>
    );
}

function DashboardAll({is}){
    console.log(is);
    return (
        is ? <DashboardProgress /> : <DashboardContent />
    )
}
function DashboardHeader({click}) {

    function handleClick(algo) {
        click(algo);
    }
    return(
        <div className="dashboardHeader">
            <button onClick={() => handleClick(false)} className="categoryTitle">Savings</button>
            <button onClick={() => handleClick(true)} className="categoryTitle">Progress</button>
            <span className="selectedCategory"></span>
        </div>
    );
}

function DashboardProgress() {
    const [planningsData, setPlanningsData] = useState([]);
    useEffect(() => {
        
            fetch("http://10.7.18.5:5000/plannings?id=2")
            .then(response => response.json())
            .then(data => {
                setPlanningsData(data);
            })
            .catch(error => {
                console.error('Error fetching planning data:', error);
            });
        
    },[]);
        console.log(planningsData)
        return (
            <div className="dashboardContent">
                <div className="dashboardContentHeader">
                    <h6>Name</h6>
                    <h6>Progress</h6>
                    <h6>Percentage</h6>
                    <h6>Estimated Time</h6>
                </div>
                {planningsData.map((planning, index) => {
                    return (
                        <Progress
                            key={index}
                            name={planning.name}
                            saves={planning.saves}
                            totalAmount={planning.savesAcu}
                            estimatedAmount={planning.cost}
                            estimatedEndDate={planning.dateEnd}
                        />
                    );
                })}
            </div>
        );

        
    }

    function DashboardContent(){
        return (
            <div className="dashboardContent">
                <h1>hola</h1>
            </div>
        );
    }

export default Dashboard;
