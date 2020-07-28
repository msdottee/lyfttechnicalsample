from flask import abort, Flask, request
from lyfttechnicalsample.split_string import split_string
from marshmallow import Schema, fields, ValidationError


class StringSplitRequest(Schema):
    string_to_cut = fields.Str(required=True)


app = Flask(__name__)


@app.route('/test', methods=['POST'])
def string_split():
    try:
        string_split_request = StringSplitRequest().load(request.get_json())

        cut_string = split_string(string_split_request['string_to_cut'])

        return {
            'return_string': cut_string,
        }
    except ValidationError:
        abort(400)


if __name__ == '__main__':
    app.run()
