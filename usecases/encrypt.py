import base64


def password_encode(password_string):
    encoded_password = base64.b64encode(bytes(password_string, "UTF-8"))
    return str(encoded_password)


def password_decode(password_string):
    decoded_password = base64.b16decode(password_string)
    return str(decoded_password)
