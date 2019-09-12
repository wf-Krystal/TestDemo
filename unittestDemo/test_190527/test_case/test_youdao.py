#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from selenium import webdriver
from time import sleep

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "http://wwww.youdao.com"

    def test_youdao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("query").clear()
        driver.find_element_by_id("query").send_keys("webdriver")
        driver.find_element_by_id("qb").click()