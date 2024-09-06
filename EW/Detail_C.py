from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from EW.to_import import acceptConsent, closeExponeaBanner, URL_detail, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import *

##global
terminyAcenyTabXpath_V1 = "//*[@id='terminyaceny-tab']"
terminyAcenyTabXpath_old = "//*[@class='f_bar-item f_tabBar']//*[contains(text(),'Termíny a ceny')]"
terminyAcenyTabXpath = "//*[@class='f_menu f_menu--inline f_menu--sticky']//*[contains(text(),'Termíny a ceny')]"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

#meal filter



valueToFilterStravaAllIncXpath_V1 = "//*[@id='filtr-stravy-detail']//*[contains(text(),'All inclusive')]"
#valueToFilterStravaAllIncXpath = "//*[@class='f_holder']//*[contains(text(),'All inclusive')]"
valueToFilterStravaAllIncXpath = "//*[@class='f_input--checkbox f_input']//*[@value=5]"





#airport filter
dopravaBoxXpath_V1 = "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']"
stravovaniBoxXpath = "//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--cutlery']"
stravaVterminechXpath = "//*[@class='f_icon f_icon--cutlery']"

dopravaBrnoXpath = "//*[@class='f_filterHolder f_set--active']//*[@value='4305']"
dopravaBoxXpath ="//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"
zvolenaStravaVboxuXpath = "//*[@class='f_button-content f_icon f_icon--cutlery']//*[@class='f_button-text f_text--highlighted']"
celkoveCenaVterminechXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_price pl-1 min-[1101px]:pl-0']"


from EW.to_import import URL_local
class TestDetailHotelu_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def omlouvamese_paragraph(self):
        time.sleep(1)
        try:
            omlouvameParagraph = self.driver.find_element_by_xpath(
                "//*[@class='fshr-paragraph fshr-paragraph--centered']")
            if omlouvameParagraph.is_displayed():
                return

        except NoSuchElementException:
            pass

    def test_detail_price_sorter_terminy_expensive(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)


        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(3.5)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(4)
        celkovaCenaSorterAfterOneClickXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor f_set--active f_icon--sortUp']"
        celkovaCenaSorterAfterOneClickElement = driver.find_element_by_xpath(celkovaCenaSorterAfterOneClickXpath)

        celkovaCenaSorterAfterOneClickElement.click()
        time.sleep(5)
        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:

            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        self.logger.info(celkoveCenyList)

        time.sleep(3)
        # cheap = "expensive"
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "expensive")

    def test_detail_price_sorter_terminy_cheap(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)
        driver = self.driver
        time.sleep(4)
        acceptConsent(driver)


        terminyAcenyElement = driver.find_element_by_xpath(terminyAcenyTabXpath)
        driver.execute_script("arguments[0].scrollIntoView();", terminyAcenyElement)
        time.sleep(2)
        terminyAcenyElement.click()
        boxTerminyXpath = "//*[@class='f_holder']"
        boxTerminyElement = driver.find_element_by_xpath(boxTerminyXpath)
        driver.execute_script("arguments[0].scrollIntoView();", boxTerminyElement)
        time.sleep(4)

        celkovaCenaSorterXpath = "//*[@class='f_termList-header-item f_termList-header-item--price']//*[@class='f_anchor f_icon f_icon_set--right f_icon_set--inheritColor']"
        celkovaCenaSorterElement = driver.find_element_by_xpath(celkovaCenaSorterXpath)
        ##2x click = od nejrdazshi
        ##1x click = od nejlevnejsiho

        celkovaCenaSorterElement.click()
        time.sleep(5)

        ##at this point kliknuto na sorter, need to take all of them and sort and compare lists / values

        ##elemenet vypada jako "41 276 Kč"
        ##odstranit menu na konci (parametr def by culture how long it is) + normalize space = should be int
        "38 764 Kč"

        pocetTerminuXpath = "//*[@class='f_termList-header-item']"
        pocetTerminuElements = driver.find_elements_by_xpath(pocetTerminuXpath)
        poziceTerminu = 0
        celkoveCenyList = []
        for _ in pocetTerminuElements:

            celkoveCenaVterminechElements = driver.find_elements_by_xpath(celkoveCenaVterminechXpath)
            kcIndex = 2
            celkovaCenaVterminechINT = celkoveCenaVterminechElements[poziceTerminu].text[:-kcIndex].replace(" ", "")
            celkovaCenaVterminechINT = int(celkovaCenaVterminechINT)
            celkoveCenyList.append(celkovaCenaVterminechINT)
            poziceTerminu = poziceTerminu + 1
        self.logger.info(celkoveCenyList)

        time.sleep(3)
        generalized_price_sorter_expensive_cheap_assert(celkoveCenyList, "cheap")
    def test_detail_fotka(self):

        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        time.sleep(1.5)

        acceptConsent(self.driver)

        time.sleep(5)
       # imageDetailXpath =  '//*[@id="pageContent"]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[2]/div[3]/swiper-container/swiper-slide[1]/img'
        imageDetailXpath = "/html/body/section/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/swiper-container/swiper-slide[1]/img"
        #imageDetail = self.driver.find_element_by_xpath( "//*[@aria-roledescription='carousel']//*[@class='splide__slide is-active is-visible']//img")
        imageDetail = self.driver.find_element_by_xpath(imageDetailXpath)

        imageDetailSrc = imageDetail.get_attribute("src")
        try:
            self.driver.set_page_load_timeout(5)
            self.driver.get(imageDetailSrc)
        except TimeoutException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  TimeoutException " + url
            sendEmail(msg)

        try:
            # time.sleep(5)
            image = self.driver.find_element_by_xpath("/html/body/img")
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

        time.sleep(5)
        acceptConsent(self.driver)
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        stravovaniBoxXpath,
                                                                        valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath(zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        self.logger.info(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)
        self.test_passed = True

    def test_detail_terminy_filtr_airport(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail}"
        self.driver.get(URL_detail_lp)

        time.sleep(1)
        acceptConsent(self.driver)

        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        dopravaBoxXpath, dopravaBrnoXpath, True)
        time.sleep(4)
        pocetZobrazenychTerminuXpath = "//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "brno"

        time.sleep(5)
        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath,
                                           departureToCompareTo, True)

        time.sleep(0.2)
        self.test_passed = True
