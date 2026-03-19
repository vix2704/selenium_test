# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# # #QUESTION 1
# driver.get("https://demowebshop.tricentis.com")
#
# driver.find_element(By.LINK_TEXT, "Books").click()
# sleep(2)
#
# driver.find_element(By.XPATH, "(//input[@value='Add to cart'])[1]").click()
# sleep(2)
#
# driver.find_element(By.LINK_TEXT, "Shopping cart").click()
# sleep(2)
#
# cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart-item-row")
#
# if len(cart_items) > 0:
#     print("Product present in cart")
#
# sleep(5)
# #----------
#
# # #QUESTION 2
# driver.get("https://demowebshop.tricentis.com")
#
# driver.find_element(By.LINK_TEXT, "Electronics").click()
# sleep(2)
#
# driver.find_element("xpath","//a[contains(text(),'Cell phones')]").click()
#
# sleep(5)
# #----------
#
# # #QUESTION 3
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
#
# driver.find_element("xpath","//button[text()='Start']").click()
# sleep(5)
#
# text = driver.find_element("xpath","//h4[text()='Hello World!']")
# print(text.text)
#
# sleep(5)
# #----------
#
# # #QUESTION 4
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
#
# driver.find_element("xpath","//button[text()='Remove']").click()
# sleep(5)
#
# driver.find_element("xpath","//button[text()='Add']").click()
#
# sleep(5)
# #----------
#
# # #QUESTION 5
# driver.get("https://demoqa.com/select-menu")
#
# driver.find_element("xpath","//div[text()='Select Value']").click()
# sleep(2)
#
# driver.find_element("xpath","//div[text()='Group 2, option 1']").click()
#
# selected = driver.find_element("xpath","//div[contains(@class,'singleValue')]")
# print(selected.text)
#
# sleep(5)
# #----------
#
# # #QUESTION 6
# driver.get("https://demoqa.com/select-menu")
# sleep(2)
#
# options = driver.find_elements("xpath","//select[@id='cars']/option")
#
# for op in options:
#     if op.text in ["Volvo","Saab","Opel"]:
#         op.click()
#
# sleep(2)
#
# for op in options:
#     if op.is_selected():
#         print(op.text)
#
# sleep(5)
# #----------
#
# # #QUESTION 7
# driver.get("https://demoqa.com/menu/")
#
# actions = ActionChains(driver)
#
# main2 = driver.find_element("xpath","//li[text()='Main Item 2']")
# actions.move_to_element(main2).perform()
# sleep(2)
#
# subsub = driver.find_element("xpath","//li[text()='SUB SUB LIST']")
# actions.move_to_element(subsub).perform()
# sleep(2)
#
# subitem = driver.find_element("xpath","//li[text()='Sub Sub Item 1']")
# subitem.click()
#
# sleep(5)
# #----------
#
# # #QUESTION 8
# driver.get("https://demoqa.com/droppable")
#
# actions = ActionChains(driver)
#
# drag = driver.find_element("xpath","//div[@id='draggable']")
# drop = driver.find_element("xpath","//div[@id='droppable']")
#
# actions.drag_and_drop(drag, drop).perform()
#
# result = driver.find_element("xpath","//div[@id='droppable']/p")
# print(result.text)
#
# sleep(5)
# #----------
#
# # #QUESTION 9
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# driver.find_element("xpath","//button[text()='Click for JS Confirm']").click()
# sleep(2)
#
# alert = driver.switch_to.alert
# alert.accept()
#
# result = driver.find_element(By.ID,"result").text
# print(result)
#
# sleep(5)
# #----------
#
# # #QUESTION 10
# driver.get("https://the-internet.herokuapp.com/upload")
#
# file_path = ""C:\Users\KIIT\Desktop\hi.text.docx""
#
# driver.find_element(By.ID,"file-upload").send_keys(file_path)
# sleep(2)
#
# driver.find_element(By.ID,"file-submit").click()
# sleep(2)
#
# uploaded = driver.find_element(By.ID,"uploaded-files").text
# print(uploaded)
#
# sleep(5)
# #----------
#
# # #QUESTION 11
# driver.get("https://the-internet.herokuapp.com/download")
#
# driver.find_element("xpath","(//a)[1]").click()
#
# print("File download triggered")
#
# sleep(5)

##-----------------
# #QUESTION 12
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Books").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[1]").click()
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,"Shopping cart").click()
# time.sleep(2)
# products=driver.find_elements(By.XPATH,"//td[@class='product']/a")
# print("2 products added" if len(products)==2 else "Not correct")
# driver.quit()
#
# #Q13-->
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# driver=webdriver.Chrome()
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"Books").click()
# time.sleep(3)
# books=driver.find_elements(By.XPATH,"//div[@class='product-item']")
# for b in books:
#     price=float(b.find_element(By.CLASS_NAME,"price").text.replace("$",""))
#     if price<20:
#         b.find_element(By.XPATH,".//input[@value='Add to cart']").click()
#         time.sleep(1)
# driver.quit()

#################################################################################