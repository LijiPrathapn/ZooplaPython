from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

class SearchPage:
    cookies_click_xpath ="//*[@id='cookie-consent-form']/div/div/div/button[2]"
    time.sleep(5)
    location_textbox_xpath ="//input[@id='header-location']"
    search_box="//button[contains(text(),'Search')]"
    highest_price_id="sort-order-dropdown"
    descending_price="//p[contains(@class,'css-6v9gpl-Text eczcs4p0')]"
    fifth_property="//body/div[@id='__next']/div[6]/div[1]/main[1]/div[2]/div[2]/div[5]/div[1]/div[1]/div[2]/a[1]"
    fifth_value="//*[@id='main-content']/div[1]/div[10]/div/div[1]/div[1]/h3"
    agent_page="//body/div[@id='__next']/main[@id='main-content']/div[1]/div[10]/div[1]/div[1]/div[1]/a[1]/img[1]"
    agent_details="//*[@id='content']/div/h1"

    def __init__(self,driver):
        self.driver = driver


    def clickCookies(self):
        self.driver.find_element_by_xpath(self.cookies_click_xpath).click()


    def clickLocation(self,place):
        self.driver.find_element_by_xpath(self.location_textbox_xpath).send_keys(place)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.search_box).click()

    def sortHighestprice(self,dropdown):
        dropdown=Select(self.driver.find_element_by_id(self.highest_price_id))
        dropdown.select_by_visible_text('Highest price')

    def sortDescending(self,descending_price):
        time.sleep(5)
        a=self.driver.find_elements_by_xpath(self.descending_price)
        for i in a:
            print("The Property Price is ",i.text)

    def fifthProperty(self):
        self.driver.find_element_by_xpath(self.fifth_property).click()

    def fifthValue(self):
        b=self.driver.find_element_by_xpath(self.fifth_value)
        print("The Fifth Property is clicked",b.text)

    def agentPage(self):
        self.driver.find_element_by_xpath(self.agent_page).click()

    def agentDetails(self):
        c=self.driver.find_element_by_xpath(self.agent_details)
        time.sleep(5)
        print("The Agent details is on agent page",c.text)



 #
 # def setManagerOfVendor(self,value):
 #        drp=Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
 #        drp.select_by_visible_text(value)

