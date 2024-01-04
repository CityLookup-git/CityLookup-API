from flask import Flask, jsonify, request
from flask_cors import CORS
from data_loader import DataLoader

app = Flask(__name__)
CORS(app)

# Load datasets from specified folder when the app starts
data_loader = DataLoader('datasets')

@app.route('/get_street_names', methods=['GET'])
def get_street_names():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    streets = data_loader.get_streets_by_city(city)
    if streets:
        return jsonify({'streets': streets})
    else:
        return jsonify({'error': 'No data found for the specified city'}), 404

if __name__ == '__main__':
    app.run(debug=False)
