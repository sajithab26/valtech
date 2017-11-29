
class Page(object):

    def __init__(self, driver, base_url='https://www.valtech.com'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open(self, path):
        url = self.base_url + path
        self.driver.get(url)
        self.driver.maximize_window()