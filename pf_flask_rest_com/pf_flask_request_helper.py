from flask import request


class RequestHelper:

    def json_data(self, default=None):
        json = request.get_json()
        if json:
            return json
        return default

    def form_data(self, default=None):
        data = request.form
        if data:
            return data
        return default

    def file_data(self, default=None):
        files = request.files
        if files:
            return files
        return default

    def query_data(self, default=None):
        data = request.args
        if data:
            return data
        return default
