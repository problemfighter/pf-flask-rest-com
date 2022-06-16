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
    is_string_name: bool = False
    save_prefix: str = None

    default_error_messages = {
        "invalid": "Not a valid file."
    }

    def set_max_size_kb(self, size: int) -> "FileField":
        self.max_size_kb = size
        return self

    def set_allowed_extension(self, extension: list) -> "FileField":
        self.allowed_extensions = extension
        return self

    def allow_multiple(self) -> "FileField":
        self.is_multiple = True
        return self

    def allow_string_name(self) -> "FileField":
        self.is_string_name = True
        return self

    def set_save_prefix(self, prefix: str) -> "FileField":
        self.save_prefix = prefix
        return self

    def _deserialize(self, value, attr, data, **kwargs) -> typing.Any:
        if self.is_multiple and isinstance(value, list):
            for file in value:
                if not isinstance(file, FileStorage) and not self.is_string_name:
                    raise self.make_error("invalid")
            return value

        if not isinstance(value, FileStorage) and not self.is_string_name:
            raise self.make_error("invalid")
        return value
