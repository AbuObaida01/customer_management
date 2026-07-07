function CustomerTable({ customers }) {

    return (

        <table border="1">

            <thead>

                <tr>

                    <th>Customer ID</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Company</th>
                    <th>City</th>
                    <th>Country</th>
                    <th>Email</th>

                </tr>

            </thead>

            <tbody>

                {

                    customers.map((customer) => (

                        <tr key={customer.customer_id}>

                            <td>{customer.customer_id}</td>

                            <td>{customer.first_name}</td>

                            <td>{customer.last_name}</td>

                            <td>{customer.company}</td>

                            <td>{customer.city}</td>

                            <td>{customer.country}</td>

                            <td>{customer.email}</td>

                        </tr>

                    ))

                }

            </tbody>

        </table>

    );

}

export default CustomerTable;