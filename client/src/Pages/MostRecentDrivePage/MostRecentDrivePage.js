import React, { useEffect, useState } from 'react';

import { fetchGet, fetchPost } from '../../util/fetchHelp.js';
import StatisticBar from '../../Components/Statistic/StatisticBar.js';
import './MostRecentDrivePage.css';

function MostRecentDrivePage() {
  const [getData, setGetData] = useState();

  useEffect(() =>{
    fetchGet("/get-most-recent-drive-stats").then(data => {
      setGetData(data);
      console.log("MOSTRECENT: data: ", data);
    });
  }, []);

  return (
    <div className="App">
      {(typeof getData === "undefined") ? (
        <p>Loading...</p>
      ): (
        <div className="statistics-container">
            <StatisticBar
                statisticLabel="# of times you texted"
                userOccurrences={getData['texting']}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you talked on the phone"
                userOccurrences={getData['talking on phone']}
                medianValue="60"
            />
            <StatisticBar
                statisticLabel="# of times you messed with infotainment"
                userOccurrences={getData['operating the radio']}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you drank"
                userOccurrences={getData['drinking']}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you reached into the backseat"
                userOccurrences={getData['reaching behind']}
                medianValue="40"
            />
            <StatisticBar
                statisticLabel="# of times you were distracted by your passengers"
                userOccurrences={getData['talking to passenger']}
                medianValue="40"
            />
        </div>
      )}
    </div>
  );
}

export default MostRecentDrivePage;
