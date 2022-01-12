from pf_flask_rest_com.data.pffr_response_data import PFFRMessageResponse
from pf_py_common.pf_exception import PFException


class PFFRException(PFException):
    messageResponse: PFFRMessageResponse
    errorResponse: PFFRMessageResponse

    def __init__(self, message=None, exception_type: str = None):
        super().__init__(message, exception_type)
