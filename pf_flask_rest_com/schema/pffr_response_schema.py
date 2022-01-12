from marshmallow import fields
from pf_flask_rest_com.api_def import APIDef


class PFFRBaseAPIResponse(APIDef):
    status = fields.String()
    code = fields.String()


class PFFRMessageAPIResponse(PFFRBaseAPIResponse):
    message = fields.String()


class PFFRErrorAPIResponse(PFFRMessageAPIResponse):
    error = fields.Dict(keys=fields.String(), values=fields.String())


class PFFRDataAPIResponse(PFFRBaseAPIResponse):
    data = fields.Dict(keys=fields.String(), values=fields.String())


class Pagination(APIDef):
    page = fields.Integer()
    itemPerPage = fields.Integer()
    total = fields.Integer()
    totalPage = fields.Integer()


class PFFRPaginateAPIResponse(PFFRDataAPIResponse):
    pagination = fields.Nested(Pagination)
