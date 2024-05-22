"""
module errors
"""


def error_name_validation():
    """ regex name validation """
    return 'Invalid contact_name was passed'


def error_phone_validation():
    """ regex phone validation """
    return 'Invalid phone_number was passed'


def error_name_doesnt_exists(name):
    """ contact_name doesnt exists """
    return f'The ({name}) doesnt exists, use command - "add" for changing contact data'


def error_name_exists(name):
    """ contact_name already exists """
    return f'The ({name}) already exists, use command - "change" for changing contact data'