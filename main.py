from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

CHAT_NAME = 'Fazil' #Change this

WAIT_FOR_DOM_TO_LOAD = 4 #secs to wait for DOM to load content

options = webdriver.ChromeOptions()
options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")

navegador = webdriver.Chrome(chrome_options=options)

navegador.get("https://web.whatsapp.com/")

time.sleep(WAIT_FOR_DOM_TO_LOAD) 

container = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div')#panel-side 

for item in container:
    name1 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]')
    name2 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[12]')
    name3 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[11]')
    name4 = item.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[10]')


def performClick(*args):
    for arg in args:
        if CHAT_NAME in arg.text: #change this to your Group Name
            arg.click()
            print('Clicked')
            return 'OK'
    return None

try:
    if performClick(name1, name2, name3, name4) != None:
        #Scrape messages inside the sender section
        messages = navegador.find_elements_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]') #path for messages section

        for _ in range(10):
            time.sleep(1)
            messages[0].send_keys(Keys.PAGE_UP)

        for msg in messages:
            print(msg.text)
            
except Exception as e:
    print('DOM NOT LOADED TRY INCREASING TIME TO WAIT FOR DOM TO LOAD')
    print(e)
