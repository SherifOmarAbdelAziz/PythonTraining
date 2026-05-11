
# from framework import (
#     Logger, 
#     TestSuite
# )

class Runner:

    def execute(self, test_suite, logger):
        
        # suite.add_test(LoginTest(browser, logger))
        # suite.add_test(PaymentTest(browser, logger))
        logger.info("--------------")
        logger.info(test_suite)
        test_suite.run_all()
        logger.info("--------------")
        
        for result in test_suite.run_all():
            logger.info(result)