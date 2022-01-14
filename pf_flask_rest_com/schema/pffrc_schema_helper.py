from pf_flask_rest_com.api_def import APIDef


class PFFRCSchemaHelper(object):

    def change_schema_field_type(self, schema: APIDef, name, data_type):
        schema.fields[name] = data_type
        schema.dump_fields[name] = data_type
        schema.declared_fields[name] = data_type
        schema.load_fields[name] = data_type
        return schema


pffrc_schema_helper = PFFRCSchemaHelper()
