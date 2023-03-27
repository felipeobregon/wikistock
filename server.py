from flask import Flask, request, jsonify
import threading
import main

app = Flask(__name__)

computation_thread = None

@app.route('/start')
def start_computation():
    global computation_thread
    
    computation_thread = threading.Thread(target=main.runComputation)
    computation_thread.start()
    return jsonify({"status": "Computation started"}), 200


@app.route('/stop')
def stopComputation():
    if main.stopComputation():
        return jsonify({"status": "Computation stopped"}), 200
    else:
        return jsonify({"status": "Computation is not running"}), 400

app.run(host='0.0.0.0', port=5000)
