from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from KTGHU_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_FM, sendEmail, setUp, tearDown

from KTGHU_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest



class TestFM_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_FM_D(self):
        self.driver.get(URL_FM)
        wait = WebDriverWait(self.driver, 1500)
        self.driver.maximize_window()
        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(1.5)

        wait.until(EC.visibility_of(self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")))
        teaserItems = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        try:
            for WebElement in teaserItems:
                ##print(len(teaserItems))
                jdouvidet = WebElement.is_displayed()
                ##print(jdouvidet)
                if jdouvidet == True:
                    ##print(jdouvidet)
                    ##print(WebElement)
                    pass

                else:
                    pass
                    ##print("Else")
                    ##emailfunciton

        except NoSuchElementException:
            pass
            ##print("no such")
            ##email fnction

        assert teaserItems[0].is_displayed() == True
        self.test_passed = True