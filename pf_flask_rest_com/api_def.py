from marshmallow import Schema, fields


class APIDef(Schema):
    class Meta:
        ordered = True


class FileField(fields.String):
    max_size_kb: int = None
    allowed_extensions: list = None

    def set_max_size_kb(self, size: int):
        self.max_size_kb = size
        return self

    def set_allowed_extension(self, extension: list):
        self.allowed_extensions = extension
        return self
