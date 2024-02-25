import React from "react";
import { createRoot } from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import NavigationBar from "./Components/NavBar/NavBar";
import "./index.css";
import Landing from "./Pages/Landing/Landing";
import AllTimeStatsPage from "./Pages/AllTimeStatsPage/AllTimeStatsPage";
import MostRecentDrivePage from "./Pages/MostRecentDrivePage/MostRecentDrivePage";

const App = () => {
  return (
    <div>
      <NavigationBar />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/all-time-stats" element={<AllTimeStatsPage />} />
        <Route path="/most-recent-drive" element={<MostRecentDrivePage />} />
      </Routes>
    </div>
  );
};



// Use createRoot instead of ReactDOM.render
const container = document.getElementById('root');
const root = createRoot(container);

root.render(
  <Router>
    <App />
  </Router>
);
