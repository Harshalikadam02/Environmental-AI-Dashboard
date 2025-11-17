from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson import json_util
import json

app = Flask(__name__)
CORS(app)


MONGO_CONNECTION_STRING = 'YOUR_MONGO_CONNECTION_STRING_GOES_HERE'

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        
        client = MongoClient(MONGO_CONNECTION_STRING)
        db = client['myDatabase']
        collection = db['air_quality_traffic']
        
      
        documents = list(collection.find({}, {'_id': 0}))
        
        json_data = json.loads(json_util.dumps(documents))
        
        return jsonify(json_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        # Close the connection
        if 'client' in locals():
            client.close()

if __name__ == '__main__':
    app.run(port=5001, debug=True)

