from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/get-most-recent-drive-stats')
def getMostRecentDriveStats():
    csv_file_path = './data.csv'
    df = pd.read_csv(csv_file_path)
    last_row = df.iloc[-1]

    csv_column_names = ['drive time', 'texting', 'talking on phone', 'operating the radio', 'drinking', 'reaching behind', 'talking to passenger']
    mostRecentDriveStats = {'drive time': 0, 'texting': 0, 'talking on phone': 0, 'operating the radio': 0, 'drinking': 0, 'reaching behind': 0, 'talking to passenger': 0}
    for columnName in csv_column_names:
        mostRecentDriveStats[columnName] = last_row[columnName]

    for columnName in csv_column_names:
        mostRecentDriveStats[columnName] = str(mostRecentDriveStats[columnName])
    return jsonify(mostRecentDriveStats)

@app.route('/get-all-time-drive-stats')
def getAllTimeDriveStats():
    csv_file_path = './data.csv'
    df = pd.read_csv(csv_file_path)
    csv_column_names = ['drive time', 'texting', 'talking on phone', 'operating the radio', 'drinking', 'reaching behind', 'talking to passenger']
    allTimeDriveStats = {'drive time': 0, 'texting': 0, 'talking on phone': 0, 'operating the radio': 0, 'drinking': 0, 'reaching behind': 0, 'talking to passenger': 0}
    for columnName in csv_column_names:
        allTimeDriveStats[columnName] = df[columnName].sum()

    for columnName in csv_column_names:
        allTimeDriveStats[columnName] = str(allTimeDriveStats[columnName])
    return jsonify(allTimeDriveStats)

if __name__ == '__main__':
    app.run(debug=True, port=3001)