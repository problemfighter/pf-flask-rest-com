import os
from flask import Flask
from pf_flask_rest_com.pf_flask_response_helper import response_helper

app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Flask Response Test......"


@app.route('/json-response')
def json_response():
    data = {'age': 7, 'name': 'hmtmcse.com', 'data': ['a', 'b', 'c']}
    return response_helper.json_response(data)


@app.route('/json-string-response')
def json_string_response():
    data = '{"age": 7, "name": "hmtmcse.com", "data": ["a", "b", "c"]}'
    return response_helper.json_string_response(data)


@app.route('/file-response')
def file_response():
    file = os.path.join(app.root_path, 'note.adoc')
    return response_helper.file_response(file, download_name="readme.adoc")


if __name__ == '__main__':
    app.run(debug=True)
