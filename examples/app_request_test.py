from flask import Flask

from pf_flask_rest_com.pf_flask_request_helper import request_helper

app = Flask(__name__)


@app.route('/')
def bismillah():
    return "Flask Request Test......"


@app.route('/query-data')
def query_data():
    params = request_helper.query_data()
    return {
        "name": params['name'],
        "age": params['age'],
    }


@app.route('/get-query-data-value')
def get_query_data_value():
    return {
        "name": request_helper.get_query_params_value('name'),
        "age": request_helper.get_query_params_value('age'),
        "noData": request_helper.get_query_params_value('noData', 'noData'),
    }


@app.route('/query-data-list')
def query_data_list():
    return {
        "name": request_helper.get_query_params_value('name')
    }


@app.route('/json-data')
def json_data():
    return "Flask Request Test......"


@app.route('/form-data')
def form_data():
    return "Flask Request Test......"


@app.route('/file-data')
def file_data():
    return "Flask Request Test......"


# @app.route('/')
# def bismillah():
#     return "Flask Request Test......"
#
#
# @app.route('/')
# def bismillah():
#     return "Flask Request Test......"


if __name__ == '__main__':
    app.run(debug=True)
