import unittest
import utility
from page import HTTP_org_page
from selenium import webdriver

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = utility.driver
        self.driver.get(utility.web_url)
        self.driver.maximize_window()

    @unittest.skip
    def tearDown(self):
        self.driver.close()

    def test_http_methods(self):

        Http_methods = HTTP_org_page(self.driver)
        self.assertEqual("httpbin.org\n 0.9.2 ", Http_methods.get_logo_text())
        Http_methods.click_Http_methods_bar()
        Http_methods.click_Http_delete_bar()
        Http_methods.click_HTTP_delete_TRYitOUT_button()




if __name__ == '__main__':
    unittest.main()



