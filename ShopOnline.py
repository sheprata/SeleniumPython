from selenium import webdriver

driver_path = '/Users/Sheprata/PycharmProjects/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://automationpractice.com/')

# we have to login before shopping. Tried logging manually first and then it did not let me sign out at all
# tried multiple times clearing history cache as well.
# It was in signed in mode so was not able to write login code as I could not inspect.

category1 = driver.find_element_by_xpath("//a[@class='sf-with-ul'][contains(text(),'Dresses')]")
driver.execute_script("arguments[0].click();", category1)
driver.implicitly_wait(10)
addToChart_category1 = driver.find_element_by_xpath("//a[@class='button ajax_add_to_cart_button btn btn-default']["
                                                    "@data-id-product='3']/span[contains(text(),'Add to cart')]")
driver.execute_script("arguments[0].click();", addToChart_category1)
driver.implicitly_wait(10)

continueShopping = driver.find_element_by_xpath("//span[@class='continue btn btn-default button exclusive-medium']")
driver.execute_script("arguments[0].click();", continueShopping)
driver.implicitly_wait(10)

category2 = driver.find_element_by_xpath("//li[@class='sfHoverForce']")
driver.execute_script("arguments[0].click();", category2)
addToChart_category2 = driver.find_element_by_xpath("//a[@class='button ajax_add_to_cart_button btn btn-default']["
                                                    "@data-id-product='1']/span[contains(text(),'Add to cart')]")
driver.execute_script("arguments[0].click();", addToChart_category2)
driver.implicitly_wait(10)

checkout = driver.find_element_by_xpath(
    "//a[@class='btn btn-default button button-medium']/span[contains(text(),'Proceed to checkout')]")
driver.execute_script("arguments[0].click();", checkout)
driver.implicitly_wait(10)

proceedCheckout = driver.find_element_by_xpath(
    "//a[@class='button btn btn-default standard-checkout button-medium']/span[contains(text(),'Proceed to checkout')]")
driver.execute_script("arguments[0].click();", proceedCheckout)
driver.implicitly_wait(10)

proceedAddress = driver.find_element_by_xpath("//button[@name='processAddress']")
driver.execute_script("arguments[0].click();", proceedAddress)
driver.implicitly_wait(10)

checkTerms = driver.find_element_by_xpath("//input[@id='cgv']").get_attribute('checked')

processCarrier = driver.find_element_by_xpath("//button[@name='processCarrier']")
driver.execute_script("arguments[0].click();", processCarrier)
