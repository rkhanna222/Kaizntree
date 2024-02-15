// App.js or similar top-level component
import React, { useState } from 'react';
import Login from './components/Login';
import Dashboard from './components/Dashboard'; 

const App = () => {
  const [auth, setAuth] = useState({ token: null });

  const handleLoginSuccess = (data) => {
    setAuth({ token: data.token });
    localStorage.setItem('token', data.token); // Save token for future sessions
  };

  return (
    <div>
      {!auth.token ? (
        <Login onLoginSuccess={handleLoginSuccess} />
      ) : (
        // Show your protected component or redirect to it
        <Dashboard />
      )}
    </div>
  );
};

export default App;
