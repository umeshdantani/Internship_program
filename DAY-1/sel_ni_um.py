from selenium import webdriver

# Set up the browser driver
driver = webdriver.Chrome()

url = 'https://flipkart.com'
driver.get(url)
print("Page title:", driver.title)
#element = driver.find_element_by_id("element_id")
driver.quit()