# import libraries
from tests.base_test import BaseTest
from pages.home_page import HomePage
from utilities.custom_logger import LogGenerator

class TestHomePage(BaseTest):

    log = LogGenerator.log_gen()

    def test_validate_page_title(self):
        self.log.info("========== test_validate_page_title  START ==========")
        home_pg = HomePage(self.driver)
        status = home_pg.verify_page_title()
        
        if status == True:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False
        
        self.log.info("========== test_validate_page_title  END ==========")

    def test_validate_featured_product_count(self):
        self.log.info("========== test_validate_featured_product_count  START ==========")
        home_pg = HomePage(self.driver)
        fcount = home_pg.verify_featured_product_count()

        if fcount == 5:
            assert True
            self.log.info("Test Passed")
        else:
            self.log.error("Test Failed")
            assert False
        
        self.log.info("========== test_validate_featured_product_count  END ==========")