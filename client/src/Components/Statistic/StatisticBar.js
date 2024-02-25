import "./StatisticBar.css";

const StatisticBar = ({ statisticLabel, userOccurrences, numMinutes }) => {

  const leftSideStyle = {
    fontWeight: 'bold',
    color: 'black',
    flex: 1,
    textAlign: 'left',
    fontSize: '40px',
  };

  const centerStyle = {
    flex: 1,
    textAlign: 'center',
  };

  const rightSideStyle = {
    color: 'black',
    fontWeight: 'normal',
    flex: 1,
    textAlign: 'right',
  };

  return (
    <div className="containerStyle">
      <span style={leftSideStyle}>{userOccurrences}</span>

      <span style={centerStyle}>{statisticLabel}</span>

      <span style={rightSideStyle}>
        {`${Math.abs(userOccurrences / numMinutes).toFixed(2)} times per minute`}
      </span>
    </div>
  );
};

export default StatisticBar;
