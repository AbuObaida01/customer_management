function FilterBar({

    filters,

    setFilters,

    onSearch,

    onReset

}) {

    const handleChange = (event) => {

        setFilters({

            ...filters,

            [event.target.name]: event.target.value

        });

    };

    return (

        <div>

            <h3>Search Customers</h3>

            <input
                type="text"
                name="city"
                placeholder="City"
                value={filters.city}
                onChange={handleChange}
            />

            <input
                type="text"
                name="country"
                placeholder="Country"
                value={filters.country}
                onChange={handleChange}
            />

            <input
                type="text"
                name="company"
                placeholder="Company"
                value={filters.company}
                onChange={handleChange}
            />

            <input
                type="text"
                name="email"
                placeholder="Email"
                value={filters.email}
                onChange={handleChange}
            />

            <button onClick={onSearch}>
                Search
            </button>

            <button onClick={onReset}>
                Reset
            </button>

        </div>

    );

}

export default FilterBar;