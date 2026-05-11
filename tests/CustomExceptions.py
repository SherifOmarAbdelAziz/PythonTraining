

class CustomExceptions(Exception):
    def __init__(self, message):
        self.message = message

class BrowserClosedError(CustomExceptions):
    pass

class InvalidUrlError(CustomExceptions):
    pass

class InvalidBrowserNameError(CustomExceptions):
    pass