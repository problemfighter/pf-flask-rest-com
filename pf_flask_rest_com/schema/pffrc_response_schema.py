from marshmallow import fields
from pf_flask_rest_com.api_def import APIDef


class PFFRCBaseAPIResponse(APIDef):
    status = fields.String()
    code = fields.String()


class PFFRCMessageAPIResponse(PFFRCBaseAPIResponse):
    message = fields.String()


class PFFRCErrorAPIResponse(PFFRCMessageAPIResponse):
    error = fields.Dict(keys=fields.String(), values=fields.String())


class PFFRCDataAPIResponse(PFFRCBaseAPIResponse):
    data = fields.Dict(keys=fields.String(), values=fields.String())


class Pagination(APIDef):
    page = fields.Integer()
    itemPerPage = fields.Integer()
    total = fields.Integer()
    totalPage = fields.Integer()


class PFFRCPaginateAPIResponse(PFFRCDataAPIResponse):
    pagination = fields.Nested(Pagination)
