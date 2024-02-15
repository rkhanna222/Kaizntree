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
    <div className="item-list">
      {items.map(item => (
        <div key={item.sku} className="item">
          <div>{item.sku}</div>
          <div>{item.name}</div>
          {/* Add more item properties here as needed */}
        </div>
      ))}
    </div>
  );
}

export default ItemList;
