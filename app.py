from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Define data directory relative to app.py
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app.template_folder = TEMPLATE_DIR
app.static_folder = STATIC_DIR

# Route to serve the main dashboard
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint for marketShare.json
@app.route('/api/marketShare')
def get_market_share():
    try:
        with open(os.path.join(DATA_DIR, 'marketShare.json'), 'r') as f:
            market_share_data = json.load(f)
        return jsonify(market_share_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

# API endpoint for revenueTrends.json
@app.route('/api/revenueTrends')
def get_revenue_trends():
    try:
        with open(os.path.join(DATA_DIR, 'revenueTrends.json'), 'r') as f:
            revenue_trends_data = json.load(f)
        return jsonify(revenue_trends_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

# API endpoint for marketSegmentation.json
@app.route('/api/marketSegmentation')
def get_market_segmentation():
    try:
        with open(os.path.join(DATA_DIR, 'marketSegmentation.json'), 'r') as f:
            market_segmentation_data = json.load(f)
        return jsonify(market_segmentation_data)
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500

if __name__ == '__main__':
    app.run(debug=True)
