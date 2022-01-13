from marshmallow import Schema, fields


class APIDef(Schema):
    class Meta:
        ordered = True


class FileField(fields.String):
    pass
