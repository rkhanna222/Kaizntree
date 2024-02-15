import React, { useState, useEffect } from 'react';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('token'); // Ensure you're retrieving the token correctly
    if (token) {
      fetch('http://localhost:8000/api/items/', {
        method: 'GET', // Explicitly state the method, though 'GET' is default
        headers: {
          'Authorization': `Token ${token}`, // Adjust according to the token type ('Bearer' if JWT)
          'Content-Type': 'application/json', // This might be required depending on your backend
        },
        // credentials: 'include' if your server requires sending cookies, but usually not needed for token auth
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setItems(data))
      .catch(error => console.error('There was an error!', error));
    }
  }, []);

  return (
    <div className="dashboard-container">
      <div className="top-bar">
        {/* You will need to fetch and display summary data here */}
        <div>Total Categories: {/* Categories count */}</div>
        <div>Total Items: {/* Items count */}</div>
      </div>
      <div className="content">
        <button className="new-category-btn">NEW ITEM CATEGORY</button>
        {/* ... Other controls like subcategory and search ... */}
        <div className="item-list">
          <table>
            <thead>
              <tr>
                <th>SKU</th>
                <th>Name</th>
                <th>Tags</th>
                <th>Category</th>
                <th>In Stock</th>
                <th>Available Stock</th>
              </tr>
            </thead>
            <tbody>
              {items.map(item => (
                <tr key={item.sku}>
                  <td>{item.sku}</td>
                  <td>{item.name}</td>
                  <td>{/* Render tags here */}</td>
                  <td>{item.category}</td>
                  <td>{/* Render stock status indicator here */}</td>
                  <td>{item.available_stock}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );

}

export default ItemList;
