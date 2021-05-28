import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.SearchPage import SearchPage
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
        self.sp.clickLocation(self.place)
        self.sp.clickSearch()
        self.sp.sortHighestprice(self)
        self.sp.sortDescending(self)
        self.sp.fifthProperty()
        self.sp.fifthValue()
        self.sp.agentPage()
        self.sp.agentDetails()






