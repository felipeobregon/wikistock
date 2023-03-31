import { useState, useEffect } from 'react';
import Table from './table.js'

export default function Content() {
  const [tableData, setTableData] = useState([]);
  const [pageIndex, setPageIndex] = useState(1);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch(`http://localhost:5000/data?page=${pageIndex}`);
      const data = await response.json();
      setTableData(data.data);
    }

    fetchData();
  }, [pageIndex]);

  function handlePrev() {
    setPageIndex(prevPageIndex => Math.max(prevPageIndex - 1, 0));
  }

  function handleNext() {
    setPageIndex(prevPageIndex => prevPageIndex + 1);
  }

  return (
    <>
        <h1>Page: {pageIndex}</h1>
        <Table data={tableData} />
        <button onClick={handlePrev}>Prev</button>
        <button onClick={handleNext}>Next</button>
    </>
  );
}
