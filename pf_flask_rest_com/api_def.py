import typing

from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage


class APIDef(Schema):
    class Meta:
        ordered = True


class FileField(fields.String):
    max_size_kb: int = None
    allowed_extensions: list = None
    is_multiple: bool = False

    default_error_messages = {
        "invalid": "Not a valid file."
    }

    def set_max_size_kb(self, size: int):
        self.max_size_kb = size
        return self

    def set_allowed_extension(self, extension: list):
        self.allowed_extensions = extension
        return self

    def allow_multiple(self):
        self.is_multiple = True
        return self

    def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
        if self.is_multiple:
            for file in value:
                if not isinstance(file, FileStorage):
                    raise self.make_error("invalid")
        elif not isinstance(value, FileStorage):
            raise self.make_error("invalid")
        return value
