from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import MainPageLocators
import time
import pyautogui
import subprocess
import re

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
        WebDriverWait(driver, 100).until(EC.presence_of_element_located(MainPageLocators.SEARCH_BUTTON))
        return True

    def ScrapeChatName(self, Target):
        driver = self.driver
        Chat_list = [MainPageLocators.ChatList_1, MainPageLocators.ChatList_2, MainPageLocators.ChatList_3, MainPageLocators.ChatList_4]
        mycontainer = driver.find_elements_by_xpath(MainPageLocators.container)
        for name in Chat_list:
            if Target in driver.find_element(*name).text:
                driver.find_element(*name).click()
                return True
        return False

    def Page_Up(self, number):
        driver = self.driver
        for _ in range(number):
            time.sleep(1)
            driver.find_element(*MainPageLocators.message_section).send_keys(Keys.PAGE_UP)
        return True

    def Scrape_messages(self, Target_list, Day, ZoomFullPath, join_meeting, video_cords, join_cords):

        def open_app(ZoomFullPath, join_meeting, video_cords, join_cords, meeting_id = None, password = None):
            """
            Open zoom and input all fields

            CHANGE X AND Y CORDINATES BY GETING YOUR SCREENS CORDS BY 'pyautogui.position()' 
            
            Read the docs for info: https://pyautogui.readthedocs.io/en/latest/mouse.html#the-screen-and-mouse-position

            Refer to comments for individual buttons cords to input
            """
            subprocess.Popen([ZoomFullPath])
            time.sleep(3) #wait to open zoom
            pyautogui.click(*join_meeting, clicks=1, interval=1, button='left')
            if meeting_id != None and password == None:
                time.sleep(5)
                pyautogui.write(meeting_id)
                time.sleep(1)
                pyautogui.click(*video_cords, clicks=1, interval=1, button='left')
                time.sleep(1)
                pyautogui.click(*join_cords, clicks=1, interval=1, button='left') 
            elif meeting_id != None and password != None:
                time.sleep(5)
                pyautogui.write(meeting_id)
                time.sleep(1)
                pyautogui.click(*video_cords, clicks=1, interval=1, button='left')
                time.sleep(1)
                pyautogui.click(*join_cords, clicks=1, interval=1, button='left')
                time.sleep(3)
                pyautogui.write(password)
                pyautogui.click(*join_cords, clicks=1, interval=1, button='left')


        def extractor(raw_msg, Target_list, Day, ZoomFullPath, join_meeting, video_cords, join_cords):
            """
            extract metting id, password and open zoom from Day specified 
            """
            msg_check = False
            regex = Day + r'\b'
            cords = re.search(regex, raw_msg).span(0)
            raw_msg = raw_msg[cords[0] + len(Day) + 1:]
            raw_msg = re.split('[0-9][0-9]:[0-9][0-9]\n', raw_msg)

            for msg in raw_msg:
                
                for TARGET in Target_list:
                    
                    regex = TARGET + r'\b'
                    if bool(re.search(regex, msg)) and 'Meeting ID:' in msg and 'Password:' in msg:
                        print(msg)
                        meeting_id = get_id(msg)
                        password = get_pass(msg)
                        msg_check = True
                        open_app(ZoomFullPath, join_meeting, video_cords, join_cords, meeting_id, password)
                    elif bool(re.search(regex, msg)) and 'Meeting ID:' in msg:
                        print(msg)
                        meeting_id = get_id(msg)
                        msg_check = True
                        open_app(ZoomFullPath, join_meeting, video_cords, join_cords, meeting_id, password=None)

            if not msg_check:
                print('Unable to Find Zoom Message.')
                return False

            return raw_msg


        def get_id(text):
            """
            Extract id from the text message

            Note: id must be six digits to be selected edit regex if you need to change it
            """
            try:
                regex = '[0-9][0-9][0-9] [0-9][0-9][0-9][0-9]? [0-9][0-9][0-9][0-9]'
                text = re.findall(regex, text)
                return text[0]
            except Exception as e:
                print('get_id func ' + str(e))
                return None


        def get_pass(text):
            """
            Extract password from the text message

            Note: password must be six digits to be selected edit regex if you need to change it
            """
            try:
                regex = 'Password: [0-9 A-Z a-z][0-9 A-Z a-z][0-9 A-Z a-z][0-9 A-Z a-z][0-9 A-Z a-z][0-9 A-Z a-z]'
                text = re.findall(regex, text)
                new_text = text[0]
                new_text = new_text[new_text.index(' ') + 1:]
                return new_text
            except Exception as e:
                print('get_pass func ' + str(e))
                return None
        
        driver = self.driver
        raw_message = driver.find_element(*MainPageLocators.message_section).text
        parsed_msg = extractor(raw_message, Target_list, Day, ZoomFullPath, join_meeting, video_cords, join_cords) 
        if parsed_msg:    
            return True
        return False     