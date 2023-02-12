import pytest
from selenium import webdriver
from configuration.config import ConfigData

@pytest.fixture(params=["chrome"], scope="function")
def setup_browser(request):
    
    if request.param == "chrome":
        _driver = webdriver.Chrome()

    request.cls.driver = _driver
    _driver.get(ConfigData.BASE_URL)
    _driver.implicitly_wait(10)
    _driver.maximize_window()
    # close browser
    yield
    _driver.quit()
