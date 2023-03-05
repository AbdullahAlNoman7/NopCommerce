import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select

import time
import unittest


class NopCommerce(unittest.TestCase):
    global driver
    screenshot_location = "G:\\SQA\\NopCommerce\\ScreenShoot\\registerFailed.png"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.get("https://demo.nopcommerce.com/")
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)

    def test_register(self):
        # Located register
        click_register = self.driver.find_element(By.LINK_TEXT, "Register")

        # check condition
        expected_title = "nopCommerce demo store"
        self.assertEqual(expected_title, self.driver.title)
        click_register.click()

        time.sleep(5)
        # after click check condition
        expected_title_after_click = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Register']").text
        actual_text_after_click = "Register"
        if expected_title_after_click == actual_text_after_click:
            assert True
        # located element select

        # personal info details
        gender = self.driver.find_element(By.ID, "gender-male")
        firstName = self.driver.find_element(By.ID, "FirstName")
        lastName = self.driver.find_element(By.ID, "LastName")
        dob_day = self.driver.find_element(By.NAME, "DateOfBirthDay")
        dob_month = self.driver.find_element(By.NAME, "DateOfBirthMonth")
        dob_year = self.driver.find_element(By.NAME, "DateOfBirthYear")
        email = self.driver.find_element(By.ID, "Email")

        # company Details
        company_name = self.driver.find_element(By.ID, "Company")

        # password field
        password = self.driver.find_element(By.ID, "Password")
        confirm_pass = self.driver.find_element(By.ID, "ConfirmPassword")

        # click register
        click_register = self.driver.find_element(By.NAME, "register-button")

        # input data
        self.assertTrue(gender.is_displayed())
        gender.click()
        if firstName.is_enabled() and firstName.is_displayed():
            firstName.send_keys("Mr.")
        if lastName.is_enabled() and lastName.is_displayed():
            lastName.send_keys("Ketty ")
        time.sleep(2)
        select_day = Select(dob_day)
        for all_days in select_day.options:
            if all_days.text == "7":
                all_days.click()
                break
        time.sleep(2)
        select_month = Select(dob_month)
        for all_months in select_month.options:
            if all_months.text == "April":
                all_months.click()
                break

        select_year = Select(dob_year)
        for all_years in select_year.options:
            if all_years.text == "1997":
                all_years.click()
                break

        email.send_keys("hello@gmail.com")
        company_name.send_keys("SJ")
        password.send_keys("123456")
        confirm_pass.send_keys("123456")
        click_register.click()

        # check after register
        expected_text_after_register = "Your registration completed"
        actual_text_after_register = self.driver.find_element(By.XPATH,
                                                              "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]").text

        self.assertTrue(expected_text_after_register, actual_text_after_register)
        print("Registration success......")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="G:/SQA/NopCommerce/Report/register"))
