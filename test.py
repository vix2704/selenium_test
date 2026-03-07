from selenium.webdriver import Chrome, ChromeOptions
o=ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#question1: 	Open Amazon and print all category names
driver.get("https://amazon.in")
sleep(3)
a=driver.find_elements("xpath","//div[@class='nav-div']")
for i in a:
    print(i.text)

#question2:  Print top 10 movie names from IMDB Top 250
driver.get("https://www.imdb.com/chart/top/")
sleep(3)
movies = driver.find_elements("xpath", "//h3[@class='ipc-title__text']")
for movie in movies[:10]:
    print(movie.text)

#question3: 	Count all images on amazon
driver.get("https://www.amazon.in")
sleep(4)
a=driver.find_elements("tag name","img")
print(len(a))
#output=199

#question 4:   Target first dropdown in that page and select first option
driver.get('https://demoqa.com/select-menu')
sleep(2)
e=driver.find_element('xpath','//input[@id="react-select-2-input"]')
e.click()
sleep(1)
driver.find_element(By.XPATH,'//div[text()="Group 1, option 1"]').click()

#question 5: Print All Links in amazon Page
driver.get("https://www.amazon.in")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")

for i in links:
    print(i.get_attribute("href"))

#question6: Print Auto Suggestions of any site
driver.get("https://www.amazon.in/")
sleep(10)
driver.find_element("id","twotabsearchtextbox").send_keys("samsung")
sleep(5)
a=driver.find_elements("xpath","//div[@class='s-suggestion-container']")
for i in a:
    print(i.text)

#question 7: From the “Accounts & Lists” section on the Amazon homepage, select the “Your Wish List” option.
driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(3)
account = driver.find_element(By.ID, "nav-link-accountList")
actions = ActionChains(driver)
actions.move_to_element(account).perform()
sleep(2)
driver.find_element(By.LINK_TEXT, "Your Wish List").click()

#question 8: Access the content displayed inside the embedded page and print the heading text visible inside it.
driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.maximize_window()
sleep(2)
driver.switch_to.frame("iframeResult")
title = driver.find_element(By.TAG_NAME, "h2").text
print(title)


#question 9:	Search Laptop and print all product titles.
driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_element("id", "twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
a = driver.find_elements("xpath", "//h2//span")
for i in a:
    print(i.text)

#########################################################################
