from marshmallow import fields
from pf_flask_rest_com.api_def import APIDef


class PFFRCBaseAPIResponse(APIDef):
    class Meta:
        ordered = True

    status = fields.String()
    code = fields.String()


class PFFRCMessageAPIResponse(PFFRCBaseAPIResponse):
    message = fields.String()


class PFFRCErrorAPIResponse(PFFRCMessageAPIResponse):
    error = fields.Dict(keys=fields.String(), values=fields.String())


class PFFRCDataAPIResponse(PFFRCBaseAPIResponse):
    message = fields.String()
    data = fields.Dict()


class PFFRCDataListAPIResponse(PFFRCBaseAPIResponse):
    data = fields.List(fields.Dict)


class Pagination(APIDef):
    page = fields.Integer()
    itemPerPage = fields.Integer()
    total = fields.Integer()
    totalPage = fields.Integer()


class PFFRCPaginateAPIResponse(PFFRCDataListAPIResponse):
    pagination = fields.Nested(Pagination())

