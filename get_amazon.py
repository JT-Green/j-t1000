from selenium import webdriver
import time

driver = webdriver.Chrome(r'C:\Program Files\Chromedriver\chromedriver.exe')

login_url = r'https://vendorcentral.amazon.com'
reports_url = r'https://vendorcentral.amazon.com/st/vendor/members/analytics/basic/productDetail?ref_=vc_ven-badashboard_subNav'

user = '***'
pw = '***'

driver.get(login_url)

user_field = driver.find_element_by_name('username')
user_field.send_keys(user)

pw_field = driver.find_element_by_name('password')
pw_field.send_keys(pw)

login_btn = driver.find_element_by_id('login-button-container')
login_btn.click()

driver.get(reports_url)
time.sleep(3)

period_btn = driver.find_element_by_xpath('//*[@id="vxa-ab-reporting-period"]/span/span')
period_btn.click()
time.sleep(3)

last_week = driver.find_element_by_xpath('//*[@id="vxa-ab-reporting-period_1"]')
last_week.click()
time.sleep(3)

filter_btn = driver.find_element_by_xpath('//*[@id="a-autoid-1-announce"]/span')
filter_btn.click()
time.sleep(3)

product_filter = driver.find_element_by_xpath('//*[@id="vxa-ab-product-details"]/div[4]/div[5]/div/div[2]/ul/li[2]')
product_filter.click()
time.sleep(3)

books_btn = driver.find_element_by_xpath('//*[@id="lazy-filter-group-product-group"]/div[3]/div[1]/span/div/label/input')
books_btn.click()
time.sleep(3)

try:
    pets_btn = driver.find_element_by_xpath('//*[@id="lazy-filter-group-product-group"]/div[3]/div[3]/span/div/label/input')
    pets_btn.click()
    time.sleep(3)
except:
    pass

export_btn = driver.find_element_by_xpath('//*[@id="a-autoid-27-announce"]')
export_btn.click()
time.sleep(3)

csv_btn = driver.find_element_by_xpath('//*[@id="vxa-ab-export-selector_1"]')
# Exports Amazon_TW
csv_btn.click()


period_btn.click()
time.sleep(3)

ytd = driver.find_element_by_xpath('//*[@id="vxa-ab-reporting-period_7"]')
ytd.click()
time.sleep(3)

export_btn.click()
time.sleep(2)
# Exports Amazon_YTD
csv_btn.click()

product_filter.click()
time.sleep(3)

digital_btn = driver.find_element_by_xpath('//*[@id="lazy-filter-group-product-group"]/div[3]/div[2]/span/div/label/input')
digital_btn.click()

time.sleep(3)
books_btn.click()
time.sleep(3)

try:
    pets_btn.click()
    time.sleep(3)
except:
    pass

export_btn.click()
time.sleep(3)
# Exports Kindle_YTD
csv_btn.click()

period_btn.click()
time.sleep(3)

last_week.click()
time.sleep(3)

export_btn.click()
time.sleep(3)
# Exports Kindle_TW
csv_btn.click()

"""
For after you've downloaded the files

import glob
import os

files = glob.glob("C:\\Users\\jt\\Downloads\\ProductDetails*.csv")
files.sort(key=lambda x: os.path.getmtime(x))
print(files)
print(files[-1])
files.pop(-1)
print(files)

"""
