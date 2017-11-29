import unittest

from selenium import webdriver

from valtechweb.pageObjects.pages import MainPage
from valtechweb import getChromeDriverPath


class ValtechSystemTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(getChromeDriverPath())


    def test_tocheck_about_exists_in_pageheader(self):
        mainpage = MainPage(self.driver)
        mainpage.load()
        aboutpage = mainpage.goto_about()
        self.assertEqual('About',aboutpage.getPageHeader(),'About is not present in header')

    def test_tocheck_work_exists_in_pageheader(self):
        mainpage = MainPage(self.driver)
        mainpage.load()
        workpage = mainpage.goto_work()
        self.assertEqual('Work', workpage.getPageHeader(), 'Work is not present in header')

    def test_to_check_services_exists_in_pageheader(self):
        mainpage = MainPage(self.driver)
        mainpage.load()
        servicespage = mainpage.goto_services()
        self.assertEqual('Services', servicespage.getPageHeader(), 'Services is not present in header')

    def test_to_check_offices_count(self):
        expectednumberofoffices = 37
        mainpage = MainPage(self.driver)
        mainpage.load()
        contactofficepage = mainpage.goto_contactoffice()
        actualnumberofoffices = contactofficepage.getofficecountrycount()
        self.assertEqual(expectednumberofoffices,actualnumberofoffices)

    def test_to_check_latest_news(self):
        mainpage = MainPage(self.driver)
        mainpage.load()
        self.assertTrue(mainpage.islatestnewspresent())


    def tearDown(self):
        self.driver.close()
