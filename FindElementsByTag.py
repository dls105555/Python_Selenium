from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.humanemulator.net/poligon/anchor.html#")
anchors = driver.find_elements_by_tag_name("a")
for anchor in anchors:
    href = anchor.get_attribute("href")
    print(anchor.text + "\t" + href)
