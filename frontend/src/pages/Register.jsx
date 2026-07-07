import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import "./Register.css";
import api from "../services/api";

function Register() {

    const navigate = useNavigate();

    const [formData, setFormData] = useState({

        username: "",

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

            const response = await api.post(
                "/register",
                formData
            );

            setMessage(response.data.message);

            setTimeout(() => {

                navigate("/login");

            }, 1500);

        }

        catch (error) {
            console.log(error);

            console.log(error.response);
        
            console.log(error.message);

            if (error.response) {

                setMessage(error.response.data.detail);

            }

            else {

                setMessage(error.message);

            }

        }

    };

    return (

        <div className="register-container">

            <h2 className="register-title">
                Customer Management System
            </h2>

            <form className="card register-form" 
            onSubmit={handleSubmit}>

                <div>

                    <label>Username</label>

                    <br />

                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                        required
                    />

                </div>

                <br />

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

                    Register

                </button>

            </form>

            <br />

            <p className={
                message === "User registered successfully."
                ? "message-success"
                : "message-error"
            }>

                {message}

            </p>

            <p className="register-footer">

                Already have an account?

                <Link to="/login">

                    Login

                </Link>

            </p>

        </div>

    );

}

export default Register;