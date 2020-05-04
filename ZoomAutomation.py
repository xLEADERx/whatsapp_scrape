import unittest
from selenium import webdriver
import page
import time
class ZoomAutomation(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def test_LoadDom(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        WhatsAppWebpage = page.WhatsAppWebPage(self.driver) 
        assert WhatsAppWebpage.WaitForDom()
        assert WhatsAppWebpage.ScrapeChatName('XII-D')
        assert WhatsAppWebpage.Page_Up(5)
        assert WhatsAppWebpage.Scrape_messages(['Rati Gupta', 'Rohit', 'Pradeep kumar Dwivedi', 'Me'], 'YESTERDAY')

        # #time.sleep(100)
    

    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()