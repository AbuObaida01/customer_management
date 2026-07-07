import FilterBar from "../components/FilterBar";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Dashboard.css";
import api from "../services/api";

import Navbar from "../components/Navbar";
import CustomerTable from "../components/CustomerTable";
import Pagination from "../components/Pagination";

function Dashboard() {

    const navigate = useNavigate();

    const [customers, setCustomers] = useState([]);
    const [filters, setFilters] = useState({

        city: "",
    
        country: "",
    
        company: "",
    
        email: ""
    
    });
    const [page, setPage] = useState(1);

    const pageSize = 20;

    const [totalRecords, setTotalRecords] = useState(0);

    const fetchCustomers = async () => {

        try {

            const response = await api.get(
                "/customers",
                {
                    params: {

                        page,
                    
                        page_size: pageSize,
                    
                        city: filters.city,
                    
                        country: filters.country,
                    
                        company: filters.company,
                    
                        email: filters.email
                    
                    }
                }
            );

            setCustomers(response.data.data);

            setTotalRecords(
                response.data.total_records
            );

        }

        catch (error) {

            if (error.response?.status === 401) {

                localStorage.removeItem("token");

                navigate("/login");

            }

            else {

                console.log(error);

            }

        }

    };
    const searchCustomers = () => {
        if(page==1){
            fetchCustomers();
        }
        else{
        setPage(1);
        }
    
    
    };
    const resetFilters = () => {

        setFilters({
    
            city: "",
    
            country: "",
    
            company: "",
    
            email: ""
    
        });
    
        if (page === 1) {

            fetchCustomers();
    
        }
    
        else {
    
            setPage(1);
    
        }
    
    };
    useEffect(() => {
        const token = localStorage.getItem("token");

        if (!token) {
    
            navigate("/login");
    
            return;
    
        }

        fetchCustomers();

    }, [page]);

    return (

        <>

            <Navbar />
            <div className="dashboard-card">

    <h2 className="dashboard-title">

        Customers

    </h2>

    <p>

        Total Records : {totalRecords}

    </p>

    <br />

    <FilterBar
        filters={filters}
        setFilters={setFilters}
        onSearch={searchCustomers}
        onReset={resetFilters}
    />

    <br />

    <CustomerTable
        customers={customers}
    />

    <br />

    <Pagination
        page={page}
        pageSize={pageSize}
        totalRecords={totalRecords}
        setPage={setPage}
    />

</div>
    </>

    );

}

export default Dashboard;