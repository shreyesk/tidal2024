from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/get-most-recent-drive-stats')
def getMostRecentDriveStats():
    csv_file_path = './data.csv'
    df = pd.read_csv(csv_file_path)
    last_row = df.iloc[-1]

    csv_column_names = ['drive time', 'texting', 'talking on phone', 'operating the radio', 'drinking', 'reaching behind', 'talking to passenger']
    mostRecentDriveStats = []
    for columnName in csv_column_names:
        mostRecentDriveStats.append(last_row[columnName])
        print(f'mostRecentDriveStats is now: {mostRecentDriveStats}')
    return jsonify({"message": mostRecentDriveStats})

@app.route('/get-all-time-drive-stats')
def getAllTimeDriveStats():
    csv_file_path = './data.csv'
    df = pd.read_csv(csv_file_path)
    csv_column_names = ['drive time', 'texting', 'talking on phone', 'operating the radio', 'drinking', 'reaching behind', 'talking to passenger']
    allTimeDriveStats = {}
    for columnName in csv_column_names:
        allTimeDriveStats[columnName] = df[columnName].sum()

    return jsonify(allTimeDriveStats)

if __name__ == '__main__':
    app.run(debug=True, port=3001)