from selenium import webdriver

profile = webdriver.FirefoxProfile()

driver = webdriver.Firefox(firefox_profile=profile, executable_path="C:\Python35\geckodriver.exe")
driver.maximize_window()

class Facebook(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('pass').send_keys(password)
        driver.find_element_by_id('login_form').submit()

# Autorization
driver.get('https://www.facebook.com/')
Facebook(driver).login('email@gmail.com', 'NoPassw0rd')
