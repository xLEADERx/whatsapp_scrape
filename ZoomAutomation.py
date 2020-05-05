import unittest
from selenium import webdriver
import Webpage

class ZoomAutomation(unittest.TestCase):
    
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"user-data-dir=D:\Python\Memory\WebWhatsAppBot")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def test_LoadDom(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        WhatsAppWebpage = Webpage.WhatsAppWebPage(self.driver) 
        assert WhatsAppWebpage.WaitForDom()
        assert WhatsAppWebpage.ScrapeChatName('XII-D')
        assert WhatsAppWebpage.Page_Up(5)
        Target_list = ['Rati Gupta', 'Rohit', 'Pradeep kumar Dwivedi', 'Me']
        ZoomFullPath = r'C:\Users\Arshad\AppData\Roaming\Zoom\bin\Zoom.exe'
        join_meeting = (955, 538)
        video_cords = (763, 691)
        join_cords = (987, 737)
        assert WhatsAppWebpage.Scrape_messages(Target_list=Target_list, Day='YESTERDAY', ZoomFullPath=ZoomFullPath, join_meeting=join_meeting, video_cords=video_cords, join_cords=join_cords)


    def tearDown(self):
        pass
        #self.driver.close()

if __name__ == '__main__':
    unittest.main()