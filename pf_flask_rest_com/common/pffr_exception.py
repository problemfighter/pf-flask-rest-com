from pf_flask_rest_com.data.pffrc_response_data import PFFRCMessageResponse
from pf_py_common.pf_exception import PFException


class PFFRCException(PFException):
    messageResponse: PFFRCMessageResponse
    errorResponse: PFFRCMessageResponse

    def __init__(self, message=None, exception_type: str = None):
        super().__init__(message, exception_type)
