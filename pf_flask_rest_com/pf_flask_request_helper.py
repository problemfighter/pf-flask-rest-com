from flask import request
from werkzeug.datastructures import ImmutableMultiDict


class RequestHelper:

    def immutable_multi_dict_to_dict(self, _input: ImmutableMultiDict, default=None):
        if not _input:
            return default
        requested_data = _input.to_dict(flat=False)
        response = {}
        for data in requested_data:
            if len(requested_data[data]) == 1:
                response[data] = requested_data[data][0]
            else:
                response[data] = requested_data[data]
        return response

    def json_data(self, default=None):
        json = request.get_json()
        if json:
            return json
        return default

    def form_data(self, default=None):
        data = request.form
        if data:
            return self.immutable_multi_dict_to_dict(data, default)
        return default

    def form_and_file_data(self, default=None):
        form_data = self.form_data(default={})
        file_data = self.file_data(default={})
        form_data.update(file_data)
        if form_data:
            return form_data
        return default

    def file_data(self, default=None):
        files = request.files
        if files:
            return self.immutable_multi_dict_to_dict(files, default)
        return default

    def query_data(self, default=None):
        data = request.args
        if data:
            return data
        return default

    def get_query_params_value(self, key: str, default=None, type=None):
        data = self.query_data(default=None)
        if not data:
            return default
        if key in data:
            value = data.getlist(key, type)
            if len(value) == 1:
                return value[0]
            return value
        return default

    def get_method(self):
        return request.method

    def is_post(self):
        return 'POST' == self.get_method()

    def is_get(self):
        return 'GET' == self.get_method()

    def get_current_url(self):
        return request.referrer


request_helper = RequestHelper()
