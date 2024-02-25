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
                statisticLabel="# of times you were texting"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were talking on phone"
                userOccurrences="50"
                medianValue="60"
            />
            <StatisticBar
                statisticLabel="# of times you were operating the radio"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were drinking"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were reaching behind"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were hair and makeup"
                userOccurrences="50"
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were talking to passanger"
                userOccurrences="50"
                medianValue="40"
            />
        </div>
      )}
    </div>
  );
}

export default MostRecentDrivePage;
