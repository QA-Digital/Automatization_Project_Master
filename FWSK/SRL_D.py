from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from FWSK.to_import import acceptConsent, sendEmail, URL_SRL, setUp, tearDown
from selenium.webdriver.support import expected_conditions as EC
import unittest

from helpers.helper import Helpers

SRLhotelyKartyXpath = "//*[@class='f_tile-item f_tile-item--content']"
#SRLfotkyKartyXpath = "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_tileGallery']"
SRLfotkyKartyXpath = "//*[@class='f_searchResult-content'and not(@style='display: none;')]//*[@class='f_tileGallery']"
#SRLcenaKartyXpath = "//*[@class='f_searchResult'and not(@style='display: none;')]//*[@class='f_price']"

#SRLhotelyKartyXpath = "//*[@class='f_searchResult-content-item']"
#SRLfotkyKartyXpath = "//*[@class='f_tileGallery']"
SRLcenaKartyXpath = "//*[@class='f_price']"


def SRL_D(self, driver):
    wait = WebDriverWait(self.driver, 15)
    driver.implicitly_wait(100)
    hotelySingle = self.driver.find_element(By.XPATH, SRLhotelyKartyXpath)
    try:
        hotelySingle = self.driver.find_element(By.XPATH, SRLhotelyKartyXpath)  ##
        hotelyAll = self.driver.find_elements(By.XPATH, SRLhotelyKartyXpath)
        wait.until(EC.visibility_of(hotelySingle))
        ##print(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                print(jdouvidet)
                assert jdouvidet == True
                if jdouvidet == True:
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s hotely v searchi - hotelCard " + url
                    sendEmail(msg)
    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s hotely v searchi - hotelCard " + url
        sendEmail(msg)

    assert hotelySingle.is_displayed() == True

    # try:
    #     self.driver.implicitly_wait(15)
    #     fotkyAll = self.driver.find_elements(By.XPATH, SRLfotkyKartyXpath)  ##
    #     fotkaSingle = self.driver.find_element(By.XPATH, SRLfotkyKartyXpath)
    #     wait.until(EC.visibility_of(fotkaSingle))
    #     ##print(fotkaSingle)
    #     if fotkaSingle.is_displayed():
    #         for WebElement in fotkyAll:
    #             jdouvidet = WebElement.is_displayed()
    #             print(jdouvidet)
    #             assert jdouvidet == True
    #             if jdouvidet == True:
    #                 pass
    #             else:
    #                 url = self.driver.current_url
    #                 msg = " Problem s fotkami hotelu v searchi " + url
    #                 sendEmail(msg)
    #
    # except NoSuchElementException:
    #     url = self.driver.current_url
    #     msg = " Problem s fotkami hotelu v searchi " + url
    #     sendEmail(msg)

    try:
        loadingImgSingle = self.driver.find_element_by_xpath(
            "//*[@class='splide__spinner']")  ##loading classa obrazku, jestli tam je = not gud
        if loadingImgSingle.is_displayed():
            url = self.driver.current_url
            msg = " Problem s načítáná fotek v SRL  //*[@class='splide__spinner']" + url
            sendEmail(msg)
            assert 1 == 2
    except NoSuchElementException:
        pass

    try:
        self.driver.implicitly_wait(100)
        cenaAll = self.driver.find_elements(By.XPATH, SRLcenaKartyXpath)  ##
        cenaSingle = self.driver.find_element(By.XPATH, SRLcenaKartyXpath)
        wait.until(EC.visibility_of(cenaSingle))
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                assert jdouvidet == True
                if jdouvidet == True:
                    print("ceny")
                    pass

                else:
                    url = self.driver.current_url
                    msg = " Problem s cenami hotelu v searchi " + url
                    sendEmail(msg)


    except NoSuchElementException:
        url = self.driver.current_url
        msg = "Problem s cenami hotelu v searchi " + url
        sendEmail(msg)

    assert cenaAll[0].is_displayed() == True

from FWSK.to_import import URL_local
class TestSRL_D(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_SRL_D(self):
        self.driver.maximize_window()
        URL_SRL_lp = f"{self.URL}{URL_SRL}"
        self.driver.get(URL_SRL_lp)

        acceptConsent(self.driver)
        Helpers.search_results_list_check(self.driver, self.logger)

        self.test_passed = True
