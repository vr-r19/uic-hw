import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

browser = webdriver.Firefox()
def Qidirsh(item):
    browser.get('https://uzum.uz')
    time.sleep(5)
    # try:    
    #     city=browser.find_element(By.CLASS_NAME, "city").click()
    # except:
    #     pass
    qidirish=browser.find_element(By.CLASS_NAME, "default-input")
    ActionChains(browser)\
        .send_keys_to_element(qidirish, item)\
        .perform()
    searchbutton =browser.find_element(By.CLASS_NAME, "search-button")
    searchbutton.click()
# def narx_filtr(min):
#     mini=browser.find_element(By.ID, '#input-text8222')
#     ActionChains(browser)\
#         .send_keys_to_element(mini, min)\
#         .perform()
#     # maxi=browser.find_element(By.CSS_SELECTOR, '#input-text8224')
#     # ActionChains(browser)\
#     #     .send_keys_to_element(maxi, max)\
#     #     .perform()
while True:
    command='Qidirish'
    try:
        if command == "Qidirish":    
            item=input("Tovar nomi: ")
            Qidirsh(item)
            # narx=input("Narx bo'yicha filtr qo'yasizmi? ").capitalize()
            # if narx:
            #     if narx == 'Ha':
            #         min=input("Boshlang'ich narx: ")
            #         narx_filtr(min)
            #     else:
            #         continue
            time.sleep(2)
            try:
                tel=browser.find_element(By.CSS_SELECTOR, "div.col-mbs-12:nth-child(1) > div:nth-child(1) > div:nth-child(1)").click()
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sharxlar=browser.find_element(By.CSS_SELECTOR, 'button.noselect:nth-child(2)').click() 
            except:
               pass
        elif command == "Filter":
            filter_by=input("Bo'yicha filtralash: ")
            if filter_by:
                filter=browser.find_element(By.CSS_SELECTOR, ".sort-select > div:nth-child(2)")
                filter.click()
                if filter_by=="Arzon":
                    arzon=browser.find_element(By.CSS_SELECTOR, "li.noselect:nth-child(2)").click()
                elif filter_by=='Qimmat':
                    qimmatroq=browser.find_element(By.CSS_SELECTOR, "li.noselect:nth-child(3)").click()
                elif filter_by=='Reyting':
                    reyting=browser.find_element(By.CSS_SELECTOR, "li.noselect:nth-child(4)").click()
                elif filter_by=='Soni':
                    soni=browser.find_element(By.CSS_SELECTOR, "li.noselect:nth-child(5)").click()
                elif filter_by=='Kun':
                    kun=browser.find_element(By.CSS_SELECTOR, "li.noselect:nth-child(6)").click()
        elif command == "Exit":
            break
    except:
        print('Choose another website')



        
                