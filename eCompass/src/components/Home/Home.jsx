import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

import Progress from '../Progress/Progress';

function Home(props) {
  return (
    <main className='home'>
        <div className="upperSection">
            <h1 className='welcome'>Welcome back, {props.name}!</h1>
        </div>
      <div className="data">
        <Progress name="Auto" totalAmount="12300" estimatedAmount="21000" estimatedTime="320"/>
      </div>
    </main>
  );
}

export default Home;
