from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS for enabling cross-origin requests
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Load the sample data from the JSON file
with open('jsondata.json', 'r', encoding='utf-8') as file:
    sample_data = json.load(file)

# Implement a route to provide filter options
@app.route('/api/data', methods=['GET'])
def get_filter_options():
    filter_options = {
        "end_year": list(set(item.get("end_year") for item in sample_data if item.get("end_year"))),
        "topic": list(set(item['topic'] for item in sample_data if 'topic' in item)),
        "sector": list(set(item.get("sector") for item in sample_data if item.get("sector"))),
        "relevance": list(set(item.get("relevance") for item in sample_data if item.get("relevance"))),
        "country": list(set(item.get("country") for item in sample_data if item.get("country"))),
        "region": list(set(item.get("region") for item in sample_data if item.get("region"))),
        "pestle": list(set(item.get("pestle") for item in sample_data if item.get("pestle"))),
        "source": list(set(item.get("source") for item in sample_data if item.get("source"))),
    }

    print("Filter Options:", filter_options)

    return jsonify({"filter_options": filter_options})

# Implement a route to provide filtered data
@app.route('/api/data/filter', methods=['GET'])
def get_filtered_data():
    end_year = request.args.get('end_year')
    topic = request.args.get('topic')
    sector = request.args.get('sector')
    relevance = request.args.get('relevance')
    country = request.args.get('country')
    region = request.args.get('region')
    pestle = request.args.get('pestle')
    source = request.args.get('source')

    # Filter data based on selected filters
    filtered_data = sample_data

    if end_year:
        filtered_data = [item for item in filtered_data if item['end_year'] == end_year]

    if topic:
        filtered_data = [item for item in filtered_data if "topic" in item and topic in item['topic']]

    if sector:
        filtered_data = [item for item in filtered_data if item['sector'] == sector]

    if relevance:
        filtered_data = [item for item in filtered_data if item['relevance'] == relevance]

    if country:
        filtered_data = [item for item in filtered_data if item['country'] == country]

    if region:
        filtered_data = [item for item in filtered_data if item['region'] == region]

    if pestle:
        filtered_data = [item for item in filtered_data if item['pestle'] == pestle]

    if source:
        filtered_data = [item for item in filtered_data if item['source'] == source]


    return jsonify({"data": filtered_data})

if __name__ == '__main__':
    app.run(debug=True)
