#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from test.common import common


def main(url):
    # login
    browser = common.login(url)
    # Let the page loadß
    browser.implicitly_wait(30)

    browser.find_element_by_css_selector('#li_policyComp > span').click()
    # browser.find_eleme('Discover NE').click()
    browser.find_element_by_xpath(
        "//div[@id='discoverPolicyMgr-bodyWrap']/div[2]/div/div/a/span/span/span").click()

    common.set_ip(browser, host='100.100.100.2')
    common.set_seedNe(browser)
    browser.find_element_by_link_text('Save').click()


if __name__ == '__main__':
    main(url='https://192.168.20.20:8443/virtuoranc/login.html')
