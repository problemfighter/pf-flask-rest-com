import json
from flask import make_response, send_file
import typing as t
from pf_flask_rest_com.common.pf_flask_rest_com_const import RestComConst


class ResponseHelper:

    def response(self, response_data, code=200, headers: dict = None):
        response_obj = make_response(response_data, code)
        if headers:
            response_obj.headers.update(headers)
        return response_obj

    def json_string_response(self, json_string: str, code=200, headers: dict = None):
        _headers = {
            RestComConst.CONTENT_TYPE: RestComConst.APPLICATION_JSON
        }
        if headers and isinstance(headers, dict):
            _headers.update(headers)
        return self.response(json_string, code=code, headers=_headers)

    def json_response(self, obj, code=200, headers: dict = None):
        json_object = {}
        if obj:
            json_object = obj
        response_string = "{}"
        try:
            response_string = json.dumps(json_object)
        except Exception as e:
            response_string = "{}"
        return self.json_string_response(response_string, code, headers)

    def file_response(self, file_path, download_name: t.Optional[str] = None):
        return send_file(file_path, download_name=download_name)

    def text_response(self, text: str, code=200, headers: dict = None):
        return self.response(text, code=code, headers=headers)


response_helper = ResponseHelper()
