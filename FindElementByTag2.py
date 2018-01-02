from selenium import webdriver

#create (open) browser
driver = webdriver.Firefox()
driver.get("http://www.humanemulator.net/poligon/input.html")
inputs = driver.find_elements_by_tag_name("input")

for input in inputs:
    name = input.get_attribute("name")
    print(name)
