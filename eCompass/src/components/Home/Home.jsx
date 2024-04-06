import React, { useState, useEffect } from 'react';
import Dashboard from '../Dashboard/Dashboard';
import Aside from '../Aside/Aside';
import './Home.css';

function Home() {
  const [userData, setUserData] = useState({
    name: '',
    save: 0,
    saveTotal: 0,
    mensualSaveEstimated: 0
  });

  useEffect(() => {
    fetch('http://10.7.18.5:5000/user?id=2')
      .then(response => response.json())
      .then(data => {
        setUserData(data);
      })
      .catch(error => {
        console.error('Error fetching user data:', error);
      });

    fetch('http://10.7.18.5:5000/plannings?id=2')
      .then(response => response.json())
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error fetching plannings data:', error);
      });
  }, []);

  function openPlanModalFunction() {
    document.querySelector('.planModal').style.opacity = '1';
    document.querySelector('.planModalBackdrop').style.opacity = '1';
    document.querySelector('.planModal').style.pointerEvents = 'all';
    document.querySelector('.planModalBackdrop').style.pointerEvents = 'all';
  }

  function closePlanModalFunction() {
    document.querySelector('.planModal').style.opacity = '0';
    document.querySelector('.planModalBackdrop').style.opacity = '0';
    document.querySelector('.planModal').style.pointerEvents = 'none';
    document.querySelector('.planModalBackdrop').style.pointerEvents = 'none';
  }

  function postear() {
    const name = document.getElementById('name').value;
    const cost = document.getElementById('cost').value;
    let saves = document.getElementById('saves').value;;
    
    

    fetch('http://10.7.18.5:5000/plannings?id=2', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: name,
        cost: parseInt(cost),
        saves: parseInt(saves),
        savesAcu: 0
      })
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
      })
      .catch(error => {
        console.error('Error creating plan:', error);
      });
  }

  return (
    <div className='home'>
      <div className="upperSection">
        <h1 className='welcome'>Welcome back, {userData.name}!</h1>
        <div className="userInfo">
          <h5>Free savings: ${userData.save}</h5>
          <h5>Total savings: ${userData.saveTotal}</h5>
          <h5>Monthly savings: ${userData.mensualSaveEstimated}</h5>
        </div>
        <button className='currencySelect'>Currency: <span id='currency'>ARS</span></button>
      </div>
      <div className="main">
        <Dashboard />
        <Aside saveTotal={userData.saveTotal} save={userData.save} />
      </div>

      <button onClick={openPlanModalFunction} title="Create a plan" className="createPlan">
        <svg xmlns="http://www.w3.org/2000/svg" className="icon icon-tabler icon-tabler-plus" width="36" height="36" viewBox="0 0 24 24" strokeWidth="1.5" stroke="#76ABAE" fill="none" strokeLinecap="round" strokeLinejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
          <path d="M12 5l0 14" />
          <path d="M5 12l14 0" />
        </svg>
        <h4>Create a plan</h4>
      </button>

      <div className="planModal">
        <div className="planModalContent">
          <div className="planModalHeader">
            <h1>Create a plan</h1>
            <button onClick={closePlanModalFunction} className="closePlanModal">
              <svg xmlns="http://www.w3.org/2000/svg" className="icon icon-tabler icon-tabler-x" width="32" height="32" viewBox="0 0 24 24" strokeWidth="1.5" stroke="#76ABAE" fill="none" strokeLinecap="round" strokeLinejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            </button>
          </div>
          <div className="planModalBody">
            <form>
              <div className='formItem'>
                <label htmlFor="name">Plan name:</label>
                <input type="text" id="name" name="name" required />
              </div>
              <div className='formItem'>
                <label htmlFor="cost">Total plan cost:</label>
                <input type="number" id="cost" name="cost" required />
              </div>
              <div className='formItem'>
                <label htmlFor="saves">Estimated monthly save percentage (%):</label>
                <input type="number" id="saves" name="saves" required />
              </div>
              <button onClick={postear} type="button">Create</button>
            </form>
          </div>
        </div>
      </div>
      <div className="planModalBackdrop"></div>
    </div>
  );
}

export default Home;
