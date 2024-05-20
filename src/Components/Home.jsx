import './Home.css';
import videoBg from '../assets/home.mp4';
function Home() {
  return (
    <div className="fullscreen-bg">
      <video autoPlay muted loop className="fullscreen-bg__video">
        <source src={videoBg} type="video/mp4" />
        
      </video>
      <div className="content">
        <h2>Medi-Spective</h2>
        <h3>A holistic approach to tackle and maintain your mental health</h3>
        <button><a href="/login" alt = "login">Login</a></button>
      </div>
    </div>
  );
}

export default Home;
