import sys, os
sys.path.insert(0, os.path.abspath('./test'))
print(sys.path)
from pages.LoginPage import LoginPage
import unittest
from dotenv import load_dotenv
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

load_dotenv()

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.login_page = LoginPage(self.driver)

    @classmethod
    def test_login_valid(self):
        self.login_page.open_login_page()
        self.login_page.send_credentials()
        self.login_page.click_on_login_button()
        self.assertTrue(self.login_page.is_products_page_displayed())

    @classmethod
    def tearDown(self):
        print("Test completed")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

