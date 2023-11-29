from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from EXPL_Automation_Local_Deploy_PyCharm.Detail_D import detail_D
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, acceptLetak, URL, URL_vlastniDoprava, setUp, tearDown,URL_leto, URL_zima, URL_egzotyka, URL_allInclusive, generalDriverWaitImplicit
import unittest
from selenium.webdriver.support import expected_conditions as EC
from EXPL_Automation_Local_Deploy_PyCharm.groupsearch_D import groupSearch_D
import time
from EXPL_Automation_Local_Deploy_PyCharm.SRL_D import SRL_D
from generalized_banners_compare_to_deploy_web import banner_check_public_prod_VS_deployed_web
#from generalized_test_functions import generalized_EW_like_top_nabidka_URL_status_check, generalized_list_of_url_checker
from EXPL_Automation_Local_Deploy_PyCharm.to_import import acceptConsent,URL_detail, sendEmail

URL_deploying_web = URL
URL_prod_public = "https://www.exim.pl/"
banneryXpath_EWPL = "//*[@class='f_teaser-item']/a"

HPvyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Szukaj'])[1]"
HPkamPojedeteButtonXpath = "//div[contains(text(),'Kierunek')]"
HPzlutakTurcjaDestinaceXpath= "//body[1]/header[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[1]/div[4]/div[1]/span[1]/label[1]/span[1]"
HPzlutakPokracovatButtonXpath = "(//span[contains(text(),'Kontynuuj')])[1]"
HPzlutakPokracovatButtonXpathStep2 ="(//span[contains(text(),'Kontynuuj')])[2]"
HPzlutakPokracovatVyberTerminuXpath = "//div[contains(text(),'Termin')]"
HPzlutakZima2024Xpath = "//span[contains(text(), 'Ferie zimowe 2024')]"
HPzlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Kontynuuj')])[3]"
HPzlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Rodzina 2+1')]"
HPzlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potwierdź i wyszukaj')]"
HPnejlepsiZajezdyVypisXpath = "//*[@class='f_tourTable-tour']"
HPnextArrowXpath = "//*[@class='slick-next slick-arrow']"
HPkartaHoteluSliderXpath = "//*[@class='f_carousel-item slick-slide slick-active']"

VyletyPoznan = "(//span[@class='f_button f_button--important'])[1]"
VyletyLublin = "(//span[@class='f_button f_button--important'])[2]"
VyletyGdansk = "(//span[@class='f_button f_button--important'])[3]"

banneryXpath = "//*[@class='f_tile f_tile--teaserDestination js-gtm-promotionClick']"
vyhledatZajezdyButtonXpath = "(//span[@class='f_button-text f_icon f_icon--chevronRight f_icon_set--right'][normalize-space()='Szukaj'])[1]"
kamPojedeteButtonXpath = "//div[contains(text(),'Kierunek')]"
zlutakPolskoDestinaceXpath= "(//span[@class='font-bold'][normalize-space()='Polska'])[1]"
zlutakPokracovatButtonXpath = "(//span[contains(text(),'Kontynuuj')])[1]"
zlutakPokracovatButtonXpathStep2 ="(//span[contains(text(),'Kontynuuj')])[2]"
zlutakPokracovatVyberTerminuXpath = "//div[contains(text(),'Termin')]"
zlutakZima2024Xpath = "//span[contains(text(), 'Ferie zimowe 2024')]"
zlutakPokracovatButtonXpathStep3 ="(//span[contains(text(),'Kontynuuj')])[3]"
zlutakObsazenost2plus1Xpath = "//div[contains(text(), 'Rodzina 2+1')]"
zlutakPotvrditAvyhledatXpath = "//*[@class='f_button f_button--common'] //*[contains(text(), 'Potwierdź i wyszukaj')]"

class Test_HP_C(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)


    def test_HP_zlutak_to_groupsearch_pobyt(self):
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPvyhledatZajezdyButtonXpath))).click()
        time.sleep(2.5)  ##time sleep not the best not pog but it works =)

        self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
        groupSearch_D(self, self.driver)
        self.test_passed = True

    def test_HP_zlutak_to_SRL_pobyt(self):
        self.driver.get(URL)
        self.driver.maximize_window()
        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(3.5)
        self.driver.find_element_by_xpath(HPkamPojedeteButtonXpath).click()
        self.driver.find_element_by_xpath(HPzlutakTurcjaDestinaceXpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep2).click()
        self.driver.find_element_by_xpath(HPzlutakZima2024Xpath).click()
        self.driver.find_element_by_xpath(HPzlutakPokracovatButtonXpathStep3).click()
        self.driver.find_element_by_xpath(HPzlutakObsazenost2plus1Xpath).click()
        self.driver.find_element_by_xpath(HPzlutakPotvrditAvyhledatXpath).click()

        SRL_D(self, self.driver)
        self.test_passed = True

    def test_HP_slider_click_detail_hotelu(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        wait = WebDriverWait(self.driver, 300)

        time.sleep(
            0.3)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)

        self.driver.implicitly_wait(100)

        HPnextArrowElement = self.driver.find_element_by_xpath(HPnextArrowXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPnextArrowElement)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.3)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", HPnextArrowElement)

        HPnextkartaHoteluSlider = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", HPnextkartaHoteluSlider)
        action = ActionChains(self.driver)
        HPkartaHoteluSliderElement = self.driver.find_element_by_xpath(HPkartaHoteluSliderXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", HPkartaHoteluSliderElement)
        action.move_to_element(HPkartaHoteluSliderElement).click().perform()
        self.driver.implicitly_wait(100)
        time.sleep(0.3)
        #HPkartaHoteluSliderElement.click()
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        detail_D(self, self.driver)

        self.test_passed = True

    def test_HP_bannery_check(self):
        banner_check_public_prod_VS_deployed_web(self.driver, URL_prod_public, URL_deploying_web, banneryXpath_EWPL)

        self.test_passed = True

    def test_HP_nabidka_Podroze_marzen(self):
        self.driver.maximize_window()
        self.driver.get(URL)

        time.sleep(2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
        acceptConsent(self.driver)
        time.sleep(1)

        Offer1 = self.driver.find_elements_by_xpath("(//a)[59]")[0].get_attribute('href')
        Offer2 = self.driver.find_elements_by_xpath("(//a)[60]")
        Offer3 = self.driver.find_elements_by_xpath("(//a)[61]")
        Offer4 = self.driver.find_elements_by_xpath("(//a)[62]")

        HPtopNabidkaElements = [Offer1, Offer2, Offer3, Offer4]
        print(HPtopNabidkaElements)
        time.sleep(4)
        linksToCheck_List = []
        for _ in HPtopNabidkaElements:
           odkazLink = HPtopNabidkaElements
           linksToCheck_List.append(odkazLink)
           print(odkazLink)

    def test_HP_vyletyPoznan(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyPoznanElement = self.driver.find_element_by_xpath(VyletyPoznan)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyPoznanElement)
        time.sleep(5)
        VyletyPoznanElement.click()

        try:
            destinationPoznan = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationPoznanAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationPoznan.is_displayed():
                for WebElement in destinationPoznanAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        print("Destinace jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationPoznan.is_displayed() == True

    def test_HP_vyletyLublin(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyLublinElement = self.driver.find_element_by_xpath(VyletyLublin)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyLublinElement)
        time.sleep(5)
        VyletyLublinElement.click()

        try:
            destinationLublin = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationLublinAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationLublin.is_displayed():
                for WebElement in destinationLublinAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        print("Destinace jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationLublin.is_displayed() == True

    def test_HP_vyletyGdansk(self):
        self.driver.maximize_window()
        self.driver.get(URL)
        time.sleep(2.5)
        acceptConsent(self.driver)
        time.sleep(1.5)

        VyletyGdanskElement = self.driver.find_element_by_xpath(VyletyGdansk)
        self.driver.execute_script("arguments[0].scrollIntoView();", VyletyGdanskElement)
        time.sleep(5)
        VyletyGdanskElement.click()

        try:
            destinationGdansk = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            destinationGdanskAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            if destinationGdansk.is_displayed():
                for WebElement in destinationGdanskAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        print("Destinace jdou videt")
                    else:
                        url = self.driver.current_url
                        msg = "Problem, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationGdansk.is_displayed() == True

    def test_letoDestination_D(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_leto)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationLeto = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationLeto)
            destinationLetoAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationLeto))
            if destinationLeto.is_displayed():
                for WebElement in destinationLetoAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Leto, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Leto, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationLeto.is_displayed() == True

    def test_zimaDestination_D(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_zima)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationZima = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationZima)
            destinationZimaAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationZima))
            if destinationZima.is_displayed():
                for WebElement in destinationZimaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Zima, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Zima, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationZima.is_displayed() == True

    def test_egzotykaDestination_D(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_egzotyka)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationEgzotyka = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationEgzotyka)
            destinationEgzotykaAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationEgzotyka))
            if destinationEgzotyka.is_displayed():
                for WebElement in destinationEgzotykaAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem Egzotyka, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem Egzotyka, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationEgzotyka.is_displayed() == True

    def test_allInclusiveDestination_D(self):
        wait = WebDriverWait(self.driver, 1500)
        self.driver.get(URL_allInclusive)
        self.driver.maximize_window()
        time.sleep(2.5)
        acceptConsent(self.driver)

        try:
            destinationAllIn = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            self.driver.execute_script("arguments[0].scrollIntoView();", destinationAllIn)
            destinationAllInAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(destinationAllIn))
            if destinationAllIn.is_displayed():
                for WebElement in destinationAllInAll:
                    jdouvidet = WebElement.is_displayed()
                    assert jdouvidet == True

                    if jdouvidet == True:
                        pass
                    else:
                        url = self.driver.current_url
                        msg = "Problem All Inclusive, destinace se nezobrazuji " + url
                        sendEmail(msg)

        except NoSuchElementException:
            url = self.driver.current_url
            msg = "Problem All Inclusive, destinace se nezobrazuji " + url
            sendEmail(msg)

        assert destinationAllIn.is_displayed() == True



# def test_HP_nejlepsi_nabidky_vypis_btn_switch(self):
#     self.driver.get(URL)
#     wait = WebDriverWait(self.driver, 300)
#     self.driver.maximize_window()
#     time.sleep(
#        2.5)  ##this is to workaround accept consent since in maximizes and then selenium gets confused with clickin on the element
#     acceptConsent(self.driver)
#     generalDriverWaitImplicit(self.driver)
#     wait.until(EC.visibility_of(self.driver.find_element_by_xpath(HPnejlepsiZajezdyVypisXpath)))
#     nejlepsiNabidkyElement = self.driver.find_elements_by_xpath(HPnejlepsiZajezdyVypisXpath)
#     positionOfCurrentElement = 0
#     nejlepsiNabidkyTextList = []
#     for _ in nejlepsiNabidkyElement:
#         nejlepsiNabidkyTextDefault = nejlepsiNabidkyElement[positionOfCurrentElement].text
#         nejlepsiNabidkyTextList.append(nejlepsiNabidkyTextDefault)
#         positionOfCurrentElement = positionOfCurrentElement + 1
#
#     print(nejlepsiNabidkyTextList)
#
#     self.test_passed = True


# class Test_Vlastni_Doprava(unittest.TestCase):
#     def setUp(self):
#         setUp(self)
#     def tearDown(self):
#         tearDown(self)
#
#     def test_Homepage_bannery(self):
#         self.driver.maximize_window()
#         self.driver.get(URL_vlastniDoprava)
#
#         time.sleep(2)
#         acceptConsent(self.driver)
#         time.sleep(1.5)
#
#         bannerSingle = self.driver.find_element_by_xpath(banneryXpath)
#         try:
#             bannerSingle = self.driver.find_element_by_xpath(banneryXpath)
#             bannerAll = self.driver.find_elements_by_xpath(banneryXpath)
#             if bannerSingle.is_displayed():
#                 for WebElement in bannerAll:
#                     jdouvidet = WebElement.is_displayed()
#                     assert jdouvidet == True
#                     if jdouvidet == True:
#                         pass
#                     else:
#                         url = self.driver.current_url
#                         msg = "Problem s bannery " + url
#                         sendEmail(msg)
#
#         except NoSuchElementException:
#             url = self.driver.current_url
#             msg = "Problem s bannery " + url
#             sendEmail(msg)
#         assert bannerSingle.is_displayed() == True
#
#     def test_Destination_isDisplayed(self):
#         wait = WebDriverWait(self.driver, 1500)
#         self.driver.get(URL_vlastniDoprava)
#         self.driver.maximize_window()
#         time.sleep(2.5)
#         acceptConsent(self.driver)
#
#         try:
#             destination = self.driver.find_element_by_xpath("//*[@class='f_teaser-item']")
#             self.driver.execute_script("arguments[0].scrollIntoView();", destination)
#             destinationAll = self.driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
#             wait.until(EC.visibility_of(destination))
#             if destination.is_displayed():
#                 for WebElement in destinationAll:
#                     jdouvidet = WebElement.is_displayed()
#                     assert jdouvidet == True
#
#                     if jdouvidet == True:
#                         pass
#                     else:
#                         url = self.driver.current_url
#                         msg = "Problem, destinace se nezobrazuji " + url
#                         sendEmail(msg)
#
#         except NoSuchElementException:
#             url = self.driver.current_url
#             msg = "Problem, destinace se nezobrazuji " + url
#             sendEmail(msg)
#
#         assert destination.is_displayed() == True
#
#     def test_zlutak_to_groupsearch(self):
#         self.driver.get(URL_vlastniDoprava)
#         wait = WebDriverWait(self.driver, 300)
#         self.driver.maximize_window()
#         time.sleep(0.3)
#         acceptConsent(self.driver)
#         wait.until(EC.visibility_of(self.driver.find_element_by_xpath(vyhledatZajezdyButtonXpath))).click()
#         time.sleep(2.5)
#
#         self.driver.find_element_by_xpath('//*[@data-testid="popup-closeButton"]').click()
#         groupSearch_D(self, self.driver)
#         self.test_passed = True
#
#     def test_zlutak_to_SRL(self):
#         self.driver.get(URL_vlastniDoprava)
#         self.driver.maximize_window()
#         time.sleep(0.3)
#         acceptConsent(self.driver)
#         time.sleep(3.5)
#
#         self.driver.find_element_by_xpath(kamPojedeteButtonXpath).click()
#         self.driver.find_element_by_xpath(zlutakPolskoDestinaceXpath).click()
#         self.driver.find_element_by_xpath(zlutakPokracovatButtonXpath).click()
#         self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep2).click()
#         self.driver.find_element_by_xpath(zlutakZima2024Xpath).click()
#         self.driver.find_element_by_xpath(zlutakPokracovatButtonXpathStep3).click()
#         self.driver.find_element_by_xpath(zlutakObsazenost2plus1Xpath).click()
#         self.driver.find_element_by_xpath(zlutakPotvrditAvyhledatXpath).click()
#
#         SRL_D(self, self.driver)
#         self.test_passed = True