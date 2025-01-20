from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# select your respective browser method- make sure the webdriver is downloaded in windows folder in the c-drive
browser = webdriver.Chrome()  # can be used with other browser as well

# get the link for the
browser.get("http://github.com")

# Analyses teh website
# find the signing through inspecting the wesite if it has any unique Id attached to the sign  and where none
Signin_link = browser.find_element_by_link_text("Sign in")
Signin_link.click()

# login/signing in processes , inspect the login for unique_id
username_box = browser.find_element_by_id("login_field")
print(username_box)
username_box.send_keys("test@gmail.com")
password_box = browser.find_element_by_id("password")
password_box.send_keys("2$")
password_box.submit()

# verify username is true
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "test@gmail.com" in link_label

browser.close()
