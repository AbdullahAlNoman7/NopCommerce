import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

import time
import unittest


class AddProductTest(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://demo.nopcommerce.com/")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_login(self):
        click_login = self.driver.find_element(By.LINK_TEXT, "Log in")
        click_login.click()

        # check condition
        expected_title = "nopCommerce demo store. Login"
        self.assertEqual(expected_title, self.driver.title)
        assert True
        time.sleep(2)
        # select located element
        email_field = self.driver.find_element(By.ID, "Email")
        password_filed = self.driver.find_element(By.ID, "Password")
        login = self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']")

        # input data
        self.assertEqual(email_field.is_enabled(), email_field.is_displayed())
        email_field.send_keys("hello@gmail.com")
        self.assertTrue(password_filed.is_displayed(), password_filed.is_enabled())
        try:
            password_filed.send_keys("123456")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\login1.png")
        login.click()

    def test_remove_product(self):
        # click shopping cart
        click_shopping_cart = self.driver.find_element(By.CSS_SELECTOR, ".cart-label")
        click_shopping_cart.click()

        # check condition after click shopping cart
        actual_text = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Shopping cart']").text
        expected_text = "Shopping cart"
        self.assertTrue(actual_text, expected_text)
        assert True

        # remove button click
        time.sleep(2)
        click_remove_icon = self.driver.find_element(By.XPATH, "//button[@class='remove-btn']")
        if click_remove_icon.is_enabled() and click_remove_icon.is_displayed():
            try:
                click_remove_icon.click()
            except:
                self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\removeproduct.png")

        # single product have added and remove after check conditon
        expected_text_after_remove = self.driver.find_element(By.XPATH, "//div[@class='no-data']")
        actual_text_after_remove = "Your Shopping Cart is empty!"
        self.assertTrue(expected_text_after_remove, actual_text_after_remove)
        try:
            print("Remove succesfull.....")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\removeproduct1.png")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="G://SQA//NopCommerce//Report//removeproduct"))
