"""
The error messages of the database
"""


def type_not_found():
    """
    Returns the type not found error string
    :return: the error message
    """
    return "ERROR: NO SUCH TYPE OF ALGORITHM IN THE DATABASE."


def specific_not_found():
    """
    Returns the specific not found error string
    :return: the error message
    """
    return "ERROR: NO SUCH SPECIFIC ALGORITHM IN THE DATABASE."


def language_not_found(lang):
    """
    Returns the language not found error string
    :return: the error message
    """
    lang = lang.upper()
    return "ERROR: NO "+lang+" VERSION OF THIS ALGORITHM IN THE DATABASE."
