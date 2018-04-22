#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from test.common.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPage(Browser):
    """description of class"""
    def __init__(self, browser = 'chrome'):
        super.__init__(browser)
    # page element identifier
    username = (By.ID,'textfield-1017-inputEl')
    password = (By.ID,'textfield-1019-inputEl')
    checkbox = (By.ID,'checkbox-1020-inputEl')
    okbutton = (By.ID,'container-1023-innerCt')

    # Get username textbox and input username
    def set_username(self,username):
        name = self.driver.find_element(*LoginPage.username)
        name.send_keys(username)

    # Get password textbox and input password, then hit return 
    def set_password(self, password):  
        pwd = self.driver.find_element(*LoginPage.password)  
        pwd.send_keys(password + Keys.RETURN)

    # agree to the terms and conditions below
    def click_checkbox(self):
        check = self.driver.find_element(*LoginPage.checkbox)
        check.click()
    
    # click login in
    def click_Login(self):
        okbtn = self.driver.find_element(*LoginPage.okbutton)
        okbtn.click()



    
