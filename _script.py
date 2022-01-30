from multiprocessing import  Pool
import multiprocessing as mp, time
import selenium
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import string
import os, platform
import urllib
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(900, 950)



#num = input('How Many Products you want to scrap? ')
num = 100000
print('It is:-',num)
num = int(num)


url = 'https://shopup.com.bd/r'
driver.get(url)
time.sleep(2)
driver.execute_script("window.scrollTo(0, 5000)")
time.sleep(2)
def scroll_down():
                dialog = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > section > div:nth-child(2) > div.feed-grid-main > div > div.feed-grid-container > ul > li > div > a > img')
                last_scroll_height = 0

                while True:
                    reviews = driver.find_elements_by_css_selector("#content > div > div.page-body > div > div > div > section > div:nth-child(2) > div.feed-grid-main > div > div.feed-grid-container > ul > li > div > a")
                    time.sleep(2)
                    driver.execute_script("arguments[0].scrollIntoView();", reviews[-1])
                    time.sleep(2)
                    scroll_height = driver.execute_script("return arguments[0].scrollHeight;", dialog)
                    if scroll_height == last_scroll_height:
                        break
                    else:
                        last_scroll_height = scroll_height



def scrap():
    try:
    scroll_down()
    time.sleep(2)
except:
    pass
Dib = {}
gb=pd.DataFrame(data=Dib,index=[0], columns=['Page Link','Product Name', 'Image Path', 'Price','Size', 'SKU', 'CATEGORY', 'SUB-CATEGORY','INFO 1','INFO 2','INFO 3','INFO 4','INFO 5','INFO 6','INFO 7'])

i = 0
w = 0
for w in range(num):
    try:
        itm = driver.find_elements_by_css_selector('#content > div > div.page-body > div > div > div > section > div:nth-child(2) > div.feed-grid-main > div > div.feed-grid-container > ul > li > div > a')[i]
        itm = itm.get_attribute('href')
        driver.execute_script("window.open('');")
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[1])
        driver.get(itm)
        time.sleep(2)

        try:
            nam = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > h1')
            nam = nam.text
        except:
            nam = 'Not Available'

        try:
            # get the image source
            img = driver.find_element_by_xpath('//*[@id="pdpMainImage"]')
            src = img.get_attribute('src')
            # download the image
            s = 1
            d = nam + '_' + str(s) + '.jpg'
            data = urllib.request.urlretrieve(src, d)
            path = d
            time.sleep(3)
        except:
            path = 'Not Available'

        try:
            tk = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div:nth-child(1) > h2 > span')
            tk = tk.text
        except:
            tk = 'Not Available'

        time.sleep(2)

        try:
            size = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.available-sizes.mrvoonik-available-sizes > ul')
            size = size.text
        except:
            size = 'Not Available'

        try:
            sku = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > ul > li:nth-child(1) > div.value')
            sku = sku.text
        except:
            sku = 'Not Available'

        try:
            category = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > ul > li:nth-child(2) > div.value > a > span:nth-child(3)')
            category = category.text
        except:
            category = 'Not Available'
        try:
            subc = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > ul > li:nth-child(3) > div.value > a')
            subc = subc.text
        except:
            subc = 'Not Available'

        try:
            info1 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(3)')
            info1= info1.text
        except:
            info1 = 'Not Available'

        try:
            info2 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(4)')
            info2= info2.text
        except:
            info2 = 'Not Available'

        try:
            info3 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(7)')
            info3= info3.text
        except:
            info3 = 'Not Available'

        try:
            info4 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(8)')
            info4= info4.text
        except:
            info4 = 'Not Available'

        try:
            info5 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(9)')
            info5= info5.text
        except:
            info5 = 'Not Available'
        time.sleep(1)

        try:
            info6 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(10)')
            info6= info6.text
        except:
            info6 = 'Not Available'

        try:
            info7 = driver.find_element_by_css_selector('#content > div > div.page-body > div > div > div > div > div > div > div:nth-child(2) > div > div.pdp-det-box.product-properties > p:nth-child(11)')
            info7= info7.text
        except:
            info7 = 'Not Available'
            
        Dib = {'Page Link':itm,'Product Name':nam, 'Image Path':path, 'Price':tk,'Size':size, 'SKU':sku, 'CATEGORY':category, 'SUB-CATEGORY':subc,'INFO 1':info1,'INFO 2':info2,'INFO 3':info3,'INFO 4':info4,'INFO 5':info5,'INFO 6':info6,'INFO 7':info7}
        gb = gb.append(Dib, ignore_index=True)
        print(gb)
        gb.to_excel('SHOPUP.xlsx')
        i = i+1
        w = w+1
        driver.close()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])
    except:
        i = i+1
        w = w+1
        try:
            scroll_down()
            time.sleep(2)
        except:
            pass
        continue