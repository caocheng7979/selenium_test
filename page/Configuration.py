#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from selenium_test.page.browser import BasePage
from selenium_test.common import CommonConfiguration
from selenium.webdriver.common.keys import Keys


class ConfigurationPage(BasePage):
    """description of class"""
    def __init__(self, browser='chrome'):
        super().__init__(browser)

    # discover node
    def set_ip(self, host):
        IP = ('id', 'gne1-inputEl')
        ip = self.findElement(IP)
        ip.click()
        ip.send_keys(host)

    def set_seedNe(self, seedNe=True):
        SEEDNE = ('name', 'seedNe')
        if seedNe is True:
            self.findElement(SEEDNE).click
        else:
            pass

    def set_protocol(self, protocol):
        PROTOCOL = ('name', 'protocol')
        # self.find_element_by_name().click()
        pass

    def set_port(self, port_id):
        # port = self.find_element_by_name('port').click()
        # port.send_keys('')
        pass

    # def set_transport(self,transport):
    #     # port = self.find_element_by_name('transport').click()
    #     pass

    def selectNode_conf(self, node_id):
        xpath = "//div[@id='policyGrid-body']//a[contains(text(), \'" + node_id + "\')]/../../../td/div/span"
        self.find_element_by_xpath(xpath=xpath).click()

    def selectNode_net(self, node_id):
        xpath = "//div[@id='inventoryGridId-body']//a[contains(text(), \'" + node_id + "\')]/../../div[3]"
        self.find_element_by_xpath(xpath=xpath).click()
