import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time
import unittest


class EditInfo(unittest.TestCase):
    global driver

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://demo.nopcommerce.com/")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.maximize_window()

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
        try:
            self.assertTrue(password_filed.is_displayed(), password_filed.is_enabled())
            password_filed.send_keys("123456")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\login1.png")
        login.click()

    def test_02wish_list(self):
        # select product through mouse hover
        electronics = self.driver.find_element(By.CSS_SELECTOR, ".notmobile [href='\/electronics']")
        camera = self.driver.find_element(By.CSS_SELECTOR, ".notmobile [href='\/camera-photo']")
        mouser_hover = ActionChains(self.driver)
        mouser_hover.move_to_element(electronics).pause(2).click(camera).pause(1).release().perform()
        time.sleep(2)
        # scroll until product not displayed and click
        scroll = self.driver.find_element(By.LINK_TEXT, "Leica T Mirrorless Digital Camera")
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth'});", scroll)
        try:
            scroll.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\WishList.png")
        time.sleep(3)

        # shipping procedure
        scroll_product = self.driver.find_element(By.CSS_SELECTOR, "[data-effect] span")
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth'});", scroll_product)
        try:
            self.assertTrue(scroll_product.is_displayed())
            scroll_product.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\WishListShipping.png")
        time.sleep(2)
        # select process
        country = self.driver.find_element(By.ID, "CountryId")
        all_country = Select(country)
        all_country.select_by_value("183")
        time.sleep(2)
        zip_code = self.wait.until(EC.presence_of_element_located((By.ID, "ZipPostalCode")))
        zip_code.send_keys("4562")
        shipping_method = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[normalize-space()='Next Day Air']")))
        shipping_method.click()
        apply = self.driver.find_element(By.XPATH, "//button[normalize-space()='Apply']")
        apply.click()
        time.sleep(3)
        # after complete shipping porcess click add to wishlist
        add_to_wish = self.wait.until(EC.presence_of_element_located((By.ID, "add-to-wishlist-button-16")))
        add_to_wish.click()

    @classmethod
    def tearDownClass(cls):
        print("Tested.....")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G://SQA//NopCommerce//Report//AddWishlist"))
