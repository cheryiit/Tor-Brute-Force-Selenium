import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumManager:

    def __init__(self, tor_folder_path, profile_path, firefox_binary_path):
        self.tor_folder_path = tor_folder_path
        self.profile_path = profile_path
        self.firefox_binary_path = firefox_binary_path
        self.driver = None

    def start_tor(self):
        self.profile = FirefoxProfile(self.profile_path)
        self.profile.set_preference("network.proxy.type", 1)
        self.profile.set_preference("network.proxy.socks", '127.0.0.1')
        self.profile.set_preference("network.proxy.socks_port", 9250)

        options = Options()
        options.binary_location = self.firefox_binary_path

        self.driver = webdriver.Firefox(firefox_profile=self.profile, options=options)
        time.sleep(2)

    def quit_driver(self):
        self.driver.quit()

    def restart_tor(self):
        self.quit_driver()
        time.sleep(3)
        self.start_tor()

    def new_identity(self):
        self.quit_driver()
        time.sleep(1)
        self.start_tor()
        time.sleep(2)

    def refresh_identity(self):
        try:
            self.driver.get("https://check.torproject.org/")
            self.driver.find_element_by_xpath("//a[text()='New Identity']").click()
            time.sleep(2)  # wait for the new identity to be established
            return True
        except:
            return False

    def wait_for_element(self, xpath, timeout=10):
        element_present = EC.presence_of_element_located((By.XPATH, xpath))
        WebDriverWait(self.driver, timeout).until(element_present)

    def wait_for_element_css(self, css, timeout=10):
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, css))
        WebDriverWait(self.driver, timeout).until(element_present)

    def has_recaptcha(self):
        try:
            wait = WebDriverWait(self.driver, 2)
            wait.until(EC.presence_of_element_located((By.XPATH, '//iframe[contains(@src, "recaptcha")]')))
            print("reCAPTCHA ERROR!!")
            return True

        except:
            print("There is no reCAPTCHA!!")
            return False


    def wait_for_page_load(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@data-page-loaded="true"]')))
