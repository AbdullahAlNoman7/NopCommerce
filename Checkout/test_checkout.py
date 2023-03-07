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


class Checkout(unittest.TestCase):
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
        try:
            self.assertTrue(password_filed.is_displayed(), password_filed.is_enabled())
            password_filed.send_keys("123456")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\login1.png")
        login.click()

    def test_02checkout(self):
        # click shopping cart
        click_shopping_cart = self.driver.find_element(By.CSS_SELECTOR, ".cart-label")
        click_shopping_cart.click()

        # scroll until got checkout button
        checkout_button_check = self.driver.find_element(By.ID, "checkout")
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth'});", checkout_button_check)

        # apply discount code
        discount_code = self.driver.find_element(By.ID, "discountcouponcode")
        try:
            self.assertTrue(discount_code.is_enabled(), discount_code.is_displayed())
            discount_code.send_keys("456")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\discountcode.png")

        # click term and condition
        click_term_conditon = self.driver.find_element(By.ID, "termsofservice")
        click_term_conditon.click()

        #  click checkout button
        click_checkout_button = self.driver.find_element(By.ID, "checkout")
        try:
            self.assertTrue(click_checkout_button.is_enabled(), checkout_button_check.is_displayed())
            click_checkout_button.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\checkout.png")

    def test_03addinfo(self):
        # shipping address
        # country select
        country_select = self.driver.find_element(By.ID, "BillingNewAddress_CountryId")
        check_country = Select(country_select)
        for all_country in check_country.options:
            if all_country.text == "Australia":
                all_country.click()
                break

        # select city
        city = self.driver.find_element(By.ID, "BillingNewAddress_City")
        try:
            self.assertTrue(city.is_enabled(), city.is_displayed())
            city.send_keys("Utara")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\city.png")

        # address 1
        address1 = self.driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1.send_keys("Australia")
        # address
        address2 = self.driver.find_element(By.ID, "BillingNewAddress_Address2")
        address2.send_keys("Australia2")
        # postal code
        postal_code = self.driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        postal_code.send_keys("2546")
        # phone number
        phone_number = self.driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone_number.send_keys("2546")
        # fax number
        fax_number = self.driver.find_element(By.ID, "BillingNewAddress_FaxNumber")
        fax_number.send_keys("2546")
        # click continue
        click_continue = self.driver.find_element(By.CSS_SELECTOR,
                                                  "div#billing-buttons-container > button[name='save']")
        click_continue.click()

        # shipping method
        time.sleep(2)
        next_day_click = self.driver.find_element(By.ID, "shippingoption_1")
        try:
            self.assertTrue(next_day_click.is_displayed(), next_day_click.is_enabled())
            next_day_click.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\nextday.png")

        click_continue_shipping_method = self.driver.find_element(By.CSS_SELECTOR,
                                                                  "[onclick='ShippingMethod\.save\(\)']")
        click_continue_shipping_method.click()

        # payment method
        time.sleep(2)
        click_continue_payment_method = self.driver.find_element(By.CSS_SELECTOR,"[class='button-1 payment-method-next-step-button']")
        click_continue_payment_method.click()

        # payment information
        time.sleep(2)
        click_continue_payment_information = self.driver.find_element(By.CSS_SELECTOR,"[onclick='PaymentInfo\.save\(\)']")
        click_continue_payment_information.click()

        # confirm order
        #check condition
        expected_text = self.driver.find_element(By.CSS_SELECTOR,".billing-info strong").text
        actual_text = "Billing Address"
        try:
            self.assertTrue(expected_text,actual_text)
            click_confirm_order = self.driver.find_element(By.CSS_SELECTOR,"[onclick='ConfirmOrder\.save\(\)']")
            click_confirm_order.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\proccessfield.png")


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G:/SQA/NopCommerce/Report/checkout"))
