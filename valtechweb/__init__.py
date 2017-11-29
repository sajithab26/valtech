import inspect, os

def getChromeDriverPath():
    return (os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\driver\chromedriver.exe')