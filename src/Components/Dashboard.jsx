import CommunityForum from './CommunityForum';
import React from 'react';
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import Home from './Home';
import JournalEntry from './JournalEntry';
import Login from './Login';
import "./Dashboard.css";



function Dashboard() {
   
  return (
    
    <JournalEntry>
        <div className="Dashboard">
            <h1>Dashboard</h1>
            <p>Dashboard coming soon!</p>
        </div>
    </JournalEntry>
  );


}



export default Dashboard;