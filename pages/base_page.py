# import libraries
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    wait_timeout = 10
    
    # constructor
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, self.wait_timeout)
    
    # action 
    def perform_click(self, by_locator):
        self.wait.until(EC.element_to_be_clickable(by_locator)).click()

    def get_page_title(self, title:str) -> bool:
        status = self.wait.until(EC.title_is(title))
        return status

    def get_webelements_count(self, by_locator) -> int:
        list_webelements = self.wait.until(EC.presence_of_all_elements_located(by_locator))
        return len(list_webelements)
