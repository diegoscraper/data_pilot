from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(options)

urls = {
    "google": "https://www.google.com",
    "python": "https://www.python.org",
    "selenium": "https://www.selenium.dev",
}

for key, url in urls.items():  # iterate the urls items
    driver.get(url)
    driver.implicitly_wait(2)  # Wait 1 sec
    print(driver.title)  # HTML <title>
    print(driver.current_url)  # Current URL
    # lists all the cookie-related values that exist in JSON format.
    print(driver.get_cookies())
    driver.get_screenshot_as_file(key + ".png")  # png files
    print(driver.page_source)  # HTML page source
    driver.implicitly_wait(3)  # wait 3 sec before page Refresh
    # refresh the page
    driver.refresh()
