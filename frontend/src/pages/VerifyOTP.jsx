import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Login.css";
import api from "../services/api";

function VerifyOTP() {
    const navigate = useNavigate();
    const [otp, setOtp] = useState("");
    const [message, setMessage] = useState("");
    const email = localStorage.getItem("loginEmail");
    useEffect(() => {
        if (!email) {
            navigate("/login");
        }
    }, [email, navigate]);
    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await api.post(
                "/verify-otp",
                {
                    email: email,
                    otp: otp
                }
            );
            localStorage.setItem(
                "token",
                response.data.access_token
            );
            localStorage.removeItem(
                "loginEmail"
            );
            navigate("/dashboard");
        }
        catch (error) {
            if (error.response) {
                setMessage(
                    error.response.data.detail
                );
            }
            else {
                setMessage(
                    "OTP verification failed."
                );
            }
        }
    };
    return (
        <div className="login-container">
            <h2 className="login-title">
                Verify OTP
            </h2>
            <p>
                OTP has been sent to:
                <br />
                <strong>{email}</strong>
            </p>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>OTP</label>
                    <br />
                    <input
                        type="text"
                        value={otp}
                        onChange={(event) => setOtp(event.target.value)}
                        placeholder="Enter 6-digit OTP"
                        required
                    />
                </div>
                <br />
                <button type="submit">
                    Verify OTP
                </button>
            </form>
            <br />
            <p>{message}</p>
        </div>
    );
}

export default VerifyOTP;