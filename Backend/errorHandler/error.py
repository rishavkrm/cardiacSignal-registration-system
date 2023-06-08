from flask import jsonify
def Error(error_message,statusCode):
    return(jsonify({'error': error_message}), statusCode)