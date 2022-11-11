from pf_flask_rest_com.api_def import APIDef
from pf_flask_rest_com.schema.pffrc_response_schema import PFFRCMessageAPIResponse, PFFRCErrorAPIResponse, \
    PFFRCDataAPIResponse, PFFRCPaginateAPIResponse, PFFRCDataListAPIResponse


class PFFRCBaseResponse:
    status: str = None
    code: str = None
    httpCode: int = None
    message: str = None

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
    _schema = PFFRCDataAPIResponse()
    data = None

    def add_data(self, model, schema: APIDef, many=False):
        if many:
            self._schema = PFFRCDataListAPIResponse()
        else:
            self._schema = PFFRCDataAPIResponse()

        if model and schema:
            self.add_only_data(model, schema, many)

    def add_only_data(self, model, schema: APIDef, many=False):
        if model:
            self.data = schema.dump(model, many=many)

    def to_dict(self):
        return self.make_dict(self, self._schema)


class PFFRCPagination(object):
    page: int = None
    itemPerPage: int = None
    total: int = None
    totalPage: int = None


class PFFRCPaginateResponse(PFFRCDataResponse):
    _schema = PFFRCPaginateAPIResponse()
    pagination: PFFRCPagination = None

    def to_dict(self):
        return self.make_dict(self, self._schema)
