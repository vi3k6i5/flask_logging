# file app/app.py
from flask import request, jsonify
from __init__ import application
from helper import *

@application.route('/v1/status', methods=['GET'])
def get_status():
    foo_method()
    return jsonify({"data" : "SUCCESSFUL"})

if __name__ == '__main__':
    application.run(debug=True, host='127.0.0.1', port=5000)

