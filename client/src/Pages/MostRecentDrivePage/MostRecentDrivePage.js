import React, { useEffect, useState } from 'react';

import { fetchGet, fetchPost } from '../../util/fetchHelp.js';
import StatisticBar from '../../Components/Statistic/StatisticBar.js';
import './MostRecentDrivePage.css';

function MostRecentDrivePage() {
  const [getData, setGetData] = useState()

  useEffect(() =>{
    fetchGet("/get-most-recent-drive-stats").then(data => {
      setGetData(data.message);
    });
  })

  return (
    <div className="App">
      {(typeof getData === "undefined") ? (
        <p>Loading...</p>
      ): (
        <div className="statistics-container">
            <StatisticBar
                statisticLabel="# of times you texted"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you talked on the phone"
                userOccurrences="50"
                medianValue="60"
            />
            <StatisticBar
                statisticLabel="# of times you messed with infotainment"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you drank"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you reached into the backseat"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you did hair or makeup"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were distracted by your passengers"
                userOccurrences="50"
                medianValue="40"
            />
        </div>
      )}
    </div>
  );
}

export default MostRecentDrivePage;
