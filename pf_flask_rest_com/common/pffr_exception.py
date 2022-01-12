from pf_flask_rest_com.data.pffrc_response_data import PFFRCMessageResponse, PFFRCErrorResponse
from pf_flask_rest_com.data.pffrc_response_status import PFFRCResponseCode, PFFRCHTTPCode
from pf_py_common.pf_exception import PFException


class PFFRCException(PFException):
    messageResponse: PFFRCMessageResponse
    errorResponse: PFFRCErrorResponse

    def __init__(self, message=None, exception_type: str = None):
        super().__init__(message, exception_type)

    def error_message_exception(self, message: str, code=PFFRCResponseCode.error, http_code=PFFRCHTTPCode.OK):
        response = PFFRCMessageResponse()
        response.message = message
        response.code = code
        response.http_code = http_code
        self.messageResponse = response
        return self

    def error_details_exception(self, message: str, details: dict, code=PFFRCResponseCode.error, http_code=PFFRCHTTPCode.OK):
        response = PFFRCErrorResponse()
        response.message = message
        response.code = code
        response.http_code = http_code
        response.error = details
        self.messageResponse = response
        return self


pffrc_exception = PFFRCException()
