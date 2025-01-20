from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from FW.to_import import acceptConsent, URL_detail, sendEmail, setUp, tearDown, URL_detail_old
import time
import unittest
from generalized_test_functions import generalized_Detail_terminyAceny_potvrdit_chooseFiltr, generalized_list_string_sorter, generalized_detail_departure_check, generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail
#from generalized_test_functions import generalized_price_sorter_expensive_cheap_assert
##global
terminyAcenyTabXpath_V1 = "//*[@id='terminyaceny-tab']"
terminyAcenyTabXpath_old = "//*[@class='f_bar-item f_tabBar']//*[contains(text(),'Termíny a ceny')]"
terminyAcenyTabXpath = "//*[@class='f_menu f_menu--inline f_menu--sticky']//*[contains(text(),'Termíny a ceny')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

#meal filter
stravovaniBoxXpath_V1 = "//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']"
stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"

valueToFilterStravaAllIncXpath_V1 = "//*[@id='filtr-stravy-detail']//*[contains(text(),'All inclusive')]"
#valueToFilterStravaAllIncXpath = "//*[@class='f_holder']//*[contains(text(),'All inclusive')]"
valueToFilterStravaAllIncXpath = "//*[@class='f_input--checkbox f_input']//*[@value=5]"

zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"

stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"

#airport filter
dopravaBoxXpath_V1 = "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']"
dopravaBrnoXpath_V1 = "//*[@data-value='4305']"
dopravaBrnoXpath_V12 = "//*[@class='f_filterHolder f_set--active']//*[@class='f_input--checkbox f_input']"
dopravaBrnoXpath = "//*[@class='f_filterHolder f_set--active']//*[@value='4312']"
dopravaBoxXpath ="//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"

celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 min-[1101px]:pl-0']"

from FW.to_import import URL_local
from helpers.helper import *
class TestDetailHotelu_C(unittest.TestCase):

    URL = URL_local  # Default value
    def __init__(self, methodName, URL=None, run_number=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL
        self.run_number = run_number

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_detail_price_sorter_terminy_expensive(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_old}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        acceptConsent(driver)
        time.sleep(4)

        terminyAcenyElement = driver.find_element(By.XPATH, terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element(By.XPATH, boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element(By.XPATH, celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(4)
        celkovaCenaSorterAfterOneClickXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterAfterOneClickElement = driver.find_element(By.XPATH, celkovaCenaSorterAfterOneClickXpath)

        celkovaCenaSorterAfterOneClickElement.click()
        time.sleep(5)
        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements(By.XPATH, pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechElements = driver.find_elements(By.XPATH, celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        self.logger.info(celkoveCenyList)

        time.sleep(3)
        #cheap = "expensive"
        Helpers.generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "expensive", self.logger)

    def test_detail_price_sorter_terminy_cheap(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_old}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        acceptConsent(driver)
        time.sleep(4)

        terminyAcenyElement = driver.find_element(By.XPATH, terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element(By.XPATH, boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element(By.XPATH, celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(5)

        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements(By.XPATH, pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:
            celkoveCenaVterminechElements = driver.find_elements(By.XPATH, celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        self.logger.info(celkoveCenyList)

        time.sleep(3)
        Helpers.generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap", self.logger)

    def test_detail_fotka(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_old}"
        self.driver.get(URL_detail_lp)

        acceptConsent(self.driver)

        time.sleep(10)
        imageDetailXpath = '/html[1]/body[1]/section[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[4]/swiper-container[1]/swiper-slide[1]/img[1]'
        imageDetail = self.driver.find_element(By.XPATH, imageDetailXpath)
        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            #time.sleep(5)
            image = self.driver.find_element(By.XPATH, "/html/body/img")
            assert image.is_displayed() == True
            if image.is_displayed():
                self.logger.info("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

        self.test_passed = True
    def test_detail_terminy_filtr_meal(self):
        self.driver.maximize_window()
        time.sleep(1)
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        time.sleep(1)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,stravovaniBoxXpath, valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element(By.XPATH, zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        self.logger.info(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True

    def test_detail_terminy_filtr_airport(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_old}"
        self.driver.get(URL_detail_lp)

        time.sleep(1)
        acceptConsent(self.driver)

        Helpers.generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath, dopravaBoxXpath, dopravaBrnoXpath, "airport", self.logger)
        time.sleep(4)
        pocetZobrazenychTerminuXpath="//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "praha"

        time.sleep(5)
        Helpers.generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath, departureToCompareTo, self.logger)

        time.sleep(0.2)
        self.test_passed = True

