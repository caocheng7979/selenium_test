#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BaseTestPage(unittest.TestCase):
    def setUp(self,url):
        #create a new session
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.accept_untrusted_certs = True
        chromeOptions.add_argument("--start-maximized")
        # Get local session of Chrome
        self.driver = webdriver.Chrome(chrome_options=chromeOptions)
        # Load page
        self.driver.get(url)
        # Let the page load
        self.driver.implicitly_wait(30)

    def tearDown(self):
        #close the browser window
        self.driver.quit()
