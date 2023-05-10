from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchWindowException
import threading
import os
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

chrome_data_dir = config['DEFAULT']['chrome_data_dir']

chrome_profile = config['DEFAULT']['chrome_profile']

options = Options()

options.add_extension('./jut.su.Next-Series.crx')
options.add_argument("--disable-dev-shm-usage")
options.add_argument('--disable-session-crashed-bubble')
options.add_argument('unexpectedAlertBehaviour=ignore')
options.add_argument('--user-data-dir={}'.format(chrome_data_dir))
options.add_argument('--profile-directory={}'.format(chrome_profile))
options.add_experimental_option("excludeSwitches", ['enable-automation'])

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('https://jut.su/')


temp_Url = driver.current_url

previous_timer = None



def check_current_url(f_driver=driver):
    global temp_Url
    try:
        current_url = f_driver.current_url
    except NoSuchWindowException:
        close_driver()
    else:
        try:
            full_screen_btn = get_element("button.extension-overlay-button")
            if full_screen_btn == "none":
                return
            get_full_screen(full_screen_btn)
        except ElementNotInteractableException as e:
            return
        temp_Url = current_url


def get_element(selector):
    try:
        return driver.find_element(By.CSS_SELECTOR, selector)
    except NoSuchElementException:
        return "none"
    except NoSuchWindowException:
        close_driver()



def get_full_screen(btn):
            btn.click()


def close_driver():
    driver.quit()
    pid = (os.getpid())
    os.system(f"Taskkill /PID {pid} /F")



def set_interval(interval, func):
    def wrapper():
        set_interval(interval, func)
        func()
    t = threading.Timer(interval / 1000, wrapper)
    t.start()
    global previous_timer
    if previous_timer is not None:
        previous_timer.cancel()
    previous_timer = t
    return t


set_interval(3000, check_current_url)
