
from framework.logging.Logger import Logger
from framework.core.CustomExceptions import CustomExceptions

class Browser():

    def __init__(self, browser_name, logger):
        self.browser_name = browser_name
        self._is_open = False
        self.logger = logger

    @property
    def browser_name(self):
        return self._browser_name
    
    @browser_name.setter
    def browser_name(self, name):
        if name not in ["Chrome", "Firefox", "Edge"]:
            raise CustomExceptions.InvalidBrowserNameError("Invalid browser name")
            # raise Exception("Invalid browser name")
        
        self._browser_name = name

    def open(self):
        self._is_open = True
        # print(f"{self._browser_name} browser opened")
        self.logger.info(f"{self._browser_name} browser opened")

    def close(self):
        self._is_open = False
        # print(f"{self._browser_name} browser closed")       
        self.logger.info(f"{self._browser_name} browser closed") 

    def navigate(self, url):
        # print(f"validating url: {Browser.validate_url(url)}")
        self.logger.info(f"validating url: {Browser.validate_url(url)}")
        if not (Browser.validate_url(url)):
            raise CustomExceptions.InvalidUrlError("Invalid url")
            # raise Exception("Invalid url")
        
        if self._is_open == True:
            # print(f"{self._browser_name} browser navigated to {url}")
            self.logger.info(f"{self._browser_name} browser navigated to {url}")
        else:
            # print(f"{self._browser_name} browser is closed")
            self.logger.info(f"{self._browser_name} browser is closed")
            # raise Exception(f"{self._browser_name} browser is closed")
            raise CustomExceptions.BrowserClosedError(f"{self._browser_name} browser is closed")

    def click(self, element):
        if self._is_open == True:
            print(f"clicking on {element}")
        else:
            print(f"{self._browser_name} browser is closed")
            # raise Exception(f"{self._browser_name} browser is closed")
            raise CustomExceptions.BrowserClosedError(f"{self._browser_name} browser is closed")

    def type_text(self, element, text):
        if self._is_open == True:
            print(f"typing {text} on {element}")
        else:
            print(f"{self._browser_name} browser is closed")
            # raise Exception(f"{self._browser_name} browser is closed")
            raise CustomExceptions.BrowserClosedError(f"{self._browser_name} browser is closed")
    
    def take_screenshot(self):
        if self._is_open == True:
            print(f"taking screenshot")
        else:
            print(f"{self._browser_name} browser is closed")
            # raise Exception(f"{self._browser_name} browser is closed")
            raise CustomExceptions.BrowserClosedError(f"{self._browser_name} browser is closed")
        
    @staticmethod
    def validate_url(url):
        return url.startswith("https://")

if __name__ == "__main__":
    logger = Logger()
    browser = Browser("Chrome", logger)
    
    browser.open()
    try:
        browser.navigate("https://google.com")
    except CustomExceptions.InvalidUrlError as e:
        logger.error(e)
    except CustomExceptions.BrowserClosedError as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)

    browser.close()