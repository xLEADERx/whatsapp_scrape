import unittest
from selenium import webdriver
import page

class ZoomAutomation(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")
        self.driver = webdriver.Chrome(options=options)

    def test_automate(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        WhatsAppWebpage = page.WhatsAppWebPage(self.driver) 
        assert WhatsAppWebpage.WaitForDom()
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()