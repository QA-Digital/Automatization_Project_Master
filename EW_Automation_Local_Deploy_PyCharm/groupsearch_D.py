import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_groupsearch, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC

from FW.groupsearch_D import groupSearch_D


class Test_Groupsearch_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_groupsearch_D(self):
        driver = self.driver
        self.driver.maximize_window()
        self.driver.get(URL_groupsearch)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(2.5)
        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()

        groupSearch_D(self, driver)
        self.test_passed = True