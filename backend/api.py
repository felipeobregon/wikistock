from flask import Flask, jsonify, request
from data import get_data
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

PAGE_SIZE = 10
FILENAME = '../data/nasdaq.json'

@app.route('/data')
def paginate():
    page = int(request.args.get('page', 1))

    # Example array of data to paginate
    data = get_data(FILENAME)


    # Calculate start and end indexes based on page and page size
    start_index = (page - 1) * PAGE_SIZE
    end_index = start_index + PAGE_SIZE

    # Slice the data array based on start and end indexes
    sliced_data = data[start_index:end_index]

    # Return the sliced data as JSON
    return jsonify({'data': sliced_data})

if __name__ == '__main__':
    app.run(debug=True)
