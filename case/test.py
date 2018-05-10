#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from selenium_test.page.Configuration import ConfigurationPage
from selenium_test.common import CommonConfiguration as cc
from selenium_test.common.TestCaseInfo import TestCaseInfo
from datetime import datetime
from selenium_test.common import LogUtility
import time


class Test_login(unittest.TestCase):

    def setUp(self):
        self.base_url = cc.baseUrl()
        self.testCaseInfo = TestCaseInfo(id=1, name="Test login", owner='cao')
        # self.testResult = TestReport()
        LogUtility.CreateLoggerFile("Test_login")

    def test_login_1(self):
        ADDIP = ('100.100.100.2', '100.100.100.3')
        DELIP = ('100.100.100.2:830', )
        path_discoverNe = ('link_text', 'Discover NE')
        path_addNe = (
            'xpath', "//div[@id='discoverPolicyMgr-bodyWrap']/div[2]/div/div/a/span/span/span")
        path_delne = (
            'xpath', "//div[@id='discoverPolicyMgr-bodyWrap']/div[2]/div/div/a[2]/span/span/span")
        path_confirm = (
            'xpath', "//div[@id='messagebox-1001-bodyWrap']//span[contains(text(), 'Yes')]")
        path_save = ('link_text', 'Save')
        try:
            self.testCaseInfo.starttime = cc.getCurrentTime()

            # Step1: open login site
            LogUtility.Log("Open Base site"+self.base_url)
            sol_val = ConfigurationPage()
            sol_val.open(self.base_url)
            sol_val.login()
            sol_val.save_screen_shot()
            sol_val.choose_navigation("configuration")
            sol_val.save_screen_shot()
            # sol_val.findElement(path_discoverNe).click()
            # sol_val.save_screen_shot()
            # add NE
            # for ip in ADDIP:
            #     sol_val.findElement(path_addNe).click()
            #     sol_val.save_screen_shot()
            #     sol_val.set_ip(ip)
            #     sol_val.set_seedNe()
            #     sol_val.findElement(path_save).click()
            #     sol_val.save_screen_shot()
            #     time.sleep(5)
            # delete NE
            for ip in DELIP:
                sol_val.selectNode_conf(ip)  # name of nod(ip)
                sol_val.findElement(path_delne).click()
                sol_val.save_screen_shot()
                sol_val.findElement(path_confirm).click()
                sol_val.save_screen_shot()
                time.sleep(5)
            self.testCaseInfo.result = "Pass"

        except Exception as err:
            self.testCaseInfo.errorinfo = str(err)
            LogUtility.Log(("Got error: "+str(err)))
        finally:
            self.testCaseInfo.endtime = cc.getCurrentTime()
            self.testCaseInfo.secondsDuration = cc.timeDiff(
                self.testCaseInfo.starttime, self.testCaseInfo.endtime)
        pass

    def tearDown(self):
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
