from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from ET.Detail_D import detail_D
from selenium.webdriver.support.wait import WebDriverWait
from ET.to_import import acceptConsent,sendEmail, URL, URL_LM, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest

HPbanneryXpath = "//*[@class='f_teaser-item']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

from ET.to_import import URL_local
class TestHP_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_homePage_D(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)
        bannerSingle = self.driver.find_element(By.XPATH, HPbanneryXpath)
        try:
            bannerSingle = self.driver.find_element(By.XPATH, HPbanneryXpath)
            bannerAll = self.driver.find_elements(By.XPATH, HPbanneryXpath)
            #wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s bannery " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s bannery " + url
            sendEmail(msg)
        assert bannerSingle.is_displayed() == True
        time.sleep(1.5)

    def test_HP_LMnabidky(self):
        wait = WebDriverWait(self.driver, 150)
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)
        generalDriverWaitImplicit(self.driver)

        try:
            nejnabidkyLMsingle = self.driver.find_element(By.XPATH, "//*[@class='page-tour']")
            nejnabidkyLMall = self.driver.find_elements(By.XPATH, "//*[@class='page-tour']")
            wait.until(EC.visibility_of(nejnabidkyLMsingle))
            if nejnabidkyLMsingle.is_displayed():
                for WebElement in nejnabidkyLMall:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True
                    if jdouvidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem na HP s nej. nabidky LM " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem na HP s nej. nabidky LM " + url
            sendEmail(msg)

        assert nejnabidkyLMsingle.is_displayed() == True

        self.test_passed = True


