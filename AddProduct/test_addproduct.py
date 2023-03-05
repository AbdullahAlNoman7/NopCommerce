import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains

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

    def test_02add_product(self):
        time.sleep(5)
        # mouse hover computer
        computer = self.driver.find_element(By.XPATH,
                                            "/html/body//div[@class='header-menu']/ul[1]//a[@href='/computers']")
        desktop = self.driver.find_element(By.XPATH,
                                           "/html/body//div[@class='header-menu']/ul[1]/li[1]/ul//a[@href='/desktops']")
        # action chain
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(computer).pause(2).click(desktop).release().perform()
        time.sleep(2)

        # filter price list
        filter_sort_by = self.driver.find_element(By.ID, "products-orderby")
        select_filter_list_by_price = Select(filter_sort_by)
        select_filter_list_by_price.select_by_value("11")
        time.sleep(2)

        # click the product
        click_image = self.driver.find_element(By.XPATH,"//h2[@class='product-title']//a[contains(text(),'Digital "
                                                        "Storm VANQUISH 3 Custom Performance PC')]")
        click_image.click()

        # after click image scroll intoview
        show_button = self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-panel [data-productid]")
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", show_button)

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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G://SQA//NopCommerce//Report//addtocart"))
