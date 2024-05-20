import { Link } from 'react-router-dom';
import './Navbar.css';

/*
Starter Code for Navbar Component
Will change to display profile Dashboard, CommunityForum, Home, Resources, and Logout
*/
function Navbar() {
  return (
    <div className="navbar-container">
      <nav>
        <ul>
          <li><Link to="/" className="button">*Home*</Link></li>
          <li><Link to="/dashboard" className="button">*Dashboard*</Link></li>
          <li><Link to="/login" className="button">*Login*</Link></li>
          <li><Link to="/community-forum" className="button">*Community Forum*</Link></li>
        </ul>
      </nav>
    </div>
  );
}

export default Navbar;

