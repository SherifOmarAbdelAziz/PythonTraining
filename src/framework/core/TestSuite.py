
from framework.core.TestCase import TestCase, LoginTest, PaymentTest
from framework.logging.Logger import Logger
from framework.core.Browser import Browser
import framework.core.CustomExceptions as CustomExceptions
from pathlib import Path
from datetime import datetime

class TestSuite:
    def __init__(self, logger):
        self.tests = []
        self.logger = logger
    
    def add_test(self, test):

        if not isinstance(test, TestCase):
            raise TypeError("test must be of type TestCase")
        
        self.tests.append(test)

    def remove_test(self, test):
        self.tests.remove(test)

    def __len__(self):
        return len(self.tests)
    
    def __str__(self):
        return f"TestSuite: Number of tests = {len(self)}"
    
    def __iter__(self):
        return iter(self.tests)
    
    def run_all(self):
        
        for test in self:
            self.logger.info(test)
            
            try:
                test.setup()
                test.run()
                test.teardown()
                yield {"Test Case": test,
                        "Status": "Passed"}
            except Exception as e:
                logger.error(e)
                yield {"Test Case": test,
                        "Status": "Failed"}
                raise

            self.logger.info("--------------")


if __name__ == "__main__":
    file_path = Path("test.log")
    logger = Logger(file_path)

    file_path = Path(file_path)
    if file_path.exists():
        print("File already exists")
    else:
        # file_path.write_text(f"{datetime.now()} [INFO] File created successfully.")
        file_path.touch(exist_ok=True)
        logger.info(f"{datetime.now()} [INFO] File created successfully.")
    
    suite = TestSuite(logger)

    # try:
    browser = Browser("Chrome", logger)
    browser.browser_name = "Firefox"
    suite.add_test(LoginTest(browser, logger))
    suite.add_test(PaymentTest(browser, logger))
    logger.info("--------------")
    logger.info(suite)
    suite.run_all()
    logger.info("--------------")
    
    for result in suite.run_all():
        logger.info(result)
    # except CustomExceptions as e:
    #     logger.error(e)

    # finally:
    #     browser.close()
    #     logger.info(f"Tests Completed.")

    