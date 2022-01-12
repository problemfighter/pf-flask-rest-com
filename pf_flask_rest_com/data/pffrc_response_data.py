from pf_flask_rest_com.api_def import APIDef
from pf_flask_rest_com.schema.pffrc_response_schema import PFFRCMessageAPIResponse, PFFRCErrorAPIResponse, \
    PFFRCDataAPIResponse, PFFRCPaginateAPIResponse


class PFFRCBaseResponse:
    status: str = None
    code: str = None
    httpCode: int = None

    def make_dict(self, data, api_def: APIDef, many=False):
        return api_def.dumps(data, many=many)


class PFFRCMessageResponse(PFFRCBaseResponse):
    message: str = None

    def to_dict(self):
        return self.make_dict(self, PFFRCMessageAPIResponse())


class PFFRCErrorResponse(PFFRCMessageResponse):
    error: dict = None

    def to_dict(self):
        return self.make_dict(self, PFFRCErrorAPIResponse())


class PFFRCDataResponse(PFFRCBaseResponse):
    data = None

    def to_dict(self):
        return self.make_dict(self, PFFRCDataAPIResponse())


class PFFRCPagination(object):
    page: int = None
    itemPerPage: int = None
    total: int = None
    totalPage: int = None


class PFFRCPaginateResponse(PFFRCDataResponse):
    pagination: PFFRCPagination = None

    def to_dict(self):
        return self.make_dict(self, PFFRCPaginateAPIResponse())