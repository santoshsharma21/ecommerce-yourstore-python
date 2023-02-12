# import libraries
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    
    # page objects
    my_account_link = (By.XPATH, "//span[normalize-space()='My Account']")
    my_account_options = (By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']/li")
    featured_products = (By.XPATH, "//div[@id='content']//div[@class='row']/div")

    # constructor
    def __init__(self, driver) -> None:
        super().__init__(driver)
        self.driver = driver

    # action methods
    def verify_page_title(self) -> bool:
        status = self.get_page_title("Your Store")
        return status

    def verify_featured_product_count(self) -> int:
        count = self.get_webelements_count(self.featured_products)
        return count
