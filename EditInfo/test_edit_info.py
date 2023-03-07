import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

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

    def test_02edit_address(self):
        # click my account
        click_my_account = self.driver.find_element(By.CSS_SELECTOR, ".ico-account")
        click_my_account.click()

        # check conditon
        expected_title = "nopCommerce demo store. Account"
        address = self.driver.find_element(By.CSS_SELECTOR, ".customer-addresses > a")
        try:
            self.assertEqual(expected_title, self.driver.title)
            address.click()
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailed.png")

        # check add new button displayed or not
        add_new = self.driver.find_element(By.CSS_SELECTOR, "[onclick]")
        if add_new.is_displayed():
            add_new.click()
        else:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailedAddNew.png")

        # add first name
        first_name = self.driver.find_element(By.ID,"Address_FirstName")
        try:
            self.assertTrue(first_name.is_enabled())
            first_name.send_keys("Aila1 ")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailedFirstName.png")

        # add last name
        last_name = self.driver.find_element(By.ID,"Address_LastName")
        try:
            self.assertTrue(last_name.is_enabled())
            last_name.send_keys("Jadu2 ")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailedLastName.png")

        # add email
        email_filed = self.driver.find_element(By.ID,"Address_Email")
        try:
            self.assertTrue(email_filed.is_displayed())
            email_filed.send_keys("Ailajadu@gmail.com")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailedEmail.png")

        # add company
        company_filed = self.driver.find_element(By.ID,"Address_Company")
        try:
            self.assertTrue(company_filed.is_displayed())
            company_filed.send_keys("Aila Jadu")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\AddressFailedEmail.png")

        # country select
        country_select = self.driver.find_element(By.ID, "Address_CountryId")
        check_country = Select(country_select)
        for all_country in check_country.options:
            if all_country.text == "Australia":
                all_country.click()
                break

        # select city
        city = self.driver.find_element(By.ID, "Address_City")
        try:
            self.assertTrue(city.is_enabled())
            city.send_keys("Utara")
        except:
            self.driver.get_screenshot_as_file("G:\\SQA\\NopCommerce\\ScreenShoot\\city.png")

        # address 1
        address1 = self.driver.find_element(By.ID, "Address_Address1")
        address1.send_keys("Australia")
        # address
        address2 = self.driver.find_element(By.ID, "Address_Address2")
        address2.send_keys("Australia2")
        # postal code
        postal_code = self.driver.find_element(By.ID, "Address_ZipPostalCode")
        postal_code.send_keys("2546")
        # phone number
        phone_number = self.driver.find_element(By.ID, "Address_PhoneNumber")
        phone_number.send_keys("2546")
        # fax number
        fax_number = self.driver.find_element(By.ID, "Address_FaxNumber")
        fax_number.send_keys("2546")
        # save info
        save_button = self.driver.find_element(By.XPATH,"//button[normalize-space()='Save']")
        save_button.click()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        print('Tested....')
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G://SQA//NopCommerce//Report//EditInfo"))
