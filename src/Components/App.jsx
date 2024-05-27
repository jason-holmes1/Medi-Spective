import React from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Dashboard from './Dashboard';
import Login from './Login';
import CommunityForum from './CommunityForum';
import Resources from './Resources';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/login" component={Login} />
          <Route path="/community-forum" component={CommunityForum} /> 
          <Route path="/resources" component={Resources} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;
