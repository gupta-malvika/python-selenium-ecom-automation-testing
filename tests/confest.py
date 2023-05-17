import pytest
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def web_browser_setup():
    # driver = webdriver.Firefox(executable_path='C:\\browserdrivers\\geckodriver_x32.exe')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("Opening Chrome Browser...")
    return driver
