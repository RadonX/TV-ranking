#!/usr/bin/env python
from flask import Flask, render_template, Response #request, jsonify
from flask import url_for
import sys
import requests
import json

import logging
#logging.basicConfig(filename='flask.log', level=logging.DEBUG)
# logging.info('...')
# logging.error('...')
# logging.debug('...')


application = Flask(__name__, static_url_path='/static')

@application.route('/ranking')
def ranking():
    r = requests.get('http://localhost:5001/static/get_ranked.json')
    # start another flask server (in `/data-flask`) to host the json
    # since in the final demo, I need to request data from another domain (provided by John)
    json_response = r.json()
    return render_template('ranking.html', TV_list = json_response)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/tv')
def tv():
    return render_template('tv.html')

@application.route('/search')
def search():
    return render_template('search.html')

@application.route('/get_ranked')
def getDetails():
    r = requests.get('http://localhost:5001/static/get_ranked.json')
    json_response = json.dumps(r.json())
    response = Response(json_response, content_type='application/json; charset=utf-8')
    response.headers.add('content-length',len(json_response))
    response.status_code=200
    return response

'''
@application.route('/json', methods=['GET'])
def json():
    # keyword = request.args.get('keyword')
    return jsonify(result)

@application.route('/send')
def send():
    return "<a href=%s>file</a>" % url_for('static', filename='get_ranked.json')
'''


if __name__ == "__main__":
    application.run(debug=True) # for dev
    #application.run(host='0.0.0.0', port=5000) # for prod
