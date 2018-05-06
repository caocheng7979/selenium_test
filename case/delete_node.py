#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from test.common import common


def main(url):
    # login
    browser = common.login(url)
    # Let the page load
    browser.implicitly_wait(30)

    browser.find_element_by_css_selector('#li_topologyComp > span').click()
    common.choose_layers(browser, 'WDM')
    browser.find_element_by_xpath(
        "//body[@id='ext-element-1']/div[3]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/a[2]/span/span").click()
    common.selectNode_net(browser, 'tokyo-T200-1')  # name of node
    browser.find_element_by_xpath(
        "//body[@id='ext-element-1']/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/a[3]/span/span").click()
    browser.find_element_by_xpath(
        "//div[@id='messagebox-1001-bodyWrap']//span[contains(text(), 'はい')]").click()

    browser.find_element_by_css_selector('#li_policyComp > span').click()
    common.selectNode_conf(browser, 'tokyo-T200-1')  # name of node
    browser.find_element_by_xpath(
        "//div[@id='discoverPolicyMgr-bodyWrap']/div[2]/div/div/a[2]/span/span/span").click()
    browser.find_element_by_xpath(
        "//div[@id='discoverPolicyMgr-bodyWrap']//span[contains(text(), 'はい')]").click()


if __name__ == '__main__':
    main(url='https://192.168.20.20:8443/virtuoranc/login.html')
