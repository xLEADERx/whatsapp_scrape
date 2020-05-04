from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import subprocess
import sys
import pyautogui

CHAT_NAME = '' # Group Name

TARGET_LIST = [''] # Add zoom sender name

ZOOM_FULL_PATH = r'' #Add Zoom.exe path

WAIT_FOR_DOM_TO_LOAD = 15 # Secs to wait for DOM to load content

DAY = 'TODAY' # Fetch data from YESTERDAY or TODAY

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")

navegador = webdriver.Chrome(options=options) # Can Add Drivers Path executable_path="path/to/diver"

def Start():
    """
    Search the side panel and click the Chat Name if success return True
    """
    navegador.get("https://web.whatsapp.com/")

    time.sleep(WAIT_FOR_DOM_TO_LOAD) 

    container = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div')# panel-side 

    try:
        for item in container:
            name1 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
            name2 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[12]')
            name3 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]')
            name4 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[10]')

        for arg in [name1 , name2 , name3 , name4]:
            if CHAT_NAME in arg.text:
                arg.click()
                return True
        sys.exit(0)
    except SystemExit:
        navegador.close()
        sys.exit("Unable To Find CHAT_NAME in List")
    except Exception: 
        return False


def get_id(text):
    """
    Extract id from the text message

    NOTE: id must be six digits to be selected edit regex if you need to change it
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

    NOTE: password must be six digits to be selected edit regex if you need to change it
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


def open_app(meeting_id = None, password = None):
    """
    Open zoom and input all fields

    CHANGE X AND Y CORDINATES BY GETING YOUR SCREENS CORDS BY 'pyautogui.position()' 
    
    Read the docs for info: https://pyautogui.readthedocs.io/en/latest/mouse.html#the-screen-and-mouse-position

    Refer to comments for individual buttons cords to input
    """
    subprocess.Popen([ZOOM_FULL_PATH])
    time.sleep(3) #wait to open zoom
    pyautogui.click(x=955, y=538, clicks=1, interval=1, button='left') #click join a meeting
    if meeting_id != None and password == None:
        time.sleep(5)
        pyautogui.write(meeting_id)
        #time.sleep(1)
        #pyautogui.click(x=761, y=656, clicks=1, interval=1, button='left') # Disconnect audio
        time.sleep(1)
        pyautogui.click(x=763, y=691, clicks=1, interval=1, button='left') # Disconnect video
        time.sleep(1)
        pyautogui.click(x=987, y=737, clicks=1, interval=1, button='left')  #Join Button
    elif meeting_id != None and password != None:
        time.sleep(5)
        pyautogui.write(meeting_id)
        #time.sleep(1)
        #pyautogui.click(x=761, y=656, clicks=1, interval=1, button='left') # Disconnect audio
        time.sleep(1)
        pyautogui.click(x=763, y=691, clicks=1, interval=1, button='left') # Disconnect video
        time.sleep(1)
        pyautogui.click(x=987, y=737, clicks=1, interval=1, button='left') # Join Button
        time.sleep(3)
        pyautogui.write(password)
        pyautogui.click(x=987, y=737, clicks=1, interval=1, button='left') # Join Button


def extractor(raw_msg):
    """
    extract metting id, password and open zoom from DAY specified 
    """
    msg_check = False

    regex = DAY + r'\b'
    
    cords = re.search(regex, raw_msg).span(0)

    raw_msg = raw_msg[cords[0] + len(DAY) + 1:]


    raw_msg = re.split('[0-9][0-9]:[0-9][0-9]\n', raw_msg)

    for msg in raw_msg:
        for TARGET in TARGET_LIST:
            regex = TARGET + r'\b'

            if bool(re.search(regex, msg)) and 'Meeting ID:' in msg and 'Password:' in msg:
                print(msg)
                meeting_id = get_id(msg)
                password = get_pass(msg)
                msg_check = True
                open_app(meeting_id, password)
            elif bool(re.search(regex, msg)) and 'Meeting ID:' in msg:
                print(msg)
                meeting_id = get_id(msg)
                msg_check = True
                open_app(meeting_id)

    if not msg_check:
        print('Unable to Find Zoom Message.')

    return raw_msg

#main block
if __name__ == '__main__':

    while True:
        if Start():
            break
        print('Error could not read the DOM content Retrying in 3 Secs...')
        time.sleep(3)

    messages = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]') # Path for messages section Scrape messages inside the sender section
      
    for _ in range(5):
        time.sleep(1)
        messages[0].send_keys(Keys.PAGE_UP)
      
    for msg in messages:
        raw_msg = msg.text
        #print(raw_msg)
        # sys.exit(0)
        parsed_msg = extractor(raw_msg)          
