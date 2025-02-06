from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

CHROMEDRIVER_PATH = "your path to driver"

options = webdriver.ChromeOptions()
options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
driver.get("https://web.telegram.org/k/")
input("Log in to Telegram Web, then press Enter to continue...")

def get_unread_chats():
    """Find unread messages (chats with notification badges)."""
    return driver.find_elements(By.XPATH, '//*[@id="column-center"]/div[1]/div/div[4]/div/div[1]/div/div[8]/div[1]')

def auto_reply():
    """Reply to unread messages."""
    while True:
        for chat in get_unread_chats():
            chat.click()
            time.sleep(2)

            input_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="column-center"]/div[1]/div/div[4]/div/div[1]/div/div[8]/div[1]'))
            )
            input_box.send_keys("This is an auto-reply. I'll get back soon 😊", Keys.RETURN)
            time.sleep(2)

        time.sleep(5) 

auto_reply()
driver.quit()
