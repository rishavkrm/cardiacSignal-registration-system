from flask import Flask, request, jsonify
from functions.preprocess import remove_nonNumeric_lines
from functions.process import find_Spectral_Values
from functions.model import checkType
from flask_cors import CORS
import csv
import os
app = Flask(__name__)
CORS(app)
@app.route('/api/v1/classifier', methods=['POST'])
def classify():
    file = request.files['file']
    # print(type(file))
    if file:
        print("A file has been sent.")
        save_dir = os.path.join(os.path.dirname(__file__), 'csv')
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, file.filename)
        file.save(file_path)
        print(file_path)
        try:
            remove_nonNumeric_lines(file_path)
            spectral_Values = find_Spectral_Values(file_path)
            result = checkType(spectral_Values)
            print(f"The file is {result}")
            return jsonify({'result':result})
        except csv.Error as e:
            return jsonify({'error': 'CSV file error: {}'.format(e)})
        finally:
            # Remove the temporary file
            os.remove(file_path)
    else:
        return jsonify({'error': 'No file received'})

if __name__ == '__main__':
    app.run(port=9000)
