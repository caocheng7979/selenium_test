#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys


def send_key(self,times,key):
    while times > 0:
        self.send_keys(key)
        times = times - 1

profile = webdriver.FirefoxProfile('C:\\Users\\admin\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\b819gahu.default')
# profile.accept_untrusted_certs = True
# profile.add_argument("--start-maximized")
# profile.set_preference('network.proxy.type', 1)
# profile.set_preference('network.proxy.socks', 'localhost')
# profile.set_preference('network.proxy.socks_port', 30080)
profile.update_preferences()
# Get local session of Firefox
browser = webdriver.Firefox(firefox_profile = profile)
# browser.maximize_window()
# Load page
browser.get('https://192.168.10.30:8443/virtuoranc/login.html')

# Let the page load  
browser.implicitly_wait(30)

#login start
browser.find_element_by_id('textfield-1017-inputEl').clear()
browser.find_element_by_id('textfield-1017-inputEl').send_keys('admin')

browser.find_element_by_id('textfield-1019-inputEl').clear()
browser.find_element_by_id('textfield-1019-inputEl').send_keys('admin')

browser.find_element_by_id('checkbox-1020-inputEl').click()

browser.find_element_by_id('container-1023-innerCt').click()
#login end

#create service
browser.find_element_by_css_selector('#li_topologyComp > span').click()
browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/a/span/span").click()
browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/a/span").click()

#service Name
service_name = browser.find_element_by_name('svcName')
service_name.send_keys('test3')
#service State
service_state = browser.find_element_by_name('state')
service_state.click()
service_state.send_keys(Keys.DOWN)
service_state.send_keys(Keys.ENTER)
#service Line Rate
service_line_rate = browser.find_element_by_name('lineRate')
service_line_rate.click()
send_key(service_line_rate,3,Keys.DOWN)
service_line_rate.send_keys(Keys.ENTER)
#service Routing Objective
service_routing_objective = browser.find_element_by_name('rtObj')
service_routing_objective.click()
send_key(service_routing_objective,3,Keys.DOWN)
service_routing_objective.send_keys(Keys.ENTER)
#service Source Node
service_source_node = browser.find_element_by_name('tidA')
service_source_node.click()
send_key(service_source_node,8,Keys.DOWN)
service_source_node.send_keys(Keys.ENTER)
#service Source End Point
service_source_end_point = browser.find_element_by_name('ctpAidA')
service_source_end_point.click()
service_source_end_point.send_keys(Keys.DOWN)
service_source_end_point.send_keys(Keys.ENTER)
#service Target Node
service_target_node = browser.find_element_by_name('tidZ')
service_target_node.click()
send_key(service_target_node,5,Keys.DOWN)
service_target_node.send_keys(Keys.ENTER)
#service Target End Point
service_target_end_point = browser.find_element_by_name('ctpAidZ')
service_target_end_point.click()
service_target_end_point.send_keys(Keys.DOWN)
service_target_end_point.send_keys(Keys.ENTER)
#save
browser.find_element_by_link_text('Next').click()