#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_test.common import ResultFolder


class BasePage(object):
    """description of class"""

    # webdriver instance
    def __init__(self, browser='chrome'):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''

        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            chromeOptions = webdriver.ChromeOptions()
            chromeOptions.accept_untrusted_certs = True
            chromeOptions.add_argument("--start-maximized")
            chromeOptions.add_argument("lang=en-US.UTF-8")
            driver = webdriver.Chrome(chrome_options=chromeOptions)
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == "phantomjs":
            driver = webdriver.PhantomJS()
        try:
            self.driver = driver
        except Exception:
            raise NameError(
                "Not found %s browser,You can enter 'ie', 'ff' or 'chrome'." % browser)

    def findElement(self, element):
        '''
        Find element

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElement(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_element_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError(
                    "Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def findElements(self, element):
        '''
        Find elements

        element is a set with format (identifier type, value), e.g. ('id','username')

        Usage:
        self.findElements(element)
        '''
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)

            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_elements_by_name(value)

            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_elements_by_class_name(value)

            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_elements_by_link_text(value)

            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_elements_by_xpath(value)

            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError(
                    "Please correct the type in function parameter")
        except Exception:
            raise ValueError("No such element found" + str(element))
        return elem

    def open(self, url):
        '''
        Open web url

        Usage:
        self.open(url)
        '''
        if url != "":
            self.driver.get(url)
            self.driver.implicitly_wait(30)
        else:
            raise ValueError("please provide a base url")

    def type(self, element, text):
        '''
        Operation input box.

        Usage:
        self.type(element,text)
        '''
        element.send_keys(text)

    def enter(self, element):
        '''
        Keyboard: hit return

        Usage:
        self.enter(element)
        '''
        element.send_keys(Keys.RETURN)

    # send same keys many times
    def send_key(self, element, times, key):
        while times > 0:
            element.send_keys(key)
            times = times - 1

    def click(self, element):
        '''
        Click page element, like button, image, link, etc.
        '''
        element.click()

    def quit(self):
        '''
        Quit webdriver
        '''
        self.driver.quit()

    def getAttribute(self, element, attribute):
        '''
        Get element attribute

        '''
        return element.get_attribute(attribute)

    def getText(self, element):
        '''
        Get text of a web element

        '''
        return element.text

    def getTitle(self):
        '''
        Get window title
        '''
        return self.driver.title

    def getCurrentUrl(self):
        '''
        Get current url
        '''
        return self.driver.current_url

    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y%m%d', time.localtime(time.time()))
        screenshot_path = ResultFolder.GetRunDirectory() + '\\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H%M%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(
            screenshot_path + '\\%s_%s.png' % (name, tm))
        return screenshot

    def maximizeWindow(self):
        '''
        Maximize current browser window
        '''
        self.driver.maximize_window()

    def back(self):
        '''
        Goes one step backward in the browser history.
        '''
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        """
        self.driver.forward()

    def getWindowSize(self):
        """
        Gets the width and height of the current window.
        """
        return self.driver.get_window_size()

    def refresh(self):
        '''
        Refresh current page
        '''
        self.driver.refresh()
        # self.driver.switch_to()

    def login(self, username='admin', password='admin'):
        '''
        Login web

        Usage:
        self.login(username,password)
        '''
        path_username = ('id', 'textfield-1017-inputEl')
        path_password = ('id', 'textfield-1019-inputEl')
        path_checkbox = ('id', 'checkbox-1020-inputEl')
        path_okbutton = ('id', 'container-1023-innerCt')

        # Get username textbox and input username
        name = self.findElement(path_username)
        name.send_keys(username)

        # Get password textbox and input password, then hit return
        pwd = self.findElement(path_password)
        pwd.send_keys(password)

        # agree to the terms and conditions below
        check = self.findElement(path_checkbox)
        check.click()

        # click login in
        okbtn = self.findElement(path_okbutton)
        okbtn.click()
        return self

    def choose_navigation(self, text):
        '''
        Choose navigation

        Usage:
        self.choose_navigation(text)
        '''
        path_dashboard = ('css', '#li_dashboardComp > span')
        path_network = ('css', '#li_topologyComp > span')
        path_design = ('css', '#li_designComp > span')
        path_configuration = ('css', '#li_policyComp > span')
        path_monitor = ('css', '#li_fpmComp > span')
        path_administration = ('css', '#li_sysAdminComp > span')

        if text == "dashboard" or text == "Dashboard" or text == "DASHBOARD":
            dashboard = self.findElement(path_dashboard)
            dashboard.click()
        elif text == "network" or text == "Network" or text == "NETWORK":
            network = self.findElement(path_network)
            network.click()
        elif text == "design" or text == "Design" or text == "DESGIN":
            design = self.findElement(path_design)
            design.click()
        elif text == "configuration" or text == "Configuration" or text == "CONFIGURATION":
            configuration = self.findElement(path_configuration)
            configuration.click()
        elif text == "monitor" or text == "Monitor" or text == "MONITOR":
            self.findElement(path_monitor).click()
        elif text == "administration" or text == "Administration" or text == "ADMINISTRATION":
            administration = self.findElement(path_administration)
            administration.click()
