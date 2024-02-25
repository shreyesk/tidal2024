import React, { useEffect, useState } from 'react';

import { fetchGet, fetchPost } from '../../util/fetchHelp.js';

import './AllTimeStatsPage.css';

function AllTimeStatsPage() {
  const [getData, setGetData] = useState()

  useEffect(() =>{
    fetchGet("/get-all-time-drive-stats").then(data => {
      setGetData(data.message);
    });
  })

  return (
    <div className="App">
      {(typeof getData === "undefined") ? (
        <p>Loading...</p>
      ): (
        <>
          <p>Data received from our get request:</p>
          <p>{getData}</p>
        </>
      )}
    </div>
  );
}

export default AllTimeStatsPage;
