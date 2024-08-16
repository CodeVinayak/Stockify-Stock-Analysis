from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Chrome options to automatically download files without prompt
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {
    "download.default_directory": r"C:\path\to\your\directory",  # Change this to your preferred download location
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

# Set path to ChromeDriver
service = Service('path_to_chromedriver')  # Replace with your ChromeDriver path

# Initialize the WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Go to the website
    driver.get("https://www.chittorgarh.com/report/latest-buyback-issues-in-india/80/tender-and-open-market-buyback/")

    # Allow the page to load
    time.sleep(5)

    # Find the export button by its ID and click it
    export_button = driver.find_element(By.ID, "export_btn")
    export_button.click()

    # Wait for download to complete
    time.sleep(10)  # Adjust the sleep time depending on download speed

finally:
    # Close the browser
    driver.quit()
