from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(r'C:\Program Files\Chromedriver\chromedriver.exe')

url = "http://tme.firebrandtech.com/WPC/Secure/Login.aspx"
username = r"***"
password = r"***"

url2 = "http://tme.firebrandtech.com/WPC/Dialogs/ReportsPopup.aspx?ListKey=12742073&SearchType=6&ReportDataCode=10&ReportDataSubCode=2&ReportDataSub2Code=3&RunReport=true"

if __name__ == "__main__":
    driver.get(url)
    uname = driver.find_element_by_name("TemplateWithSingleContentControl$CC$Login1$txtUserName")
    uname.send_keys(username)

    passw = driver.find_element_by_name("TemplateWithSingleContentControl$CC$Login1$txtPassword")
    passw.send_keys(password)

    login_btn = driver.find_element_by_name("TemplateWithSingleContentControl$CC$Login1$cmdLogin")
    login_btn.click()

    driver.close()
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url2)

    export_btn = driver.find_element_by_id("CrystalReportViewer_toptoolbar_export")
    export_btn.click()

    combobox = driver.find_element_by_class_name('iconnocheck')
    combobox.click()

    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)
    actions.perform()

    export_btn2 = driver.find_element_by_class_name('wizbutton')
    export_btn2.click()

