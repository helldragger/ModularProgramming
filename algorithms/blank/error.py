class BlankError(Exception):
    """
    A template of a new exception to throw
    """

    def __init__(self):
        super().__init__()
        self.reason = "Replace this with a real error text to display"
