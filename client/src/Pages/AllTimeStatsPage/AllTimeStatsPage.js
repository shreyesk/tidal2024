import React, { useEffect, useState } from "react";

import StatisticBar from "../../Components/Statistic/StatisticBar.js";
import { fetchGet } from "../../util/fetchHelp.js";
import "./AllTimeStatsPage.css";

function AllTimeStatsPage() {
  const [getData, setGetData] = useState([])

  useEffect(() => {
    fetchGet("/get-all-time-drive-stats").then((data) => {
      setGetData(data);
      console.log("ALLTIME: data: ", data);
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
                numMinutes={getData['drive time']}
            />
            <StatisticBar
                statisticLabel="# of times you talked on the phone"
                userOccurrences={getData['talking on phone']}
                numMinutes={getData['drive time']}
            />
            <StatisticBar
                statisticLabel="# of times you drank"
                userOccurrences={getData['drinking']}
                numMinutes={getData['drive time']}
            />
            <StatisticBar
                statisticLabel="# of times you reached into the backseat"
                userOccurrences={getData['reaching behind']}
                numMinutes={getData['drive time']}
            />
            <StatisticBar
                statisticLabel="# of times you were distracted by your passengers"
                userOccurrences={getData['talking to passenger']}
                numMinutes={getData['drive time']}
            />
        </div>
      )}
    </div>
  );
}

export default AllTimeStatsPage;
