

from abc import ABC, abstractmethod
from framework.core.Browser import Browser
from framework.logging.Logger import Logger
from framework.core.CustomExceptions import InvalidUrlError
from datetime import datetime
from functools import wraps

class TestCase(ABC):

    # class variable
    tests_count = 0

    @classmethod
    def increment_tests_count(cls):
        cls.tests_count += 1

    def __init__(self, testname, logger):
        self.testname = testname
        self.logger = logger

    def setup(self):
        self.logger.info("Setup")
        # print("Setup")

    @abstractmethod
    def run(self):
        pass

    def __str__(self):
        return f"Test: {self.testname}"

    def teardown(self):
        self.logger.info("Teardown")
        # print("Teardown")


class LoginTest(TestCase):
    
    def __init__(self, browser, logger):
        self.browser = browser
        super().__init__("Login", logger) 

    @staticmethod
    def measure_time(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            start = datetime.now()
            result = func(*args, **kwargs)
            stop = datetime.now()
            # print(f"{func.__name__} took {stop - start:.2f} seconds to run.")
            args[0].logger.info(f"{__class__.__name__}.{func.__name__}"
                                f" took {((stop - start).total_seconds())*1e6:.4f} microseconds")
            return result
        
        return wrapper

    @staticmethod
    def execution_logging(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            args[0].logger.info(f"Running {__class__.__name__} test case. ")
            result = func(*args, **kwargs)
            args[0].logger.info(f"Completed execution of {__class__.__name__} test case. ")
            return result
        return wrapper

    @staticmethod
    def retry(max_retries):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):           
                for numberOfRetries in range(max_retries):
                    args[0].logger.info(f"Starting Execution#{numberOfRetries+1} of {__class__.__name__} test case. ")
                    result = func(*args, **kwargs)
                    args[0].logger.info(f"Completed Execution#{numberOfRetries+1} of {__class__.__name__} test case. ")
                return result
            return wrapper
        return decorator

    @retry(2)
    @measure_time
    @execution_logging
    def run(self):
        # print("Running login test")
        # self.logger.info("Running login test")
        try:
            self.browser.open()
            self.browser.navigate("https://google.com")
            self.browser.close()

            TestCase.increment_tests_count()
        except InvalidUrlError as e:
            self.logger.error(str(e))
        finally:
            self.browser.close()

class PaymentTest(TestCase):

    def __init__(self, browser, logger):
        self.browser = browser
        super().__init__("Payment", logger) 

    def run(self):
        # print("Running payment test") 
        self.logger.info("Running payment test") 
        TestCase.increment_tests_count()      


if __name__ == "__main__":

    myBrowser = Browser.Browser("Chrome")
    logger = Logger()
    myBrowser.browser_name = "Firefox"
    tests = [LoginTest(myBrowser),
            PaymentTest(myBrowser)
            ]
    

    for test in tests:
        # print(test)
        logger.info(test)
        test.setup()
        test.run()
        test.teardown()
        logger.info("--------------")

    # print(f"Tests count: {TestCase.tests_count}")
    logger.info(f"Tests count: {TestCase.tests_count}")