import pytest
from selenium import webdriver
from config.config import TestDate
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        #web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(executable_path = r"C:\Users\jayra\PycharmProjects\PageObjectModel\chromedriver.exe")
        web_driver.maximize_window()

    elif request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path = TestDate.FIREFOX_EXE_PATH )
    elif request.param == "edge":
        web_driver = webdriver.Edge(executable_path = TestDate.EDGE_EXE_PATH )
    request.cls.driver = web_driver
    web_driver.get(TestDate.BASE_URL)

    yield
    web_driver.quit()

