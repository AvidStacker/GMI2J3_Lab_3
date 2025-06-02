import time
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Kontrollerar att alert visar rätt text för primtal/icke-primtal
def check_alert(num, text):
    if num in [10, 12, 14, 15, 16, 18]:
        if "true" in text.lower():
            raise ValueError(f"{num} should NOT be prime!")
    elif num in [11, 13, 17, 19]:
        if "false" in text.lower():
            raise ValueError(f"{num} SHOULD be prime!")

# Startar Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('C:/Users/ilage/Documents/GitHub/GMI2J3_Lab_3/Part3/Lab3SeleniumMocking/Javascript/prime-assert.html')

# Väntar tills knappen finns
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'inpbtn')))

# Hittar inputfältet
input_field = driver.find_element(By.ID, 'primeinput')

# Sätter sökvägen till loggfilen baserat på skriptets plats
script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "testlogg.txt")

# Öppnar loggfil
with open(log_path, "w", encoding="utf-8") as log_file:
    log_file.write(f"Testkörning: {datetime.now()}\n")
    log_file.write("Nummer\tAlerttext\tStatus\n")

    # Loopar igenom tal 10 till 19
    for number in range(10, 20):
        input_field.send_keys(str(number))
        submit_button = driver.find_element(By.ID, 'inpbtn')
        submit_button.click()

        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            status = "PASS"
            try:
                check_alert(number, alert_text)
            except Exception as ex:
                status = f"FAIL: {ex}"
            log_file.write(f"{number}\t{alert_text}\t{status}\n")
            print(f"{number}: {alert_text} => {status}")
            alert.accept()
        except NoAlertPresentException:
            log_file.write(f"{number}\tNo alert present\tFAIL\n")
            print(f"{number}: No alert present => FAIL")

        input_field.clear()

# Stänger webbläsaren
driver.quit()
