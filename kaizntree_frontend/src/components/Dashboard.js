// Dashboard.js
import React from 'react';
//import Sidebar from './Sidebar';
import ItemList from './ItemList';
//import SearchBar from './SearchBar';
//import SummaryCards from './SummaryCards';

const Dashboard = () => {
  return (
    <div className="dashboard">
      {/* <Sidebar /> */}
      <div className="main-content">
        {/* <SummaryCards />
        <SearchBar /> */}
        <ItemList />
      </div>
    </div>
  );
};

export default Dashboard;
