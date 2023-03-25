import React from 'react';

function Table({ data }) {
  return (
    <table>
      <tbody>
        {/* Map over each row in the data array */}
        {data.map((row, rowIndex) => (
          <tr key={rowIndex}>
            {/* Map over each value in the row array */}
            {row.map((value, colIndex) => (
              <td key={`${rowIndex}-${colIndex}`}>{value}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Table;
