#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from teselenium_testst.page.browser import BasePage
from selenium_test.common import CommonConfiguration
from selenium.webdriver.common.keys import Keys

class NetworkPage(BasePage):
    """description of class"""
    # page element identifier
    
    
   
    
    




    def __init__(self, browser = 'chrome'):
        super().__init__(browser)
        self.find_element_by_css_selector('#li_topologyComp > span').click()

    LAYER = ('name','topoLayerGrp')
    def choose_layers(self,layer):
        '''
        choose network's layer

        Usage:
        self.choose_layer(layer)
        '''
        layers = self.findElements(NetworkPage.LAYER)
        if layer == 'WDM':
            layer_wdm = layers[0]
            layer_wdm.click()
        elif layer == 'OTN':
            layer_otn = layer[1]
            layer_otn.click()
        elif layer == 'PACKET':
            layer_packet = layer[2]
            layer_packet.click() 
    
    def choose_
    browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div/a/span/span").click()
    browser.find_element_by_xpath("//body[@id='ext-element-1']/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/a/span/span").click()
    
    # service  
    # service Name
    SVCNAME = ('name','svcName')
    def set_service_name(self,service_name):
        name = self.findElement(NetworkPage.SVCNAME)
        name.send_keys(service_name)


    # service State
    STATE = ('name','state')
    def set_service_state(self,state):
        if state == 'Active':
            state = self.findElement(NetworkPage.STATE)
            state.click()
            state.send_keys(Keys.DOWN)
            state.send_keys(Keys.ENTER)
                
        elif state == 'Pending':
                pass

    # service Line Rate
    LINERATE = ('name','lineRate')
    def set_service_linerate(self,service_linerate):
        if service_linerate == '100G':
            pass

        elif service_linerate == '10G':
            linerate = self.findElement(NetworkPage.LINERATE)
            linerate.click()
            linerate.send_keys(Keys.DOWN)
            linerate.send_keys(Keys.ENTER)
                

        elif service_linerate == '10G-e':
            linerate = self.findElement(NetworkPage.LINERATE)
            linerate.click()
            self.send_key(linerate,2,Keys.DOWN)
            linerate.send_keys(Keys.ENTER)
                

        elif service_linerate == '200G':
            linerate = self.findElement(NetworkPage.LINERATE)
            linerate.click()
            self.send_key(linerate,3,Keys.DOWN)
            linerate.send_keys(Keys.ENTER)
                

    # service Routing Objective
    RTOBJ = ('name','rtObj')
    def set_service_rtObj(self,service_rtObj):
        if service_rtObj == 'Least Cost':
                pass

        elif service_rtObj == 'Least Hops':
            routing_objective = self.findElement(NetworkPage.RTOBJ)
            routing_objective.click()
            routing_objective.send_keys(Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)
                

        elif service_rtObj == 'Least Latency':
            routing_objective = self.findElement(NetworkPage.RTOBJ)
            routing_objective.click()
            self.send_key(routing_objective,2,Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)
                

        elif service_rtObj == 'Manual':
            routing_objective = self.findElement(NetworkPage.RTOBJ)
            routing_objective.click()
            self.send_key(routing_objective,3,Keys.DOWN)
            routing_objective.send_keys(Keys.ENTER)
                

    # service Source Node
    TIDA = ('name','tidA')
    def set_service_tidA(self,service_tidA):
        source_node = self.findElement(NetworkPage.TIDA)
        source_node.click()
        source_node.clear()
        source_node.send_keys(service_tidA)
        source_node.send_keys(Keys.ENTER)

    # service Source End Point
    CTPAIDA = ('name','ctpAidA')
    def set_service_ctpAidA(self):
        source_end_point = self.findElement(NetworkPage.CTPAIDA)
        source_end_point.click()
        source_end_point.send_keys(Keys.DOWN)
        source_end_point.send_keys(Keys.ENTER)

    # service Target Node
    TIDZ = ('name','tidZ')
    def set_service_tidZ(self,service_tidZ):
        target_node = self.findElement(NetworkPage.TIDZ)
        target_node.click()
        target_node.clear()
        target_node.send_keys(service_tidZ)
        target_node.send_keys(Keys.ENTER)

    # service Target End Point
    CTPAIDZ = ('name','ctpAidZ')
    def set_service_ctpAidZ(self):
        service_target_end_point = self.findElement(NetworkPage.CTPAIDZ)
        service_target_end_point.click()
        service_target_end_point.send_keys(Keys.DOWN)
        self.enter(service_target_end_point)
   
    
