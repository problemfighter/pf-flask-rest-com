import typing

from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage


class APIDef(Schema):
    class Meta:
        ordered = True


class FileField(fields.String):
    max_size_kb: int = None
    allowed_extensions: list = None

    default_error_messages = {
        "invalid": "Not a valid file."
    }

    def set_max_size_kb(self, size: int):
        self.max_size_kb = size
        return self

    def set_allowed_extension(self, extension: list):
        self.allowed_extensions = extension
        return self

    def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
        if not isinstance(value, FileStorage):
            raise self.make_error("invalid")
        return value
