from pprint import pprint
from marshmallow import Schema, fields, validate, ValidationError

'''
    err.valid_data -> returns valid data passed
    err.messages -> returns invalid data passed

    schema()
        valid_data -> dict of valid data (empty dict if none is valid)
        messages -> dict of invalid data (cannot be empty. will not raise error if all are valid lol)

    schema(many=True)
        valid_data -> list of dict (empty dict if none is valid)
        messages -> { index of dict : { 'field':'error msg' }, ... }

'''

def validate_test(s):
    if s[3] != '3':
        raise ValidationError("Fourth character is not '3'.")

LoginSchema = Schema.from_dict(
    {
        "username" : fields.Str(required=True, validate=validate.Length(max=11)),
        "password" : fields.Str(validate=validate.And(validate.OneOf(["test","wtf3"]),validate_test))
    }
)

data1 = {
        "password" : "20171111152",
    }
    
data2 = {
        "username" : "20171111152",
        "password" : "hey3"
    
    }
data3 = {
        "username" : "hey",
        "password" : "test4"
    }

data4 = {
        "username" : "hey",
        "password" : "wtf3"
    }


try:
    LoginSchema().load(data1)
except ValidationError as err:
    print("data1")
    pprint(err.valid_data)
    pprint(err.messages)

try:
    LoginSchema().load(data2)
except ValidationError as err:
    print("data2")
    pprint(err.valid_data)
    pprint(err.messages)

try:
    LoginSchema().load(data3)
except ValidationError as err:
    print("data3")
    pprint(err.valid_data)
    pprint(err.messages)

try:
    LoginSchema().load(data4)
except ValidationError as err:
    print("data4")
    pprint(err.valid_data)
    pprint(err.messages)

# 'args',
#  'data',
#  'field_name',
#  'kwargs',
#  'messages',
#  'normalized_messages',
#  'valid_data',
#  'with_traceback']