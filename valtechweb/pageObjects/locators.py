from selenium.webdriver.common.by import By

class MainPageLocatars(object):
    ABOUT = (By.XPATH, "//span[contains(.,'About')]")
    WORK = (By.XPATH, "//span[contains(.,'Work')]")
    SERVICES = (By.XPATH, "//span[contains(.,'Services')]")
    CONTACTOFFICES = (By.CSS_SELECTOR, '.icons.glyph')
    NEWS = (By.CSS_SELECTOR, '.news-post__listing-header')

class AboutPageLocatars(object):
    HEADER = (By.CSS_SELECTOR, '.page-header > h1')

class WorkPageLocatars(object):
    HEADER = (By.CSS_SELECTOR, '.page-header > h1')

class ServicesPageLocatars(object):
    HEADER = (By.CSS_SELECTOR, '.page-header > h1')

class ContactOfficePageLocatars(object):
    CONTACTCITIES = (By.CSS_SELECTOR, '.contactcities > li')