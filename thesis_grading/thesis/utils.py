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
        messages -> { index of data : { 'field':'error msg' }, ... }

    if all are valid, it will just return what you fed it 
        and if many=True, will return a list of dict

'''

def validate_test(s):
    if s[3] != '3':
        raise ValidationError("Fourth character is not '3'.")

LoginSchema = Schema.from_dict(
    {
        "csrf_token" : fields.Str(required=True),
        "username" : fields.Str(required=True, validate=validate.Length(max=11)),
        "password" : fields.Str(validate=validate.And(validate.OneOf(["test","wtf3"]),validate_test))
    }
)

# data1 = {
#         "username" : "11111",
#         "password" : "wtf3"
#     }



# try:
#     result = LoginSchema().load(data1)

#     print(result)
# except ValidationError as err:
#     print("data1")
#     pprint(err.valid_data)
#     pprint(err.messages)




# make Class based schema para inherit inherit nalang



# def validate(dict):
#     valid = {}
#     invalid = {}

#     try:
#         result = validate()
#         valid = result
#     except:
#         valid = err.valid_data
#         invalid = err.messages 

#     return valid, invalid


