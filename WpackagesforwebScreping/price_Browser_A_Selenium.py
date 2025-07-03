from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# select your respective browser method- make sure the webfriver s in windows folder
# in the c-drive
browser = webdriver.Chrome()  # This brwser can be any browser

# get the link for the
browser.get("https://vistaenergymarketing.com/choice-gas/")

# to find the signing inspect the wesite if it has any unique Id attached to the sign  and where none
Signin_link = browser.find_element_by_link_text("View Plans and Enroll")
Signin_link.click()
username_box = browser.find_element_by_id("textboxSearch")
username_box.send_keys("6038411955")
Signin_link = browser.find_element_by_id("buttonSearch_Basic")
Signin_link.click()
Signin_link = browser.find_element_by_id("buttonSubmitAccountDetail_308172")
Signin_link.click()
# login/signing in processes , inspect the login for unique_id
"""username_box = browser.find_element_by_id("login_field")
print(username_box)
username_box.send_keys("test@gmail.com")
password_box = browser.find_element_by_id("password")
password_box.send_keys("")
password_box.submit()

# verify username is true
profile_link = browser.find_element_by_class_name("user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "test@gmail.com" in link_label"""

# browser.close()
