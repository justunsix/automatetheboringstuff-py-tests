from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import time

print(
    "If experiencing issues, close all Firefox instances and then start Firefox with --marionette"
)

webdriver_service = Service(
    service_args=["--marionette-port", "2828", "--connect-existing"]
)

driver = webdriver.Firefox(service=webdriver_service)

driver.get("https://www.google.com")
# Print the page title
print("Page title is:", driver.title)
time.sleep(2)
driver.quit()
