import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

import time
import unittest

class ContinueShopping(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://demo.nopcommerce.com/")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_01login(self):
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

    def test_02continue_shopping(self):
        # click shopping cart
        click_shopping_cart = self.driver.find_element(By.CSS_SELECTOR, ".cart-label")
        click_shopping_cart.click()

        # click continue shopping button
        click_continue_button = self.driver.find_element(By.CSS_SELECTOR,"button[name='continueshopping']")
        self.assertTrue(click_continue_button.is_displayed(),click_continue_button.is_enabled())
        click_continue_button.click()

        # after click continue button check condition
        expected_text = self.driver.find_element(By.XPATH,"//h1[normalize-space()='Desktops']").text
        actual_text = "Desktops"
        if expected_text == actual_text:
            try:
                print("ok....")
            except:
                self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\continueshopping.png")

        # select product
        click_desktop = self.driver.find_element(By.XPATH,"//div[@class='product-item']//img[@title='Show details for "
                                                          "Build your own computer']")
        click_desktop.click()
        time.sleep(2)

    def test_03build_own_customized(self):
        # RAM select
        ram = self.driver.find_element(By.ID,"product_attribute_2")
        select_ram = Select(ram)
        select_ram.select_by_value("5")
        time.sleep(1)
        # HDD select
        hdd = self.driver.find_element(By.CSS_SELECTOR,"[for='product_attribute_3_7']")
        hdd.click()
        time.sleep(1)
        # OS select
        os = self.driver.find_element(By.CSS_SELECTOR,"[for='product_attribute_4_9']")
        if not os.is_selected():
            try:
                os.click()
            except:
                self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\os.png")
        time.sleep(1)
        # given quantity
        quantity = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-panel input")
        quantity.clear()
        quantity.send_keys(2)
        time.sleep(2)
        # add to cart
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-panel [data-productid]")
        add_to_cart_button.click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G://SQA//NopCommerce//Report//continueshopping"))

