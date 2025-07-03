import os
import time
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# Set the path to the ChromeDriver executable
#chromedriver_path = '/Users/s.eromonsei/stageGitHub/my_sandbox/PrivacyPolicy_validator_in_Apps/chromedriver'
driver = webdriver.Chrome()

# Create a list of free Android apps from the Play Store
apps = ['cat.game.liftapp', 'com.tutotoons.app.fluvsies.free&hl=en&gl=US', 'com.outfit7.mytalkingtom2&hl=en&gl=US']

# Loop through the list of apps
for app in apps:
    # Use Selenium to open Chrome and navigate to the app's Play Store page
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get(f'https://play.google.com/store/apps/details?id={app}')
    

    # Wait for the "Install" button to be clickable
    install_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Install"]')))

    install_button.click()
    

    # Wait for the sign-in dialog to appear (use appropriate wait conditions)
    wait = WebDriverWait(driver, 30)
    popup_box = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/div[3]/div/button[2]')))
    popup_box.click()

    # Find the username and password fields within the pop-up box
    element_username = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']")))
    element_password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="password"]')))

    element_username.send_keys("exel@gmail.com")
    element_password_field.send_keys(os.environ.get('gmailpwd'))

    # Submit the form
    element_password_field.submit()

    # Submit the form
    element_password_field.submit()
    # Wait for the download to complete
    time.sleep(10)
    
    # Use os to move the downloaded APK file to a new directory
    downloads_path = ' /Users/s.eromonsei/Downloads/'
    apk_filename = f'{app}.apk'
    apk_path = os.path.join(downloads_path, apk_filename)
    os.rename('/path/to/downloaded/apk', apk_path)
    
    # Use os to extract the manifest.xml file from the APK
    manifest_path = os.path.join(downloads_path, f'{app}_manifest.xml')
    os.system(f'apktool d {apk_path} -o {manifest_path}')
    
    # Close the Chrome window
    driver.quit()
