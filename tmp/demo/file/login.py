#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

def login(website, user_name="admin", password="admin"):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.accept_untrusted_certs = True
    chromeOptions.add_argument("--start-maximized")
    # Get local session of Chrome
    global browser
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    # Load page
    browser.get(website)

    # Let the page load
    # time.sleep(5)
    browser.implicitly_wait(30)

    # login start
    browser.find_element_by_id('textfield-1017-inputEl').clear()
    browser.find_element_by_id('textfield-1017-inputEl').send_keys(user_name)

    browser.find_element_by_id('textfield-1019-inputEl').clear()
    browser.find_element_by_id('textfield-1019-inputEl').send_keys(password)

    browser.find_element_by_id('checkbox-1020-inputEl').click()

    browser.find_element_by_id('container-1023-innerCt').click()
    # login end
    return browser