#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# send same keys many times
def send_key(self,times,key):
    while times > 0:
        self.send_keys(key)
        times = times - 1

# login website 
def login(url,user_name='admin',password='admin'):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.accept_untrusted_certs = True
    chromeOptions.add_argument("--start-maximized")
    # Get local session of Chrome
    global browser
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    # Load page
    browser.get(url)

    # Let the page load
    browser.implicitly_wait(60)
    
    # login start
    browser.find_element_by_id('textfield-1017-inputEl').clear()
    browser.find_element_by_id('textfield-1017-inputEl').send_keys(user_name)

    browser.find_element_by_id('textfield-1019-inputEl').clear()
    browser.find_element_by_id('textfield-1019-inputEl').send_keys(password)

    browser.find_element_by_id('checkbox-1020-inputEl').click()

    browser.find_element_by_id('container-1023-innerCt').click()
    # login end
    return browser


# service  
# service Name
def set_service_name(browser,service_name):
    try:
        name = browser.find_element_by_name('svcName')
        name.send_keys(service_name)
    

# service State
def set_service_state(browser,state):
    if state == 'Active':
        try:
            state = browser.find_element_by_name('state')
            state.click()
            state.send_keys(Keys.DOWN)
            state.send_keys(Keys.ENTER)

    elif state == 'Pending':
            pass

# service Line Rate
def set_service_linerate(browser,service_linerate):
    if service_linerate == '100G':
        pass

    elif service_linerate == '10G':
        try:
            linerate = browser.find_element_by_name('lineRate')
            linerate.click()
            linerate.send_keys(Keys.DOWN)
            linerate.send_keys(Keys.ENTER)

    elif service_linerate == '10G-e':
        try:                
            linerate = browser.find_element_by_name('lineRate')
            linerate.click()
            send_key(linerate,2,Keys.DOWN)
            linerate.send_keys(Keys.ENTER)


    elif service_linerate == '200G':
        try:
            linerate = browser.find_element_by_name('lineRate')
            linerate.click()
            send_key(linerate,3,Keys.DOWN)
            linerate.send_keys(Keys.ENTER)


# service Routing Objective
def set_service_rtObj(browser,service_rtObj):
    if service_rtObj == 'Least Cost':
            pass

    elif service_rtObj == 'Least Hops':
        try:
            routing_objective = browser.find_element_by_name('rtObj')
            routing_objective.click()
            routing_objective.send_keys(Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)


    elif service_rtObj == 'Least Latency':
        try:
            routing_objective = browser.find_element_by_name('rtObj')
            routing_objective.click()
            send_key(routing_objective,2,Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)


    elif service_rtObj == 'Manual':
        try:
            routing_objective = browser.find_element_by_name('rtObj')
            routing_objective.click()
            send_key(routing_objective,3,Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)


# service Source Node
def set_service_tidA(browser,service_tidA):
    try:
        source_node = browser.find_element_by_name('tidA')
        source_node.click()
        source_node.clear()
        source_node.send_keys(service_tidA)
        source_node.send_keys(Keys.ENTER)


# service Source End Point
def set_service_ctpAidA(browser):
    try:
        source_end_point = browser.find_element_by_name('ctpAidA')
        source_end_point.click()
        source_end_point.send_keys(Keys.DOWN)
        source_end_point.send_keys(Keys.ENTER)


# service Target Node
def set_service_tidZ(browser,service_tidZ):
    try:        
        target_node = browser.find_element_by_name('tidZ')
        target_node.click()
        target_node.clear()
        target_node.send_keys(service_tidZ)
        target_node.send_keys(Keys.ENTER)


# service Target End Point
def set_service_ctpAidZ(browser):
    try:
        service_target_end_point = browser.find_element_by_name('ctpAidZ')
        service_target_end_point.click()
        service_target_end_point.send_keys(Keys.DOWN)
        service_target_end_point.send_keys(Keys.ENTER)

    
# discover node
def set_ip(browser,host):
    try:
        ip = browser.find_element_by_id('gne1-inputEl')
        ip.click()
        ip.send_keys(host)


def set_seedNe(browser,seedNe= True):
    if seedNe == True:
        browser.find_element_by_name('seedNe').click
    else:
        pass

def set_protocol(browser,protocol):
    # browser.find_element_by_name('protocol').click()
    pass

def set_port(browser,port_id):
    # port = browser.find_element_by_name('port').click()
    # port.send_keys('')
    pass

# def set_transport(browser,transport):
#     # port = browser.find_element_by_name('transport').click()
#     pass

def choose_layers(browser,layer):
    layers = browser.find_elements_by_name('topoLayerGrp')
    if layer == 'WDM':
        layer_wdm = layers[0]
        layer_wdm.click()
    elif layer == 'OTN':
        layer_otn = layer[1]
        layer_otn.click()
    elif layer == 'PACKET':
        layer_packet = layer[2]
        layer_packet.click()

def selectNode_conf(browser,node_id):  
    xpath = "//div[@id='policyGrid-body']//a[contains(text(), \'"+node_id+"\')]/../../../td/div/span"
    browser.find_element_by_xpath(xpath=xpath).click()

def selectNode_net(browser,node_id):  
    xpath = "//div[@id='inventoryGridId-body']//a[contains(text(), \'"+node_id+"\')]/../../div[3]"
    browser.find_element_by_xpath(xpath=xpath).click()
