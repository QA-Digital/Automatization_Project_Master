from selenium.common.exceptions import NoSuchElementException, TimeoutException
from FWSK_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, URL_detail, sendEmail, setUp, tearDown
import time
import unittest
from generalized_test_functions import generalized_Detail_terminyAceny_potvrdit_chooseFiltr, generalized_list_string_sorter, generalized_detail_departure_check

##global
terminyAcenyTabXpath = "//*[@id='terminyaceny-tab']"
potvrditPopupXpath = "//*[@data-testid='popup-closeButton']"

#meal filter
stravovaniBoxXpath= "//*[@class='fshr-button-content fshr-icon fshr-icon--forkSpoon js-selector--catering']"
valueToFilterStravaAllIncXpath = "//*[@id='filtr-stravy-detail']//*[contains(text(),'All inclusive')]"
zvolenaStravaVboxuXpath = "//*[@class='js-subvalue f_text--highlighted']"
stravaVterminechXpath = "//*[@class='fshr-termin-catering js-tooltip js-tooltip--onlyDesktop']"

#airport filter
dopravaBoxXpath = "//*[@class='fshr-button-content fshr-icon fshr-icon--plane js-selector--travel']"
dopravaKosiceXpath = "//*[@data-value='1837']"
testss=0

class TestDetailHotelu_C(unittest.TestCase):
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

    def test_detail_fotka(self):
        self.driver.maximize_window()
        self.driver.get(URL_detail)

        acceptConsent(self.driver)

        time.sleep(10)
        imageDetail = self.driver.find_element_by_xpath(
            "//*[@aria-roledescription='carousel']//*[@class='splide__slide is-active is-visible']//img")
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
                print("its ok")
        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s fotkou src, detailhotelu,  NoSuchElementException " + url
            sendEmail(msg)

        self.test_passed = True

    def test_detail_terminy_filtr_meal(self):
        self.driver.maximize_window()

        def omlouvamese_paragraph(self):
            time.sleep(1)
            try:
                omlouvameParagraph = self.driver.find_element_by_xpath(
                    "//*[@class='fshr-paragraph fshr-paragraph--centered']")
                if omlouvameParagraph.is_displayed():
                    return

            except NoSuchElementException:
                pass

        self.driver.get(URL_detail)

        time.sleep(1)
        acceptConsent(self.driver)

        generalized_Detail_terminyAceny_potvrdit_chooseFiltr(self.driver, terminyAcenyTabXpath, potvrditPopupXpath,
                                                             stravovaniBoxXpath, valueToFilterStravaAllIncXpath)
        time.sleep(1.2)

        zvolenaStravaVboxu = self.driver.find_element_by_xpath(zvolenaStravaVboxuXpath)
        zvolenaStravaVboxuString = zvolenaStravaVboxu.text.lower()
        print(zvolenaStravaVboxuString)

        generalized_list_string_sorter(self.driver, stravaVterminechXpath, zvolenaStravaVboxuString)

        self.test_passed = True

    def test_detail_terminy_filtr_airport(self):
        self.driver.maximize_window()


        self.driver.get(URL_detail)

        time.sleep(1)
        acceptConsent(self.driver)

        generalized_Detail_terminyAceny_potvrdit_chooseFiltr(self.driver, terminyAcenyTabXpath, potvrditPopupXpath,
                                                             dopravaBoxXpath, dopravaKosiceXpath)

        time.sleep(5)

        pocetZobrazenychTerminuXpath = "//*[@class='fshr-termins-table-item-header js-toggleSlide']"
        odletyTerminyXpath = "//*[@class='fshr-termin-departure-from']"
        departureToCompareTo = "košice"

        generalized_detail_departure_check(self.driver, pocetZobrazenychTerminuXpath, odletyTerminyXpath,
                                           departureToCompareTo, False)

        time.sleep(0.2)
        self.test_passed = True