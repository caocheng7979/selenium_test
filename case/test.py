#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from test.page.login import LoginPage

class Test_login(unittest.TestCase):
    url = 'https://192.168.10.30:8443/virtuoranc/login.html'
    username = 'admin'
    password = 'admin'

    def setUp(self):
        self.page=LoginPage()
        self.page.get(url)
        self.page.set_username()

    


    def tearDown(self):

        