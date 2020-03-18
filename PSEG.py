 selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://nj.pseg.com/")
#                                               assert "Python" in driver.title
elem = driver.find_element_by_id("usernamePublic")
elem.clear()
elem.send_keys("juliomoran0923")
elem = driver.find_element_by_id("passwordPublic")
elem.clear()
elem.send_keys("straqualursi2013")
elem.send_keys(Keys.RETURN)
# tag = driver.find_element_by_xpath('//h2').click()

'''if float(owed) > 0.00:
    print("Pay Bill")
else:
    print("You are paid in full")
'''