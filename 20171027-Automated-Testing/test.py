#! /usr/bin/env python


import time     # Used for to give time for a page to load
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Setup the options for Chrome:
options = webdriver.ChromeOptions()
options.add_argument("--test-type")

# Replace this with the path to your chromedriver:
driver_path = "C:\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)

# Navigate to thedigitalcraft.com
driver.get("https://thedigitalcraft.com")

# Save a screenshot of the Home page:
driver.save_screenshot("home-page.png")

# Get the Live Events link and click it:
element = driver.find_element_by_id("live-events")
element.click()

# Wait for the page to load (there are ways to do this with the webdriver too)
time.sleep(5)

# Save a screenshot of the Live Events page:
driver.save_screenshot("live-events-page.png")

# Get the First Name field in the form and send text to it:
element = driver.find_element_by_id("first_name")
element.send_keys("Alan")

# Get the Last Name field in the form and send text to it:
element = driver.find_element_by_id("last_name")
element.send_keys("Quandt")

# Get the Email field in the form and send text to it:
element = driver.find_element_by_id("email")
element.send_keys("some@place.com")

# Get the Question field in the form and send text to it:
element = driver.find_element_by_id("question")
# It would be awesome if you sent a real question!
element.send_keys("I have a great question!")

# Save a screenshot of the Live Events page with the form filled out:
driver.save_screenshot("live-events-page-form.png")

# Get the form's button and hit enter to submit it:
element = driver.find_element_by_xpath('//*[@id="live-event-questions"]/button')
element.send_keys(Keys.RETURN)

# Save a screenshot of the Live Events page after the form as been submitted:
driver.save_screenshot("live-events-page-form-submitted.png")

# Wait 5 seconds so you can see what has been done:
time.sleep(5)

# Close the session and browser:
driver.close()
