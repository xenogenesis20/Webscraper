from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from decouple import config
import time

USER = config('USER')
PW = config('PW')

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.genedx.com/signin/")
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='catapultCookie']"))).click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "div#biopeople-login-registration iframe")))
wait.until(EC.element_to_be_clickable((By.ID, "loginEmail"))).send_keys(USER)
wait.until(EC.element_to_be_clickable((By.ID, "passwordEmail"))).send_keys(PW)
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.switch_to.default_content()

try:
    n = 0
    for i in range(2, 23):
        n = i
        report = driver.find_element_by_xpath(f"//tbody/tr[{n}]/td[9]/a[1]/i[1].")
        print(n)
        if report:

            report.click()
            time.sleep(3)
        elif n == 22:
            next_page = driver.find_element_by_link_text("2")
            next_page.click()
except:
    driver.quit()


# close browser after 5 second delay
# time.sleep(5)
# driver.close()