from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

# مسیر Edge WebDriver را وارد کنید
service = Service('E:/APP/Microsoft Edge WebDriver/msedgedriver.exe')
driver = webdriver.Edge(service=service)

# آدرس صفحه را وارد کنید
driver.get('https://sdhm.pw/bonus')

# چند ثانیه صبر کن تا صفحه کامل لود شود
time.sleep(5)

# همه دکمه‌ها را پیدا و متن‌شان را چاپ کن
buttons = driver.find_elements(By.TAG_NAME, "button")
for i, btn in enumerate(buttons):
    print(f"Button {i}: '{btn.text}'")

# برنامه را باز نگه می‌دارد تا خروجی را ببینی
input("Check the button texts above and press Enter to continue...")

while True:
    try:
        # پیدا کردن لینک با کلاس button و متن Get money
        links = driver.find_elements(By.XPATH, "//a[contains(@class, 'button') and contains(text(), 'Get money')]")
        if links:
            links[0].click()
            print("Clicked!")
        else:
            print("'Get money' link not found.")
    except Exception as e:
        print("Error:", e)
    time.sleep(65)  # ۶۵ ثانیه صبر می‌کند
    driver.refresh()  # بعد از ۶۵ ثانیه صفحه را رفرش کن
    print("Page refreshed.")