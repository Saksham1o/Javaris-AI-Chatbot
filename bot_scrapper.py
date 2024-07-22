from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import warnings
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

warnings.simplefilter("ignore")
url = f"https://cdn.botpress.cloud/webchat/v1/index.html?options=%7B%22config%22%3A%7B%22composerPlaceholder%22%3A%22Talk%20to%20AVA%22%2C%22botConversationDescription%22%3A%22AVA-%20Virtual%20Assistance%22%2C%22botId%22%3A%22523f0fb5-5465-49cd-add0-0ab112f8e10a%22%2C%22hostUrl%22%3A%22https%3A%2F%2Fcdn.botpress.cloud%2Fwebchat%2Fv1%22%2C%22messagingUrl%22%3A%22https%3A%2F%2Fmessaging.botpress.cloud%22%2C%22clientId%22%3A%22523f0fb5-5465-49cd-add0-0ab112f8e10a%22%2C%22webhookId%22%3A%22bb8b8b32-e44d-4d5a-82fe-742ac9a15369%22%2C%22lazySocket%22%3Atrue%2C%22themeName%22%3A%22prism%22%2C%22botName%22%3A%22AVA-%20Virtual%20Assistance%22%2C%22stylesheet%22%3A%22https%3A%2F%2Fwebchat-styler-css.botpress.app%2Fprod%2F6b8cf6e1-a574-4f16-af37-3fde90f152a6%2Fv29879%2Fstyle.css%22%2C%22frontendVersion%22%3A%22v1%22%2C%22showPoweredBy%22%3Atrue%2C%22theme%22%3A%22prism%22%2C%22themeColor%22%3A%22%232563eb%22%2C%22allowedOrigins%22%3A%5B%5D%2C%22chatId%22%3A%22bp-web-widget%22%2C%22encryptionKey%22%3A%228uO3LkysAUo2sHGQxbZBqKtlzOMCwPba%22%7D%7D"
chrome_driver_path = 'chromedriver.exe'
chrome_options = Options()
# chrome_options.add_argument("--headless=new") # Enable headless mode (Runs chrome without GUI)
chrome_options.add_argument('--log-level=3') # Set chrome log level
service = Service(chrome_driver_path)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(Service = service , options= chrome_options)
driver.maximize_window()
driver.get(url)
sleep(3)


def click_on_chat_button():
    button = driver.find_element(By.XPATH , '/html/body/div/div/button').click()
    sleep(2)
    while True:
        try:
            loader = driver.find_element(By.CLASS_NAME , 'bpw-msg-list-loading')
            is_visible = loader.is_displayed()
            print("Initializing ava...")

            if not is_visible:
                break
        except NoSuchElementException:
            print("AVA is Initializing.")
            break
        sleep(1)

def sendQuery(text):
    # find and interact with the textarea element
    textarea = driver.find_element(By.ID,'input-message')
    textarea.send_keys(text)
    sleep(1)

    sleep_btn = driver.find_element(By.ID,'btn-send').click()
    sleep(1)


def isBubbleLoaderVisible():
    print("AVA is typing")
    while True:
        try:
            bubble_loader = driver.find_element(By.CLASS_NAME,'bpw-typing-group')
            is_visible = bubble_loader.is_displayed()

            if not is_visible:
                break
            else:
                pass
        except NoSuchElementException:
            print("AVA is sending message...")
            break
        sleep(1)


chatnumber = 2 

