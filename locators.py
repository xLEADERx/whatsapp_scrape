from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """
    A class for main page locators. All main page locators should come here
    """
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')