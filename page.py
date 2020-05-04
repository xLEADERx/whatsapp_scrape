from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class BasePage(object):
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver):
        self.driver = driver


class WhatsAppWebPage(BasePage):
    '''
    Main WhatsApp Web Page for Scrapping User Zoom Message
    '''
    def WaitForDom(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MainPageLocators.SEARCH_BUTTON))
        return True