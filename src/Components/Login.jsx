import './Login.css'
import imagebg from '../assets/welcome.jpg'
export default function Login() {
    return (
        <div>
        <img src={imagebg} alt="background" className="background"/>
        <h1 className="login">Login</h1>
        <form>
            <label>
            Username:
            <input type="text" name="username" />
            </label>
            <label>
            Password:
            <input type="password" name="password" />
            </label>
            <button type="submit">Submit</button>
        </form>
        </div>
    );
    }