import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver_path = '/Users/Sheprata/PycharmProjects/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://automationpractice.com/')
driver.find_element_by_class_name("login").click()
driver.find_element_by_id("email_create").send_keys("cpratastha2012@gmail.com")
driver.find_element_by_id("SubmitCreate").click()

# Registration form
time.sleep(3)
driver.find_element_by_css_selector("#id_gender1").click()
driver.find_element_by_xpath("//input[@id='customer_firstname']").send_keys("Sheprata")
driver.find_element_by_xpath("//input[@id='customer_lastname']").send_keys("Shrestha")
driver.find_element_by_xpath("//input[@id='email']").send_keys("cpratastha2012@gmail.com")
driver.find_element_by_xpath("//input[@id='passwd']").send_keys("Welcome01")
Select(driver.find_element_by_css_selector("#days")).select_by_index(2)
Select(driver.find_element_by_css_selector("#months")).select_by_index(2)
Select(driver.find_element_by_css_selector("#years")).select_by_index(2)
driver.find_element_by_xpath("//input[@id='firstname']").send_keys("Sheprata")
driver.find_element_by_xpath("//input[@id='lastname']").send_keys("Shrestha")
driver.find_element_by_xpath("//input[@id='address1']").send_keys("Jorpati")
driver.find_element_by_xpath("//input[@id='city']").send_keys("Kathmandu")
Select(driver.find_element_by_xpath("//select[@id='id_state']")).select_by_index(2)
driver.find_element_by_xpath("//input[@id='postcode']").send_keys("44600")
Select(driver.find_element_by_xpath("//select[@id='id_country']")).select_by_index(1)
driver.find_element_by_xpath("//input[@id='phone_mobile']").send_keys("9841018945")
driver.find_element_by_xpath("//input[@id='alias']").send_keys("test")
driver.find_element_by_xpath("//button[@id='submitAccount']").click()
