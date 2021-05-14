import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from Pages.SearchPage import SearchPage
import time

class Test_01_Main:
    baseURL="https://www.zoopla.co.uk/"
    location="London"
    value="Highest price"

    def test_main(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        print(self.baseURL.title())
        self.sp = SearchPage(self.driver)
        self.sp.clickCookies()
        self.sp.clickLocation(self.location)
        self.sp.clickSearch()
        self.sp.sortHighestprice()
        self.sp.sortDescending(self)
        self.sp.fifthProperty()
        self.sp.fifthValue()
        self.sp.agentPage()
        self.sp.agentDetails()






