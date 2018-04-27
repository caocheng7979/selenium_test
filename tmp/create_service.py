#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time 
from test.common import common

  
def main(url):
    # login
    browser=common.login(url)
    # Let the page load
    browser.implicitly_wait(30)

    browser.find_element_by_css_selector('#li_topologyComp > span').click()
    browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/a/span/span").click()
    browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/a/span/span").click()
    
    common.set_service_name(browser,service_name='autotest')
    # state: Active, Pending
    common.set_service_state(browser,state='Active')
    # service_linerate: 100G, 10G, 10G-e, 200G
    common.set_service_linerate(browser,service_linerate='100G')
    # service_rtObj: Least Cost, Least Hops, Least Latency, Manual
    common.set_service_rtObj(browser,service_rtObj='Manual')
    # service Source Node
    common.set_service_tidA(browser,service_tidA='kanagawa-T310-4')
    # service Source End Point
    common.set_service_ctpAidA(browser)
    # service Target Node
    common.set_service_tidZ(browser,service_tidZ='tokyo-T310-3')
    # service Target End Point
    common.set_service_ctpAidZ(browser)    
    # save
    browser.find_element_by_link_text('Next').click()
    # # linkcombo
    # linkcombo = browser.find_elements_by_name('linkCombo')
    # linkcombo_2 = linkcombo[0]
    # linkcombo_2.click()
    # # linkcombo_2.send_keys(Keys.DOWN)
    # linkcombo_2.send_keys(Keys.ENTER)
    # create
    browser.find_element_by_link_text('Create').click()


if __name__ == '__main__':
    main(url='https://192.168.20.20:8443/virtuoranc/login.html')