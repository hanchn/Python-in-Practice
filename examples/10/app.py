#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
10. API接口开发
'''

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
