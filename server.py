from flask import Flask, render_template, jsonify, request
from src.core.monitor import Monitor
from src.core.neural_processor import NeuralProcessor
from src.services.blockchain_scanner import BlockchainScanner
import os

app = Flask(__name__, 
    template_folder='templates',
    static_folder='static'
)

# Initialize core components
monitor = Monitor()
processor = NeuralProcessor()
scanner = BlockchainScanner()

@app.route('/')
def serve_index():
    return render_template('index.html')

@app.route('/main')
def serve_main():
    return render_template('main.html')

@app.route('/monitor')
def serve_monitor():
    return render_template('monitor.html')

@app.route('/whitepaper')
def serve_whitepaper():
    return render_template('whitepaper.html')

# API Routes
@app.route('/api/monitors', methods=['POST'])
def create_monitor():
    params = request.json
    try:
        monitor.configure(params)
        monitor.start()
        return jsonify({
            'success': True,
            'monitorId': 'mon_' + os.urandom(8).hex()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/monitors/<monitor_id>', methods=['DELETE'])
def stop_monitor(monitor_id):
    try:
        monitor.stop()
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

@app.route('/api/analyze', methods=['POST'])
def analyze_contract():
    address = request.json.get('address')
    try:
        analysis = scanner.analyze_contract(address)
        return jsonify({
            'success': True,
            'analysis': analysis
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=8000) 