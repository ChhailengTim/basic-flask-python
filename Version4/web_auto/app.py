from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome driver using ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# Navigate to Facebook
driver.get("https://www.facebook.com")

myEmail = '100068061740556'
myPass = '822293$$$$'

# Find the email input field by its ID and enter your login credentials
email_field = driver.find_element("id", "email")
email_field.send_keys(myEmail)

# Find the password input field by its ID and enter your password
password_field = driver.find_element("id", "pass")
password_field.send_keys(myPass)

# Submit the login form
password_field.submit()

# Wait for a few seconds (you can adjust this time as needed)
time.sleep(5)

# Navigate to the profile page
driver.get(f'https://web.facebook.com/profile.php?id={myEmail}')

# Find and extract the link from the anchor elements
link_elements = driver.find_elements_by_css_selector("a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x1heor9g.xt0b8zv")

# Extract the href attribute (the link) from each element
links = [element.get_attribute("href") for element in link_elements]

# Print the links
for link in links:
    print("Link:", link)

# Close the browser
driver.quit()
