# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import config


class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(config.CHROME_DRIVER_PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://ais.usvisa-info.com/en-am/niv/users/sign_in")
        driver.find_element_by_id("user_email").clear()
        driver.find_element_by_id("user_email").send_keys(config.USER_EMAIL)
        driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys(config.PASSWORD)
        driver.find_element_by_xpath("//form[@id='new_user']/div[3]/label/div").click()
        driver.find_element_by_name("commit").click()
        driver.get("https://ais.usvisa-info.com/en-am/niv/users/sign_in")
        driver.find_element_by_link_text("Continue").click()
        href = driver.find_element_by_xpath("//a[contains(text(),'Pay Visa Fee')]").get_property('href')
        driver.get(href)
        self.assertEqual("No Appointments Available",
                         driver.find_element_by_xpath("//div[@id='paymentOptions']/div[2]/table/tbody/tr/td[2]").text)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
