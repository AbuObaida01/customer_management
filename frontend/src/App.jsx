import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import VerifyOTP from "./pages/VerifyOTP";

function App() {
    return (
        <Routes>
            <Route
                path="/"
                element={<Navigate to="/login" />}
            />
            <Route
                path="/login"
                element={<Login />}
            />
            <Route
                path="/register"
                element={<Register />}
            />
            <Route
                path="/verify-otp"
                element={<VerifyOTP />}
            />
            <Route
                path="/dashboard"
                element={<Dashboard />}
            />
        </Routes>
    );
}

export default App;