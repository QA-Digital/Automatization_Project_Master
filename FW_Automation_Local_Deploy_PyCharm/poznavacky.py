import time
from FW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_poznavacky, URL_poznavacky_vikendy, URL_poznavacky_rodiny, URL_poznavacky_zazitky, setUp, tearDown, generalDriverWaitImplicit
import unittest
from sedivka_check import sedivka_check_assert
sedivkaXpathFw = "//*[@class='f_box h-full flex flex-col']"
kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"

def poznavacky_check_D(self, driver):

    generalDriverWaitImplicit(self.driver)
    generalDriverWaitImplicit(self.driver)

    imgs = self.driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
    #self.driver.execute_script("arguments[0].scrollIntoView();", kartyHoteluBottom)
    print(imgs)
    x = 0
    assert imgs[0].is_displayed() == True
    for _ in imgs:
        imgsDisplayed = imgs[x].is_displayed()
        x = x + 1

        assert imgsDisplayed == True
        print("true imgdisplay")

    gridItems = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid-item']")
    self.driver.execute_script("arguments[0].scrollIntoView();", gridItems[0])
    assert gridItems[0].is_displayed() == True
    y = 0
    for _ in gridItems:
        gridItemDisplayed = gridItems[y].is_displayed()
        assert gridItemDisplayed == True
        y = y + 1
        print("grid true")

    gridBig = self.driver.find_elements_by_xpath("//*[@class='f_tileGrid']")
    a = 0
    assert gridBig[0].is_displayed() == True
    for _ in gridBig:
        gridBigDisplayed = gridBig[a].is_displayed()
        assert gridBigDisplayed == True
        a = a + 1
        print("big grid ture")

def proklik_kostkaHotelu_toDetail_check_sedivka(driver):
            element = driver.find_element_by_xpath(kostkaPoznavackaXpath)
            driver.execute_script("arguments[0].scrollIntoView();", element)
            time.sleep(2)
            element.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            print(driver.current_url)
            sedivka_check_assert(driver, sedivkaXpathFw)


class TestPoznavacky_D(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_poznavacky_okruzni_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky)
        acceptConsent(self.driver)
        time.sleep(3)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True

    def test_poznavacky_vikendy_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_vikendy)
        acceptConsent(self.driver)
        time.sleep(3)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True

    def test_poznavacky_rodiny_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_rodiny)
        acceptConsent(self.driver)
        time.sleep(3)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True

    def test_poznavacky_zazitky_D(self):
        self.driver.maximize_window()
        self.driver.get(URL_poznavacky_zazitky)

        acceptConsent(self.driver)
        time.sleep(3)
        poznavacky_check_D(self, self.driver)
        self.test_passed = True

    def test_poznavacky_okruzni_C(self):
        self.driver.get(URL_poznavacky)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(10)
        kostkaPoznavackaXpath = "//*[@class='f_tile f_tile--tour']"
        element3 = self.driver.find_elements_by_xpath(kostkaPoznavackaXpath)[6]
        self.driver.execute_script("arguments[0].scrollIntoView();", element3)
        time.sleep(2)
        element3.click()
        self.driver.switch_to.window(
            self.driver.window_handles[1])
        time.sleep(1)
        print(self.driver.current_url)
        sedivka_check_assert(self.driver, sedivkaXpathFw)
        self.test_passed = True

    def test_poznavacky_vikendy_C(self):
        self.driver.get(URL_poznavacky_vikendy)
        time.sleep(1)
        self.driver.maximize_window()
        acceptConsent(self.driver)
        time.sleep(5)
        proklik_kostkaHotelu_toDetail_check_sedivka(self.driver)

        self.test_passed = True