import Tab from "@mui/material/Tab";
import Tabs from "@mui/material/Tabs";
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const NavigationBar = () => {
  const navigate = useNavigate();
  const buttons = { "Most Recent Drive": "/most-recent-drive", "Your All-Time Stats": "/all-time-stats" };

  const [value, setValue] = useState(0);

  const handleButtonClick = (index) => {
    setValue(index);
    navigate(Object.values(buttons)[index]);
  };

  return (
    <div>
      <Tabs value={value} onChange={(e, newValue) => setValue(newValue)} centered>
        {Object.keys(buttons).map((button, index) => (
          <Tab
            key={index}
            label={button}
            onClick={() => handleButtonClick(index)}
          />
        ))}
      </Tabs>
    </div>
  );
};

export default NavigationBar;
