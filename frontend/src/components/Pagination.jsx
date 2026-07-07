function Pagination({

    page,

    pageSize,

    totalRecords,

    setPage

}) {

    return (

        <div>

            <button
                disabled={page === 1}
                onClick={() => setPage(page - 1)}
            >

                Previous

            </button>

            <span>

                {" "}Page {page}{" "}

            </span>

            <button
                disabled={page * pageSize >= totalRecords}
                onClick={() => setPage(page + 1)}
            >

                Next

            </button>

        </div>

    );

}

export default Pagination;