from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://uefa.com/uefachampionsleague/season=2020/clubs/player=250024456/index.html")

elements = len(driver.find_elements_by_css_selector(".player--statistics--list .field"))



statisticsListBlock = driver.find_element_by_class_name("player--statistics--list")
fields = statisticsListBlock.find_elements_by_css_selector(".player--statistics--list .field")

for field in fields:
    label = field.find_element_by_class_name("statistics--list--label").text
    data = field.find_element_by_class_name("statistics--list--data").text
    print(label)
    print(data)               

driver.close()