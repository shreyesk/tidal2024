import React, { useEffect, useState } from 'react';

import StatisticBar from '../../Components/Statistic/StatisticBar.js';
import { fetchGet } from '../../util/fetchHelp.js';
import './MostRecentDrivePage.css';

function MostRecentDrivePage() {
  const [driveData, setDriveData] = useState([])

  useEffect(() =>{
    fetchGet("/get-most-recent-drive-stats").then(data => {
      setDriveData(data.message);
      console.log(driveData);
    });
  })

  return (
    <div className="App">
      {(typeof driveData === "undefined") ? (
        <p>Loading...</p>
      ): (
        <div className="statistics-container">
            <StatisticBar
                statisticLabel="# of times you were texting"
                userOccurrences={driveData[1]}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were talking on phone"
                userOccurrences={driveData[2]}
                medianValue="60"
            />
            <StatisticBar
                statisticLabel="# of times you were operating the radio"
                userOccurrences={driveData[3]}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were drinking"
                userOccurrences={driveData[4]}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were reaching behind"
                userOccurrences={driveData[5]}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were hair and makeup"
                userOccurrences={driveData[6]}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were talking to passanger"
                userOccurrences={driveData[7]}
                medianValue="40"
            />
        </div>
      )}
    </div>
  );
}

export default MostRecentDrivePage;
