import time
#import datetime
#import emoji
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
input("Escaneie o QR Code, e pressione [ENTER] posteriormente.")
wait5 = WebDriverWait(driver, 5)

with open('/contacts.txt', 'r', encoding = "utf8") as c:
    contacts = [contact.strip() for contact in c.readlines()]

#region Messages
mensagem1 = "Each message in global variables"
#endregion

def findContact(contact):
    searchField = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    contactFounded = '//span[@title="' + contact + '"]'
    time.sleep(1)
    searchField.click()
    time.sleep(0.5)
    searchField.send_keys(Keys.CONTROL, 'a')
    time.sleep(0.2)
    searchField.send_keys(contact)
    time.sleep(5)
    try:
        wait5.until(EC.presence_of_element_located((
            By.XPATH, contactFounded
        )))
        print("Contato encontrado! [" + contact + "]")
        searchField.send_keys(Keys.ENTER)

        messageField = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
        messageField[1].click()
        print("Escrevendo a mensagem...")
        time.sleep(1)

        #region Sending Messages
        messageField[1].send_keys(mensagem1)
        messageField[1].send_keys(Keys.SHIFT,Keys.ENTER)
        time.sleep(.5)
        #endregion

        messageField[1].send_keys(Keys.ENTER)
        time.sleep(5)
    except:
        print("Contato não encontrado! [" + contact + "]") # Validating contact name
        pass

for contact in contacts:
    findContact(contact)

driver.quit()