from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/get-most-recent-drive-stats')
def getMostRecentDriveStats():
    csv_file_path = './data.csv'  # Adjust the path to where your data.csv is located
    df = pd.read_csv(csv_file_path)
    last_row = df.iloc[-1]

    csv_column_names = ['normal driving', 'texting', 'talking on phone', 'operating the radio', 'drinking', 'reaching behind', 'hair and makeup', 'talking to passenger']
    mostRecentDriveStats = []
    for columnName in csv_column_names:
        mostRecentDriveStats.append(last_row[columnName])
        print(f'mostRecentDriveStats is now: {mostRecentDriveStats}')
    return jsonify({"message": mostRecentDriveStats})

@app.route('/get-all-time-drive-stats')
def getAllTimeDriveStats():
    return jsonify({"message": "this works!"})

# # example get request
# @app.route('/default_greet')
# def hello():
#     return jsonify({"message": "Hello, World!"})

# # example of sending a post request with data as a json
# @app.route('/greet', methods=['POST'])
# def greet():
#     data = request.get_json()

#     if 'name' in data:
#         return jsonify({'message': f'Hello, {data["name"]}!'})
#     else:
#         return jsonify({'error': 'Missing "name" parameter'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=3001)