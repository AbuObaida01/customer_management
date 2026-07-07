import "./Navbar.css";
import { useNavigate } from "react-router-dom";

function Navbar() {

    const navigate = useNavigate();

    const logout = () => {

        localStorage.removeItem("token");

        navigate("/login");

    };

    return (

        <div className="navbar">

            <h2>Customer Management System</h2>

            <button
                className="logout-btn"
                onClick={logout}
            >
                Logout
            </button>

        </div>

    );

}

export default Navbar;