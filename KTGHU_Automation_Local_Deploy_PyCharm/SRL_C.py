from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from KTGHU_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, closeExponeaBanner, URL_SRL, sendEmail, setUp, tearDown, generalDriverWaitImplicit
import time
from selenium.webdriver.support import expected_conditions as EC
import unittest
from generalized_test_functions import generalized_map_test_click_through_circles, generalized_map_test_click_on_pin_and_hotel_bubble, generalized_SRL_choose_meal_filter_EW_like, generalized_list_string_sorter, generalized_SRL_price_sorter

hotelyKartyXpath = "//*[@class='f_tile-item f_tile-item--content']"
cenaZajezduXpath = "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']"
sorterCheapXpath = "//*[@class='f_tabBar-text' and contains(text(), 'Rendezés - a legolcsóbb elöl')]"
sorterExpensiveXpath = "//*[@class='f_tabBar-text' and contains(text(), 'Rendezés - a legdrágább elöl')]"

class Test_SRL_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_SRL_sort_cheapest(self):
        self.driver.maximize_window()
        self.driver.get(URL_SRL)

        time.sleep(2)

        acceptConsent(self.driver)
        time.sleep(1.5)

        typeOfSort = "cheap"

        generalized_SRL_price_sorter(self.driver, sorterCheapXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort)

        self.test_passed = True

    def test_SRL_sort_expensive(self):
        driver = self.driver
        self.driver.maximize_window()

        driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(4)

        typeOfSort = "expensive"

        generalized_SRL_price_sorter(self.driver, sorterExpensiveXpath, hotelyKartyXpath, cenaZajezduXpath, typeOfSort)

        self.test_passed = True

    def test_SRL_map(self):
        driver = self.driver
        driver.maximize_window()

        driver.get(URL_SRL)

        acceptConsent(driver)
        time.sleep(2)
        generalDriverWaitImplicit(self.driver)
        zobrazitNaMapeXpath = "//*[@class='f_bar-item f_bar-map']"
        # zobrazitNaMape.click()
        generalized_map_test_click_through_circles(driver, zobrazitNaMapeXpath)
        time.sleep(2.5)

        generalized_map_test_click_on_pin_and_hotel_bubble(driver)
        time.sleep(3)

        self.driver.switch_to.window(self.driver.window_handles[1])  ##gotta switch to new window
        currentUrl = self.driver.current_url
        print(currentUrl)
        print(URL_SRL)
        assert currentUrl != URL_SRL

        self.test_passed = True

    def test_SRL_filtr_strava(self):
        driver = self.driver
        driver.maximize_window()
        driver.get(URL_SRL)
        time.sleep(2)
        acceptConsent(driver)
        time.sleep(2)

        wait = WebDriverWait(driver, 30)
        rozbalitFiltrStravyXpath = "//*[contains(text(),'Kedvenc étel')]"
        rozbalitFiltrStravy = self.driver.find_element_by_xpath(rozbalitFiltrStravyXpath)

        rozbalitFiltrStravy.click()

        stravaMenuXpath = "//div[@class='f_additionalFilter-item f_set--opened']//div//span[@class='f_input-content']"
        generalized_SRL_choose_meal_filter_EW_like(driver, stravaMenuXpath)

        stravaZajezduSrlXpath = "//*[@class='f_list-item f_icon f_icon--cutlery']"
        assertion_strava = "all inclusive"
        generalized_list_string_sorter(driver, stravaZajezduSrlXpath, assertion_strava)

        self.test_passed = True

    def test_srl_C(self):
        x = 0  ##variable for taking the first hotel, starting at 0
        windowHandle = 1  ##variable for handling windows, gotta start on 1
        self.driver.maximize_window()
        self.driver.get(URL_SRL)
        wait = WebDriverWait(self.driver, 35)

        time.sleep(2)
        acceptConsent(self.driver)
        time.sleep(2)
        closeExponeaBanner(self.driver)
        hotelyAllKarty = self.driver.find_elements_by_xpath(hotelyKartyXpath)
        wait.until(EC.visibility_of(hotelyAllKarty[1]))
        for _ in range(7):

            print("|||||HOTEL CISLO|||||||" )
            print(x+1)
            print(x + 1)
            print(x + 1)
            terminZajezdu = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")
            terminZajezduSingle = self.driver.find_element_by_xpath(
                "//*[@class='f_tile f_tile--searchResultTour']//*[@class='f_list-item']")

            wait.until(EC.visibility_of(terminZajezduSingle))
            ##print(terminZajezdu[x].text)

            linkDetail = self.driver.find_elements_by_xpath("//*[@class='f_tile-priceDetail-item']/a")
            linkDetailActualUrl = linkDetail[x].get_attribute("href")
            ##print(linkDetailActualUrl)

            stravaZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--cutlery']")
            stravaZajezduString = stravaZajezdu[x].text

            pokojZajezdu = self.driver.find_elements_by_xpath("//*[@class='f_list-item f_icon f_icon--bed']")
            pokojZajezduString = pokojZajezdu[x].text
            ##print(pokojZajezduString)

            cenaZajezduAll = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-content']//*[@class='f_price']")
            cenaZajezduAllString = cenaZajezduAll[x].text.lower()
            ##print(cenaZajezduAllString)

            cenaZajezduAdult = self.driver.find_elements_by_xpath(
                "//*[@class='f_tile-priceDetail-item']//*[@class='f_tile-priceDetail-note'] //*[@class='f_price']")
            cenaZajezduAdultString = cenaZajezduAdult[x].text.lower()
            print(cenaZajezduAdultString)

            self.driver.execute_script("window.open("");")
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.get(linkDetailActualUrl)

            closeExponeaBanner(self.driver)

            time.sleep(1)  ##natvrdo aby se to neposralo

            #detailTerminSedivka = self.driver.find_element_by_xpath("//*[@class='fshr-detail-summary-title']")
            ##print(detailTerminSedivka.text)

            # detailStravaSedivka = self.driver.find_elements_by_xpath("//*[@class='fshr-detail-summary-paragraph']")
            # detailStravaSedivkaString = detailStravaSedivka[
            #     1].text  ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully

            try:
                detailStravaSedivka = self.driver.find_element_by_xpath(
                    "//*[@class='f_icon f_icon--cutlery before:mr-1 before:text-neutral-400']")
            except NoSuchElementException:
                try:
                    detailStravaSedivka = self.driver.find_element_by_xpath(
                        "/html/body/section/div/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/span")
                except NoSuchElementException:
                    pass

                # detailStravaSedivkaString = detailStravaSedivka[1].text  ##gottaa be 1 cuz thats how its set up (multiple locators are attached to this locator so position 1 is always gonna be strava hopefully
            detailStravaSedivkaString = detailStravaSedivka.text
            print(detailStravaSedivkaString)

            detailPokojSedivka = self.driver.find_element_by_xpath(
                "//*[@class='f_box-item f_icon f_icon--bed']//strong")
            detailPokojSedivkaString = detailPokojSedivka.text

            # detailPokojSedivka = self.driver.find_element_by_xpath(
            #     "//*[@class='fshr-detail-summary-title fshr-icon fshr-icon--bed']")
            # detailPokojSedivkaString = detailPokojSedivka.text
            # detailPokojSedivkaString = detailPokojSedivkaString[:-3]  ##need to be edited cuz there is random spaces and "?" in the element
            # ##print(detailPokojSedivkaString)

            # detailCenaAll = self.driver.find_element_by_xpath("//*[@class='fshr-tooltip-underline js-totalPrice']")
            # detailCenaAllString = detailCenaAll.text
            # ##print(detailCenaAllString)

            detailCenaAll = self.driver.find_element_by_xpath("//*[@class='f_column-item']//*[@class='f_price']")
            detailCenaAllString = detailCenaAll.text.lower()

            # detailCenaAdult = self.driver.find_element_by_xpath(
            #         '//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
            # detailCenaAdultString = detailCenaAdult.text.lower()
            # print(detailCenaAdultString)

            try:
                # detailCenaAdult = self.driver.find_element_by_xpath('//*[contains(concat(" ", normalize-space(@class), " "), " fshr-detail-summary-price-header ")]//*[contains(concat(" ", normalize-space(@class), " "), " fshr-price ")]')
                # detailCenaAdult = self.driver.find_element_by_xpath("//*[@class='flex justify-between']//*[@class='text-right bold']")
                detailCenaAdult = self.driver.find_element_by_xpath(
                    "//*[@class='flex justify-between mb-2']//*[@class='text-right bold']")
                detailCenaAdultString = detailCenaAdult.text.lower()
                print(detailCenaAdultString)

            except NoSuchElementException:
                pass


            assert detailPokojSedivkaString == pokojZajezduString
            self.driver.close()

            if detailPokojSedivkaString == pokojZajezduString:
                print("pokoje sedi srl vs detail")
            else:
                print(" NESEDÍ pokoj SRL vs sedivka")

            assert detailStravaSedivkaString == stravaZajezduString
            if detailStravaSedivkaString == stravaZajezduString:
                print("stravy sedi srl vs detail")

            else:
                print("NESEDÍ strava srl vs ssedika")
            assert detailCenaAllString == cenaZajezduAllString
            if detailCenaAllString == cenaZajezduAllString:
                print("ceny all sedi srl vs detail")

            else:
                print("ceny all NESEDÍ srl vs detail")

            assert detailCenaAdultString == cenaZajezduAdultString

            if detailCenaAdultString == cenaZajezduAdultString:
                print(" cena adult sedi srl vs detail")

            else:
                print("cena adult NESEDÍ srl vs detail")

            self.driver.switch_to.window(
                self.driver.window_handles[0])  ##this gotta be adjusted based on what test is executed
            ##for daily test needs to be set on 1 so it gets on the SRL

            x = x + 1
            print(x)
            windowHandle = windowHandle + 1
            print(windowHandle)

            self.test_passed = True
