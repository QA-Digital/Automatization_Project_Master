from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

from ND_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from ND_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL, URL_leto, URL_zima, setUp, tearDown, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from ND_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from ND_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check, generalized_list_of_url_checker

URL_deploying_web = URL
URL_prod_public = "https://new.nev-dama.cz/"
banneryXpath_EW = "//*[@class='f_teaser-item']/a"

HPvyhledatZajezdyButtonXpath = "//div[@class='f_filterMainSearch-content']//div[6]"
HPkamPojedeteButtonXpath = "//div[normalize-space()='Destinace']"
HPzlutakRakouskoDestinaceXpath = "(//span[@class='!flex gap-2 items-center'])[71]"
HPzlutakChorvatskoDestinaceXpath = "(//span)[94]"
HPzlutakPokracovatButtonXpath = "//div[@class='f_filterHolder js_filterHolder f_set--active']//a[@class='f_button f_button--common']"
HPzlutakPokracovatButtonXpathStep3 ="//div[@class='f_filterHolder js_filterHolder f_set--active']//a[@class='f_button f_button--common']"
HPzlutakStravovaniPokracovat = "//div[@class='f_filterHolder js_filterHolder f_set--active']//a[@class='f_button f_button--common']"
HPzlutakObsazenost2plus1Xpath = "//*[contains(text(), 'Rodina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potvrdit a vyhledat')]"
HPnejlepsiZajezdySwitchButtonXpath = "//*[@class='f_switch-button']"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"


class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True


    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(3)
        acceptConsent(self.driver)
        time.sleep(8)
        self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakChorvatskoDestinaceXpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath).click()
        time.sleep(5)
        element = self.driver.find_element_by_xpath("//div[@class='f_filterHolder js_filterHolder f_set--active']//a[@class='f_button f_button--common']")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep3).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakStravovaniPokracovat).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath).click()
        time.sleep(0.5)
        self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath).click()

        SRL_D(self, self.driver)
        self.test_passed = True


    def test_HP_bannery_check_leto(self):

        self.driver.get(URL_leto)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 1500)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1)

        banneryXpath = self.driver.find_element_by_xpath("//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']")
        banneryElements = self.driver.find_elements_by_xpath("//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']")
        banneryElement = banneryElements[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", banneryElement)
        time.sleep(4)
        linksToCheck_List = []
        pozice = 0
        for _ in banneryElements:
            odkazLink = banneryElements[pozice].get_attribute("href")
            linksToCheck_List.append(odkazLink)
            print(odkazLink)
            pozice = pozice + 1

        generalized_list_of_url_checker(linksToCheck_List)

    def test_HP_bannery_check_zima(self):

        self.driver.get(URL_zima)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 1500)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1)

        banneryXpath = self.driver.find_element_by_xpath("//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']")
        banneryElements = self.driver.find_elements_by_xpath("//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']")
        banneryElement = banneryElements[0]
        self.driver.execute_script("arguments[0].scrollIntoView();", banneryElement)
        time.sleep(4)
        linksToCheck_List = []
        pozice = 0
        for _ in banneryElements:
            odkazLink = banneryElements[pozice].get_attribute("href")
            linksToCheck_List.append(odkazLink)
            print(odkazLink)
            pozice = pozice + 1

        generalized_list_of_url_checker(linksToCheck_List)

    def test_oblibene_destinace(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 1500)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1)

        oblibeneDestinaceXpath = "//*[@data-id-country]"
        try:
            oblibeneDestinace = self.driver.find_element_by_xpath(oblibeneDestinaceXpath)
            oblibeneDestinaceAll = self.driver.find_elements_by_xpath(oblibeneDestinaceXpath)
            wait.until(EC.visibility_of(oblibeneDestinace))
            if oblibeneDestinace.is_displayed():
                for WebElement in oblibeneDestinaceAll:
                    jdouVidet = WebElement.is_displayed()
                    assert jdouVidet == True
                    if jdouVidet == True:
                        pass

                    else:
                        url = self.driver.current_url
                        msg = "Problem s destinacemi, nezobrazuji se " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem s destinacemi, nezobrazuji se " + url
            sendEmail(msg)
        assert oblibeneDestinace.is_displayed() == True

