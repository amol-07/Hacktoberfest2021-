from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os


PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# last done till main35 gulbarga
# print(url, sno)
driver.get("https://www.justdial.com/Jamnagar/Teachers-For-Academic/nct-10502492")
nameee = "main22"

driver.execute_script("window.scrollTo(0, 1500)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 3000)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 4000)")
time.sleep(3)

driver.execute_script("window.scrollTo(0, 5000)")

time.sleep(2)

driver.execute_script("window.scrollTo(0, 6000)")
time.sleep(2)

driver.execute_script("window.scrollTo(0, 7000)")
time.sleep(1)

driver.execute_script("window.scrollTo(0, 9000)")

driver.execute_script("window.scrollTo(0, 20000)")
time.sleep(3)

storeDetails = driver.find_elements_by_class_name('store-details')
# driver.quit()

def all_city():
    global remain_city
    from bs4 import BeautifulSoup
    import requests
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population"
    html = requests.get(url)

    soup = BeautifulSoup(html.text, 'html.parser')
    tables = soup.find_all("table")

    tables = tables[0]
    city_names = []
    # print(tables)
    rows = tables.find_all('tr')
    express = ['[', ']']
    for row in rows:
        cell = row.find_all('td')

        if len(cell) > 1:
            name = cell[1].text.strip()
            name = ''.join([i for i in name if not i.isdigit()])
            new_name = ""
            for i in name:
                if i not in express:
                    new_name += ''.join(i)
            city_names.append(new_name)

    for i in range(len(city_names)):
        if city_names[i] == "Gulbarga":
            for j in range(i + 1, len(city_names)):
                remain_city.append(city_names[j])
            break


def toExcel(df):
    from openpyxl import load_workbook
    book = load_workbook('teacher1.xlsx')
    with pd.ExcelWriter('teacher1.xlsx', mode='a') as writer:
        writer.book = book
        writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
        print(writer.sheets)
        df.to_excel(writer, sheet_name=nameee, header=False, index=False)


def strings_to_num(argument):
    switcher = {
        'dc': '+',
        'fe': '(',
        'hg': ')',
        'ba': '-',
        'acb': '0',
        'yz': '1',
        'wx': '2',
        'vu': '3',
        'ts': '4',
        'rq': '5',
        'po': '6',
        'nm': '7',
        'lk': '8',
        'ji': '9'
    }

    return switcher.get(argument, "nothing")


