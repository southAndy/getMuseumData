from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def create_chrome_driver():
    chromeDriverPath = './chromedriver'
    s = Service(chromeDriverPath)
    # 模仿瀏覽器設定
    options = Options()
    options.add_argument("--disable-notifications")
    # 用 selenium 開啟瀏覽器
    driver = webdriver.Chrome(service=s, options=options)
    return driver
