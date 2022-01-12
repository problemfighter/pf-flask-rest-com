from pf_flask_rest_com.api_def import APIDef
from pf_flask_rest_com.schema.pffr_response_schema import PFFRMessageAPIResponse, PFFRErrorAPIResponse, \
    PFFRDataAPIResponse, PFFRPaginateAPIResponse


class PFFRBaseResponse:
    status: str = None
    code: str = None
    httpCode: int = None

    def make_dict(self, data, api_def: APIDef, many=False):
        return api_def.dumps(data, many=many)


class PFFRMessageResponse(PFFRBaseResponse):
    message: str = None

    def to_dict(self):
        return self.make_dict(self, PFFRMessageAPIResponse())


class PFFRErrorResponse(PFFRMessageResponse):
    error: dict = None

    def to_dict(self):
        return self.make_dict(self, PFFRErrorAPIResponse())


class PFFRDataResponse(PFFRBaseResponse):
    data = None

    def to_dict(self):
        return self.make_dict(self, PFFRDataAPIResponse())


class PFFRPagination(object):
    page: int = None
    itemPerPage: int = None
    total: int = None
    totalPage: int = None


class PFFRPaginateResponse(PFFRDataResponse):
    pagination: PFFRPagination = None

    def to_dict(self):
        return self.make_dict(self, PFFRPaginateAPIResponse())
