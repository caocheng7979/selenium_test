#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selenium_test.page.login import LoginPage

class Test_login(unittest.TestCase):
    url = 'https://192.168.10.30:8443/virtuoranc/login.html'
    username = 'admin'
    password = 'admin'

    def setUp(self):
        self.page=LoginPage()
        self.page.get(Test_login.url)
        self.page.set_username(Test_login.username)

    


    def tearDown(self):
        pass
        