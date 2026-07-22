import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./Login.css";
import api from "../services/api";

function Login() {

    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: "",
        password: ""
    });

    const [message, setMessage] = useState("");
    const handleChange = (event) => {
        setFormData({
            ...formData,
            [event.target.name]: event.target.value
        });
    };
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const params = new URLSearchParams();
            params.append(
                "username",
                formData.email
            );
            params.append(
                "password",
                formData.password
            );
            const response = await api.post(
                "/login",
                params,
                {
                    headers: {
                        "Content-Type":
                        "application/x-www-form-urlencoded"
                    }
                }
            );
            localStorage.setItem(
                "loginEmail",
                formData.email
            );
            setMessage(
                response.data.message
            );
            navigate("/verify-otp");
        }
        catch (error) {
            if (error.response) {
                setMessage(
                    error.response.data.detail
                );
            }
            else {
                setMessage(
                    "Login failed."
                );
            }
        }
    };
    return (
        <div className="login-container">
            <h2 className="login-title">
                Customer Management System
            </h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Email</label>
                    <br />
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                    />
                </div>
                <br />
                <div>
                    <label>Password</label>
                    <br />
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                        required
                    />
                </div>
                <br />
                <button type="submit">
                    Login
                </button>
            </form>
            <br />
            <p>{message}</p>
            <p>
                Don't have an account?
                <Link to="/register">
                    Register
                </Link>
            </p>
        </div>
    );
}
export default Login;