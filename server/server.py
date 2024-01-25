from flask import Flask, jsonify, request
from flask_cors import CORS
from stockFinder import StockFinder
import pandas as pd 

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

    # Perform the search using your Python code
    # Replace this with your actual Python code to fetch data
    # Example: result = your_python_function(search_criteria, search_value)

    # result_json = result.to_json(orient='records')
    if isinstance(result, pd.DataFrame):
        result_json = result.to_json(orient='records')
    else:
        result_json = result

    return jsonify({'result': result_json})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
