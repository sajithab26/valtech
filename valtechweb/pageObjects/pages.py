from valtechweb.pageObjects.locators import *
from valtechweb.pageObjects.base import Page


class MainPage(Page):

    def load(self):
        self.open('')

    def goto_about(self):
        self.find_element(*MainPageLocatars.ABOUT).click()
        return AboutPage(self.driver)

    def goto_work(self):

        self.find_element(*MainPageLocatars.WORK).click()
        return Workpage(self.driver)

    def goto_services(self):
        self.find_element(*MainPageLocatars.SERVICES).click()
        return ServicesPage(self.driver)

    def goto_contactoffice(self):
        self.find_element(*MainPageLocatars.CONTACTOFFICES).click()
        return ContactOfficePage(self.driver)

    def islatestnewspresent(self):
        ele = self.find_element(*MainPageLocatars.NEWS)
        if ele.text == 'LATEST NEWS':
            return True
        else:
            print('News Text : ' + ele.text)
            return False


class AboutPage(Page):

    def getPageHeader(self):
        ele = self.find_element(*AboutPageLocatars.HEADER)
        return ele.text


class Workpage(Page):

    def getPageHeader(self):
        ele = self.find_element(*WorkPageLocatars.HEADER)
        return ele.text


class ServicesPage(Page):

     def getPageHeader(self):
         ele = self.find_element(*ServicesPageLocatars.HEADER)
         return ele.text


class ContactOfficePage(Page):

     def getofficecountrycount(self):
         ele = self.find_elements(*ContactOfficePageLocatars.CONTACTCITIES)
         return len(ele)
