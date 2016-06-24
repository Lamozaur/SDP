import re

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

import unittest
import time

class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.rec-global.com"

    def test_Search(self):
        driver = self.driver
        driver.get(self.base_url + "/search")
        SearchField = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_id("search-searchword"))
        SearchField.send_keys("QA Engineer")
        Button = WebDriverWait(driver,10).until(lambda driver: driver.find_element_by_name("Search"))
        time.sleep(5) 
        Button.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()