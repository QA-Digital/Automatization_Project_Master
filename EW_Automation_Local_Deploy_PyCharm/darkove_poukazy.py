from selenium.common.exceptions import NoSuchElementException
from EW_Automation_Local_Deploy_PyCharm.to_import import acceptConsent, sendEmail, URL, setUp, tearDown, \
    generalDriverWaitImplicit
import time
import unittest

# URL_darkove_poukazy = URL + "/poukazy-benefity/darkove-poukazy"
URL_darkove_poukazy = URL + "/informace-pro-klienty/poukazky/darkove-poukazky"

motivyXpath = "//*[@class='absolute inset-0 flex justify-center items-center bg-white/50 transition-all rounded opacity-0']"
vybranyMotivXpath = "//*[@class='flex-1']"

castkyXpath = "//*[@class='col-span-1 btn py-8']"
castkaVlastniXpath = "//*[@class='border w-full border-neutral-300 rounded-[--form-element-rounding] px-4 py-1 text-center text-lg font-semibold']"
venovaniBoxXpath = "//*[@class='w-full border rounded-[--form-element-rounding] border-neutral-300 min-h-[6rem] p-4 order-2 sm:order-3']"

jmeno = "test_jmeno"
prijmeni = "test_prijmeni"
telefon = "735599725"
email = "ooo.kadoun@gmail.com"

jmenoInputXpath = "//*[@id='input-text-1']"
prijmeniInputXpath = "//*[@id='input-text-2']"
telefonInputXpath = "//*[@id='input-phoneNumber-3']"
emailInputXpath = "//*[@id='input-email-4']"
checkboxAgreementXpath = "(//span[@class='inline-block shrink-0 box-border w-4 h-4 relative border rounded-[var(--input-checkbox-rounding)] transition-all border-[var(--neutral-300)] text-[var(--white)]'])[410]"
objednatXpath = "//div[@class='whitespace-nowrap overflow-ellipsis overflow-hidden'][normalize-space()='Objednat a zaplatit']"

platebniKartouXpath = "//*[@class='flex flex-col gap-1 grow items-start']"
zaplatitXpath = "//div[@class='whitespace-nowrap overflow-ellipsis overflow-hidden'][normalize-space()='Zaplatit']"

class Test_darkove_poukazy(unittest.TestCase):
    def setUp(self):
        setUp(self)

    def tearDown(self):
        tearDown(self)

    def test_darkove_poukazy_motivy(self):
        self.driver.maximize_window()
        self.driver.get(URL_darkove_poukazy)
        time.sleep(2.5)

        acceptConsent(self.driver)
        time.sleep(5)
        motivyElements = self.driver.find_elements_by_xpath(motivyXpath)
        print(motivyElements)
        pozice = 0
        for _ in motivyElements:
           # motivyElements[pozice].click()
            self.driver.execute_script("arguments[0].click();", motivyElements[pozice])
            print(pozice)
            time.sleep(2)
            pozice = pozice + 1

        time.sleep(6)

        vybranyMotivElement = self.driver.find_element_by_xpath(vybranyMotivXpath)
        assert vybranyMotivElement.is_displayed() == True

    def test_darkove_poukazy_castka_venovani(self):
        self.driver.maximize_window()
        self.driver.get(URL_darkove_poukazy)
        time.sleep(2.5)

        acceptConsent(self.driver)
        time.sleep(5)

        castkyElements = self.driver.find_elements_by_xpath(castkyXpath)
        pozice = 0
        for _ in castkyElements:
            #castkyElements[pozice].click()
            self.driver.execute_script("arguments[0].click();", castkyElements[pozice])
            print(pozice)
            time.sleep(2)
            pozice = pozice + 1

        vlastniCastkyElement = self.driver.find_element_by_xpath(castkaVlastniXpath)
        number_to_write = "12345"
        #vlastniCastkyElement.click()
        #vlastniCastkyElement.send_keys(number_to_write)
        self.driver.execute_script("arguments[0].value = arguments[1];", vlastniCastkyElement, number_to_write)

        written_text = vlastniCastkyElement.get_attribute("value")
        assert written_text == number_to_write, f"Expected: {number_to_write}, Actual: {written_text}"
        vlastniCastkyElement.clear()
        cleared_text = vlastniCastkyElement.get_attribute("value")
        assert cleared_text == "", "The element is not empty after clearing"
        time.sleep(3)

        text_to_write = "věnuji ti tohle neni to super ,?!*123"
        venovaniBoxElement = self.driver.find_element_by_xpath(venovaniBoxXpath)
        self.driver.execute_script("arguments[0].value = arguments[1];", venovaniBoxElement, text_to_write)
        written_text = venovaniBoxElement.get_attribute("value")
        assert written_text == text_to_write, f"Expected: {number_to_write}, Actual: {written_text}"
        venovaniBoxElement.clear()
        cleared_text =  venovaniBoxElement.get_attribute("value")
        assert cleared_text == "", "The element is not empty after clearing"

    def test_darkove_poukazy_purchase(self):
        self.driver.maximize_window()
        self.driver.get(URL_darkove_poukazy)
        time.sleep(2.5)

        acceptConsent(self.driver)
        time.sleep(5)

        jmenoInputElement = self.driver.find_element_by_xpath(jmenoInputXpath)
        prijmeniInputElement = self.driver.find_element_by_xpath(prijmeniInputXpath)
        telefonInputElement = self.driver.find_element_by_xpath(telefonInputXpath)
        emailInputElement = self.driver.find_element_by_xpath(emailInputXpath)

        checkboxAgreementElement = self.driver.find_element_by_xpath(checkboxAgreementXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",checkboxAgreementElement)
        jmenoInputElement.send_keys(jmeno)
        prijmeniInputElement.send_keys(prijmeni)
        telefonInputElement.send_keys(telefon)
        emailInputElement.send_keys(email)

        checkboxAgreementElement.click()

        self.driver.find_element_by_xpath(objednatXpath).click()

        time.sleep(5)

        self.driver.find_element_by_xpath(platebniKartouXpath).click()
        zaplatitElement = self.driver.find_element_by_xpath(zaplatitXpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", zaplatitElement)
        zaplatitElement.click()
        time.sleep(5)
        assert "gopay" in (self.driver.current_url)
