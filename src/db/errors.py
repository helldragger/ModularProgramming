"""
The error messages of the database
"""


class DataBaseException(Exception):
    """
    A subclass of the base exception to regroup every specific exception of this database
    """

    def __init__(self):
        super().__init__()
        self.reason = ""


class UnsupportedLanguageException(DataBaseException):
    """
    The unsupported language error
    """

    def __init__(self, language):
        super().__init__()
        self.reason = " ".join(["ERROR:", str(language).upper(), "IS CURRENTLY NOT SUPPORTED."])


class LanguageNotFoundException(DataBaseException):
    """
    The language version not found error
    """

    def __init__(self, language):
        super().__init__()
        self.reason = " ".join(["ERROR: NO", str(language).upper(), "VERSION OF THIS ALGORITHM IN THE DATABASE."])


class TypeNotFoundException(DataBaseException):
    """
    The type not found error
    """

    def __init__(self, type):
        super().__init__()
        self.reason = " ".join(["ERROR: THERE IS NO ", str(type).upper(), "TYPE IN THE DATABASE."])


class CircularDependenciesException(DataBaseException):
    """
    The circular dependencies error
    """

    def __init__(self, node_path, child_path):
        super().__init__()
        self.reason = " ".join(["ERROR: CIRCULAR DEPENDENCIES,", node_path, "HAS ATTEMPTED TO IMPORT", child_path, "."])


class DependenceNotFoundException(DataBaseException):
    """
    The circular dependencies error
    """

    def __init__(self, child_path):
        super().__init__()
        self.reason = " ".join(["ERROR: DEPENDENCE", child_path, "NOT FOUND."])
