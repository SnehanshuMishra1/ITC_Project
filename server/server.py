from flask import Flask, jsonify, request
from flask_cors import CORS
from stockFinder import StockFinder, APIResponseFetcher
import pandas as pd 
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/search-stocks', methods=['POST'])
def search_stocks():
    data = request.get_json()
    search_criteria = data.get('searchCriteria')
    search_value = data.get('searchValue')

    # Assuming you have a method 'search_stocks' in your StockFinder class
    searcher = StockFinder()
    
    if search_criteria == 'ticker':
        result = searcher.by_symbol(search_value)
    elif search_criteria == 'name':
        result = searcher.by_name(search_value)
    elif search_criteria == 'industry':
        result = searcher.by_industry(search_value)
    else:
        result = None

    result_json = result.to_json(orient='records')
    if isinstance(result, pd.DataFrame):
        result_json = result.to_json(orient='records')
    else:
        result_json = result
        
    return result_json

@app.route('/api/industry-list', methods=['GET'])
def find_industries():
    searcher = StockFinder()
    result = searcher.fetch_all_industries()

    if isinstance(result, pd.DataFrame):
        result_json = result.to_json(orient='records')
    else:
        result_json = result
        
    return result_json

@app.route('/api/sentiment-score', methods=['POST'])
def find_sentiment_score():
    data = request.get_json()
    ticker = data.get('ticker')

    # Assuming you have a method 'search_stocks' in your StockFinder class
    searcher = StockFinder()
    result = searcher.by_symbol(ticker)

    result_json = result.to_json(orient='records')
    if isinstance(result, pd.DataFrame):
        result_json = result.to_json(orient='records')
    else:
        result_json = result

    return result_json
        

@app.route('/api/api-topic-wise', methods=['POST'])
def topic_wise_news():
    topic = request.get_json().get('topic')
    api = APIResponseFetcher()
    result_dict = api.by_topic(topic)

    result_json = json.dumps(result_dict)
    return result_json

if __name__ == '__main__':
    app.run(debug=True, port=5000)
