from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from FWSK.to_import import acceptConsent, URL_detail, sendEmail, setUp, tearDown, URL_detail_new
import time
import unittest
from generalized_test_functions import generalized_Detail_terminyAceny_potvrdit_chooseFiltr, \
    generalized_list_string_sorter, generalized_detail_departure_check, \
    generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail

##global
terminyAcenyTabXpath_V1 = "//*[@id='terminyaceny-tab']"
terminyAcenyTabXpath_old = "//*[@class='f_bar-item f_tabBar']//*[contains(text(),'Termíny a ceny')]"
#terminyAcenyTabXpath = "//*[@class='f_bar-item f_tabBar']//*[contains(text(),'Termíny a ceny')]"
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
dopravaBratislavaXpath = "//*[@class='f_filterHolder f_set--active']//*[@value='4312']"
dopravaBoxXpath ="//*[@class='f_holder']//*[@class='f_button-content f_icon f_icon--plane']"

from FWSK.to_import import URL_local
class TestDetailHotelu_C(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None, run_number=None):
        self.run_number = run_number
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_detail_fotka(self):
        self.driver.maximize_window()
        URL_detail_lp = f"{self.URL}{URL_detail_new}"
        self.driver.get(URL_detail_lp)

        acceptConsent(self.driver)

        time.sleep(10)
        imageDetailXpath = "//div[@class='grid grid-cols-4 grid-rows-2 gap-2 rounded-[--galleryImageRadius] overflow-hidden']//div[1]//img[1]"
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
            # time.sleep(5)
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
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        stravovaniBoxXpath,
                                                                        valueToFilterStravaAllIncXpath, False)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element(By.XPATH, zvolenaStravaVboxuXpath)
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
        # TODO na box pro filtrace je v generalized test fncs to tam kliká fixně na valu 2 asi k tomu byl nejaky duvod
        # TODO ale na fwsk ted neni nic z kosic takze to nejde filtrofvat takze tohle nebude fungovat
        # TODO asi podminka pro sk kde se klikne fixne na xpath te volby jako je ted definovana dopravaBratislavaXpath
        # TODO pokud nebude vyplneny parametr ve funkci proste se to passne
        generalized_Detail_terminyAceny_potvrdit_chooseFiltr_new_detail(self.driver, terminyAcenyTabXpath,
                                                                        dopravaBoxXpath, dopravaBratislavaXpath, True)
        time.sleep(4)
        pocetZobrazenychTerminuXpath = "//*[@class='f_termList-header-item f_termList-header-item--dateRange']"
        odletyTerminyXpath = "//*[@class='f_termList-header-item f_termList-header-item--transport']"
        departureToCompareTo = "praha"

        time.sleep(5)
        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath,
                                           departureToCompareTo, True)

        time.sleep(0.2)
        self.test_passed = True
