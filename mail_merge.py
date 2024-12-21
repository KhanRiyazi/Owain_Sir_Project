import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # Import the Service class
from webdriver_manager.chrome import ChromeDriverManager  # This will automatically manage the chromedriver for you
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Read contacts data
contacts = pd.read_csv('C:/Users/Dell/AppData/Local/Programs/Python/Python313/Owain_Selenium_Project/name_mail.csv')

# Set up Selenium WebDriver with automatic ChromeDriver management
service = Service(ChromeDriverManager().install())  # This will automatically download and set the correct driver
driver = webdriver.Chrome(service=service)

# Function to log in to Gmail
def login_to_gmail():
    driver.get('https://mail.google.com')
    # Wait until the email input field is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')))
    
    email_input = driver.find_element('xpath', '//input[@type="email"]')
    email_input.send_keys('rizwanrka826@gmail.com')  # Enter your email
    email_input.send_keys(Keys.RETURN)
    
    # Wait until the password input field is present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
    password_input = driver.find_element('xpath', '//input[@type="password"]')
    password_input.send_keys('Ri#123ri')  # Enter your Gmail password
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)
    
# Function to send email
def send_email(to_email, subject, body):
    driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    time.sleep(2)
    
    to_input = driver.find_element('xpath', '//textarea[@name="to"]')
    subject_input = driver.find_element('xpath', '//input[@name="subjectbox"]')
    body_input = driver.find_element('xpath', '//div[@aria-label="Message Body"]')

    to_input.send_keys(to_email)
    subject_input.send_keys(subject)
    body_input.send_keys(body)

    send_button = driver.find_element('xpath', '//div[contains(text(), "Send")]')
    send_button.click()
    time.sleep(2)

# Main script to send emails
def main():
    login_to_gmail()
    
    for _, row in contacts.iterrows():
        name = row['Name']
        email = row['Email']
        subject = row['Subject']
        body = row['Body']

        personalized_body = f"Hello {name},\n\n{body}"
        
        send_email(email, subject, personalized_body)
        print(f"Email sent to {email}")

    driver.quit()

if __name__ == "__main__":
    main()


