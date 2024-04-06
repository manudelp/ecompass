import React, { useState, useEffect } from 'react';
import Progress from '../Progress/Progress';
import './Home.css';


function Home() {
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    fetch('http://10.7.18.5:5000/user')
      .then(response => response.json())
      .then(data => {
        const { id, name, save, saveTotal, mensualSaveEstimated } = data;
        setUserData({ id, name, save, saveTotal, mensualSaveEstimated });
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });
  }, []);

  var userName = userData ? userData.name : '';


  return (
    <div className='home'>
        <div className="upperSection">
            <h1 className='welcome'>Welcome back, <strong>{userName}</strong>!</h1>
            <div className="userInfo">
              <h4 className="userSavings">Free savings: ${userData.save}</h4>
              <h4 className="userSavings">Total savings: ${userData.saveTotal}</h4>
              <h4 className="userSavings">Monthly savings: ${userData.mensualSaveEstimated}</h4>
            </div>
        </div>
        <div className="main">
          <div className="data">
            <div className='sections'>
              <h4 className='progressCategoryTitle'>Progress</h4>
              <h4 className='progressCategoryTitle'>Savings</h4>
              <h4 className='progressCategoryTitle'>Investments</h4>
              <h4 className='progressCategoryTitle'>Other</h4>
              <div className="selectedCategory"></div>
            </div>
            <Progress name="Car" totalAmount="12300" estimatedAmount="21000" estimatedEndDate="2025-11"/>
            <Progress name="PC" totalAmount="2033" estimatedAmount="2430" estimatedEndDate="2024-04"/>
            <Progress name="TV" totalAmount="282" estimatedAmount="300" estimatedEndDate="2024-05"/>
          </div>
          <aside className="createPlan">
              <h4>Create a new plan</h4>
          </aside>
        </div>
    </div>
  );
}

export default Home;
