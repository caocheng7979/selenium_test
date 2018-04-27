#!/usr/bin/env python3
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
from login import login

def send_key(self,times,key):
    while times > 0:
        self.send_keys(key)
        times = times - 1

# login
web = 'https://192.168.10.30:8443/virtuoranc/login.html'
browser=login(website=web)

class CreateService(object):

    def __init__(self,service_name,service_state,service_linerate,
        service_rtObj,service_tidA,service_ctpAidA,service_tidZ,service_ctpAidZ)
        self.service_name = service_name
        self.service_state = service_state
        self.service_linerate = service_linerate
        self.service_rtObj = service_rtObj
        self.service_tidA = service_tidA
        self.service_ctpAidA = service_ctpAidA
        self.service_tidZ = service_tidZ
        self.service_ctpAidZ = service_ctpAtidZ
        
    # create service
    def service(self):
        try:
            browser.find_element_by_css_selector('#li_topologyComp > span').click()
            browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/a/span/span").click()
            browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/a/span/span").click()
        
        except Exception as exc:
            pass        
    # service Name
    def set_service_name(self):
        try:
            name = browser.find_element_by_name('svcName')
            name.send_keys(self.service_name)
        
        except Exception as exc:
            pass

    # service State
    def set_service_state(self):
        if self.state == 'Active':
            try:
                state = browser.find_element_by_name('state')
                state.click()
                state.send_keys(Keys.DOWN)
                state.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

        else self.state == 'Pending':
            pass

    # service Line Rate
    def set_service_linerate(self):
        if self.service_linerate == '100G':
            pass

        elif self.service_linerate == '10G':
            try:
                linerate = browser.find_element_by_name('lineRate')
                linerate.click()
                linerate.send_keys(Keys.DOWN)
                linerate.send_keys(Keys.ENTER)
            except Exception as exc:
                pass

        elif self.service_linerate == '10G-e':
            try:                
                linerate = browser.find_element_by_name('lineRate')
                linerate.click()
                send_key(linerate,2,Keys.DOWN)
                linerate.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

        elif self.service_linerate == '200G':
            try:
                linerate = browser.find_element_by_name('lineRate')
                linerate.click()
                send_key(linerate,3,Keys.DOWN)
                linerate.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

    # service Routing Objective
    def set_service_rtObj(slef):
        if self.service_rtObj == 'Least Cost':
                pass

        if self.service_rtObj == 'Least Hops':
            try:
                routing_objective = browser.find_element_by_name('rtObj')
                routing_objective.click()
                routing_objective.send_keys(Keys.DOWN)
                routing_objective.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

        if self.service_rtObj == 'Least Latency':
            try:
                routing_objective = browser.find_element_by_name('rtObj')
                routing_objective.click()
                send_key(routing_objective,2,Keys.DOWN)
                routing_objective.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

        if self.service_rtObj == 'Manual':
            try:
                routing_objective = browser.find_element_by_name('rtObj')
                routing_objective.click()
                send_key(routing_objective,3,Keys.DOWN)
                routing_objective.send_keys(Keys.ENTER)

            except Exception as exc:
                pass

    # service Source Node
    def set_service_tidA(self):
        try:
            source_node = browser.find_element_by_name('tidA')
            source_node.click()
            source_node.clear()
            source_node.send_keys(self.service_tidA)

        except Exception as exc:
            pass

    # service Source End Point
    def set_service_ctpAidA(self):
        try:
            source_end_point = browser.find_element_by_name('ctpAidA')
            source_end_point.click()
            source_end_point.send_keys(Keys.DOWN)
            source_end_point.send_keys(Keys.ENTER)

        except Exception as exc:
            pass

    # service Target Node
    def set_service_tidZ(self):
        try:        
            target_node = browser.find_element_by_name('tidZ')
            target_node.click()
            target_node.clear()
            target_node.send_keys(self.service_tidZ)

        except Exception as exc:
            pass

    # service Target End Point
    def set_service_ctpAidZ(self):
        try:
            service_target_end_point = browser.find_element_by_name('ctpAidZ')
            service_target_end_point.click()
            service_target_end_point.send_keys(Keys.DOWN)
            service_target_end_point.send_keys(Keys.ENTER)

         except Exception as exc:
            pass
     
# save
browser.find_element_by_link_text('Next').click()
# linkcombo
linkcombo = browser.find_elements_by_name('linkCombo')
linkcombo_2 = linkcombo[0]
linkcombo_2.click()
# linkcombo_2.send_keys(Keys.DOWN)
linkcombo_2.send_keys(Keys.ENTER)
# create
browser.find_element_by_link_text('Create').click()