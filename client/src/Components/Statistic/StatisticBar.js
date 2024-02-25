import "./StatisticBar.css";

const StatisticBar = ({ statisticLabel, userOccurrences, medianValue }) => {
  const comparisonText = Number(userOccurrences) > Number(medianValue) ? 'more' : 'less';
  const comparisonColor = Number(userOccurrences) > Number(medianValue) ? 'red' : 'green';

  const leftSideStyle = {
    fontWeight: 'bold',
    color: 'black',
    flex: 1, // This will ensure the items take equal space
    textAlign: 'left', // Align text to the left
    fontSize: '40px',
  };

  const centerStyle = {
    flex: 1,
    textAlign: 'center', // Align text to the center
  };

  const rightSideStyle = {
    color: comparisonColor,
    fontWeight: 'normal',
    flex: 1,
    textAlign: 'right', // Align text to the right
  };

  return (
    <div className="containerStyle">
      <span style={leftSideStyle}>{userOccurrences}</span>

      <span style={centerStyle}>{statisticLabel}</span>

      <span style={rightSideStyle}>
        {`${Math.abs(userOccurrences - medianValue)} times ${comparisonText} than the median`}
      </span>
    </div>
  );
};

export default StatisticBar;
