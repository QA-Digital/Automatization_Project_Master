from selenium.webdriver.common.by import By
from KTGHU.to_import import URL, setUp, tearDown
import unittest
from compare_SRL_results_DEV_vs_PROD import list_SRL_number_of_results

URL_public_prod = "https://kartagotours.hu"



URL_SRL_KTGHU1 = "/keresesi-eredmenyek?ac1=2&d=64419|64420|64425|211801|211814|63260|63288|63448&dd=2023-09-01&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU2 = "/keresesi-eredmenyek?ac1=2&d=63252|63447&dd=2023-09-01&ds=0&ic1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU3 = "/keresesi-eredmenyek?ac1=2&d=63213|63216|63218|63226|63227|63231|63241|63242|63243|63244|63245|63263|63267|63272|63284|63299|63312|63313|63328|63334|63349|63350|63354|63360|63363|63455|64429|64430|74459|74460|74461|74462|74463|74464|74465|77806|211764&dd=2023-10-01&ic1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-11-30&to=489|4371&tt=0"

URL_SRL_KTGHU4 = "/keresesi-eredmenyek?ac1=2&d=64086|64087|64089|64090|64091|64092|64093|64094|64095|64096&dd=2023-09-01&ds=0&ic1=1&ka1=5&kc1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU5 = "/keresesi-eredmenyek?ac1=2&d=64419|64420|64421|64422|64423|64424|64425|64426&dd=2023-10-01&ds=0&ic1=1&ka1=5&kc1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-11-30&to=489|4371&tt=0"

URL_SRL_KTGHU6 = "/keresesi-eredmenyek?ac1=2&d=63213|63216|63218|63226|63227|63231|63241|63242|63243|63244|63245|63263|63267|63272|63284|63299|63312|63313|63328|63334|63349|63350|63354|63360|63363|63455|64429|64430|74459|74460|74461|74462|74463|74464|74465|77806|211764&dd=2023-10-01&ds=0&ic1=1&ka1=5|7&kc1=2&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-11-30&to=489|4371&tt=0"

URL_SRL_KTGHU7 = "/keresesi-eredmenyek?ac1=2&d=63252|63447&dd=2023-10-01&ds=0&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-11-30&to=489|4371&tt=0"

URL_SRL_KTGHU8 = "/keresesi-eredmenyek?ac1=4&d=64419|64420|64421|64422|64423|64424|64425|64426&dd=2023-10-01&ds=0&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-11-30&to=489|4371&tt=0"

URL_SRL_KTGHU9 = "/keresesi-eredmenyek?ac1=4&d=64086|64087|64089|64090|64091|64092|64093|64094|64095|64096&dd=2023-09-01&ds=0&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU10 = "/keresesi-eredmenyek?ac1=2&d=63260|63288|63448|64152|64153|64154|64157|211801|211814&dd=2023-09-01&ds=0&ic1=1&ka1=10&kc1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU11 = "/keresesi-eredmenyek?ac1=2&d=63209|63214|63219|63220|63262|63266|63281|63283|63285|63290|63297|63311|63314|63316|63319|63324|63327|63333|63335|63336|63341|63352|63357|63362|63364|63373|63383|63384|63387|63388|63390|63399|63402|63408|63409|63424|63427|63428|63430|63431|63437|63439|63442|63463|63471|63472|64431|64432|64433|64434|64435|64436|64437|64438|64439|64440|64441|64442|74677&dd=2023-09-01&ds=0&ic1=1&ka1=10&kc1=1&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"

URL_SRL_KTGHU12 = "/keresesi-eredmenyek?ac1=2&d=63213|63216|63218|63226|63227|63231|63241|63242|63243|63244|63245|63263|63267|63272|63284|63299|63312|63313|63328|63334|63349|63350|63354|63360|63363|63455|64429|64430|74459|74460|74461|74462|74463|74464|74465|77806|211764&dd=2023-10-01&ds=0&nn=4|5|6|7|8|9|10|11|12|13|14&rd=2023-10-31&to=489|4371&tt=0"



URL_SRLs_list_KTGHU = [URL_SRL_KTGHU1, URL_SRL_KTGHU2, URL_SRL_KTGHU3, URL_SRL_KTGHU4, URL_SRL_KTGHU5, URL_SRL_KTGHU6, URL_SRL_KTGHU7, URL_SRL_KTGHU8, URL_SRL_KTGHU9, URL_SRL_KTGHU10, URL_SRL_KTGHU11, URL_SRL_KTGHU12]





from KTGHU.to_import import URL_local
class Test_SRL_C_comparer(unittest.TestCase):
    URL = URL_local  # Default value
    def __init__(self, methodName="runTest", URL=None):
        super().__init__(methodName)
        if URL:
            self.URL = URL

    def setUp(self):
        setUp(self)


    def tearDown(self):
        tearDown(self)


    def test_SRL_number_of_results_comparer(self):
        list_SRL_number_of_results(self.driver, URL, URL_public_prod, URL_SRLs_list_KTGHU)



        self.test_passed = True