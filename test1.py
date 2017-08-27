# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BaiduWebdriver(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_baidu_webdriver(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        # ERROR: Caught exception [ERROR: Unsupported command [clickAt | id=kw | 12,10]]
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        driver.find_element_by_id("form").submit()
    

    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
