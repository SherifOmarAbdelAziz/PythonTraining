from framework import (
    Runner, 
    Browser, 
    Logger, 
    TestSuite, 
    TestCase, 
    LoginTest,
    PaymentTest,
    CustomExceptions
)
from datetime import datetime
from pathlib import Path


file_path = Path("test_1.log")
logger = Logger(file_path)

file_path = Path(file_path)
if file_path.exists():
    print("File already exists")
else:
    file_path.touch(exist_ok=True)
    logger.info(f"{datetime.now()} [INFO] File created successfully.")

suite = TestSuite(logger)
browser = Browser("Chrome", logger)
browser.browser_name = "Firefox"
suite.add_test(LoginTest(browser, logger))
suite.add_test(PaymentTest(browser, logger))

runner = Runner()
runner.execute(suite, logger)