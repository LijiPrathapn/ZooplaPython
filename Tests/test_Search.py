
import time
from Pages.SearchPage import SearchPage
from Utilities.readProperties import ReadConfig
class Test_01_Main:
    baseURL = ReadConfig.getApplicationURL()
    place = ReadConfig.getLocation()


    def test_main(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        print(self.baseURL.title())
        self.sp = SearchPage(self.driver)
        self.sp.clickCookies()
        time.sleep(3)
        self.sp.clickLocation(self.place)
        self.sp.clickSearch()
        self.sp.sortHighestprice(self)
        time.sleep(3)
        self.sp.sortDescending(self)
        self.sp.fifthProperty()
        time.sleep(3)
        self.sp.fifthValue()
        self.sp.agentPage()
        self.sp.agentDetails()







