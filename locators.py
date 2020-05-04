from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """
    A class for main page locators. All main page locators should come here
    """
    TARGET_LIST = ['Rati Gupta', 'Rohit', 'Pradeep kumar Dwivedi', 'Me']
    SEARCH_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]')
    message_section = (By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]')
    container = '/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div'# panel-side 
    ChatList_1 = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[1]')
    ChatList_2 = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[12]')
    ChatList_3 = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[11]')
    ChatList_4 = (By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[10]')
