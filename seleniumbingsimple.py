# Small script with Bing AI
# i'll note down the corrections i've made.
# This script just opens Selenium's documentation page, i won't do a readme.md since it was a short experimental thing.
# Made by Chuma assisted by Bing AI.
# Co Credits to Nepta and Dany.
from selenium import webdriver
from selenium.webdriver.common.by import By # Added by Chuma.

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Find the search box and enter the query
search_box = driver.find_element(By.NAME,"q")  # element by ID old version , q refers to the search bar.
search_box.send_keys("Selenium documentation") # I "rewrote" the search typing parameter.

# Submit the query
search_box.submit()


# Find the link to the Selenium documentation site and click it
#link = driver.find_element(By.PARTIAL_LINK_TEXT,'The Selenium browser automation') # Not sure if this can work, it didn't for me
link = driver.find_element(By.CSS_SELECTOR,"a[href='https://www.selenium.dev/documentation/']")
link.click()

# I modified the CSS Selector because the link was partially wrong, small change applied

# Keep the browser window open (done by Bing AI, this works but the detach function is more optimal)
input("Press Enter to close the browser...")

# I wanted to use the detach function, i tried that Bing AI

