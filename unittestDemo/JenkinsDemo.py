#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from time import sleep

class TestClass(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Firefox()
        self.base_url = "http://www.testclass.net"
        self.driver.implicitly_wait(10)

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    def test_case1(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        search_ipput = self.driver.find_element_by_id("wd")
        search_ipput.clear()
        search_ipput.send_keys("selenium")
        search_ipput.submit()

    def test_case2(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        search_input = self.driver.find_element_by_id("wd")
        search_input.clear()
        search_input.send_keys("Jenkins")
        search_input.submit()

if __name__ == '__main__':
    unittest.main()