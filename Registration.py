from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
driver = webdriver.Firefox()
driver.get("https://www.litecart.net/account/create")

driver.find_element_by_name("alias").clear()
driver.find_element_by_name("alias").send_keys("mv9895555@gmail.com")

driver.find_elements_by_name("password")[1].clear()
driver.find_elements_by_name("password")[1].send_keys("password")

select = Select(driver.find_element_by_name("role"))
# select.select_by_index(index)
# select.select_by_visible_text("text")
select.select_by_value("Developer")

select = Select(driver.find_element_by_name("zone_code"))
# select.select_by_index(index)
# select.select_by_visible_text("text")
select.select_by_visible_text("Illinois")


checked = driver.find_element_by_name("newsletter").is_selected()
if checked == False:
    driver.find_element_by_name("newsletter").click()

#same for uncheck checkbox, dependes if the element was checked/unchecked before

select = Select(driver.find_element_by_name("country_code"))
# select.select_by_index(index)
# select.select_by_visible_text("text")
select.select_by_value("TG")

driver.find_element_by_name("create_account").click()
