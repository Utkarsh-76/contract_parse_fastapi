from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from datetime import datetime
import os
from parsing_code.file_name_log import copy_pdfs
from dir_path import base_dirname
from parsing_code.utilities import empty_temp_folder
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def extract_links(category_code, sol_type, category='ert', scrapping_type='incr'):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--headless")
    chrome_driver_path = os.path.join(base_dirname, "chromedriver")
    service = Service(chrome_driver_path)

    driver = webdriver.Chrome(options=chrome_options, service=service)

    driver.get("ABC")
    time.sleep(0.5)
    submit_button = driver.find_element("xpath", "//input[@type='submit']")
    submit_button.click()
    time.sleep(0.5)

    rfq_button = driver.find_element("xpath", "(//*[contains(@class, 'linkwhite')])[3]")
    rfq_button.click()
    time.sleep(0.5)

    select_element = Select(driver.find_element("xpath", "//select[@id='ctl00_cph1_ddlScope']"))
    if scrapping_type == 'hist':
        select_element.select_by_value("all")
    else:
        select_element.select_by_value("recent")

    if category == 'abc':

        select_element = Select(driver.find_element("xpath", "//select[@id='ctl00_cph1_ddlCategory']"))
        select_element.select_by_value("ert")

        search_value_textbox = driver.find_element("xpath", "//*[@id='ctl00_cph1_txtValue']")
        cat_codes = ','.join(category_code)
        search_value_textbox.send_keys(cat_codes)

    elif category == 'xyz':

        select_element = Select(driver.find_element("xpath", "//select[@id='ctl00_cph1_ddlCategory']"))
        select_element.select_by_value("cage")

        search_value_textbox = driver.find_element("xpath", "//*[@id='ctl00_cph1_txtValue']")
        cat_codes = ','.join(category_code)
        search_value_textbox.send_keys(cat_codes)

    if 'qwe' in sol_type:
        sb_checkbox = driver.find_element("xpath", "//*[@id='ctl00_cph1_chkS']")
        sb_checkbox.click()

    if 'rty' in sol_type:
        sdvosb_checkbox = driver.find_element("xpath",
                                              "//*[@id='ctl00_cph1_chkB']")
        sdvosb_checkbox.click()

    if 'asd' in sol_type:
        combine_checkbox = driver.find_element("xpath", "//*[@id='ctl00_cph1_chkC']")
        combine_checkbox.click()

    time.sleep(0.5)

    search_button = driver.find_element("xpath", "//*[@id='ctl00_cph1_butDbGo']")
    search_button.click()
    time.sleep(0.5)

    page_selector = driver.find_elements(By.CSS_SELECTOR, "tr.pagination table td")
    if len(page_selector) > 0:
        last_page_element = page_selector[-1].find_element('xpath', 'a')
        if last_page_element.text == 'Last':
            last_page_element.click()
            time.sleep(0.5)

    last_page_selector = driver.find_elements(By.CSS_SELECTOR, "tr.pagination table td")
    if len(last_page_selector) > 0:
        total_pages_count = int(last_page_selector[-1].find_element('xpath', './/a | .//span').text)
        page_list_count = int(total_pages_count/10) if total_pages_count%10 != 0 else int(total_pages_count/10) - 1
    else:
        total_pages_count = 1
        page_list_count = 0

    if page_list_count > 0:
        last_page_selector[0].find_element('xpath', 'a').click()

    print(total_pages_count)
    print(page_list_count)

    all_page_links = []

    for p in range(page_list_count + 1):

        current_page_selector = driver.find_elements(By.CSS_SELECTOR, "tr.pagination table td")
        current_page_selector = current_page_selector[:(int(len(current_page_selector) / 2))]
        pages_count = min(len(current_page_selector), 10)

        if pages_count == 0:
            pages_count = 1

        print(pages_count)

        links = []

        for i in range(pages_count):
            if p*10+i == total_pages_count:
                break
            if i > 0:
                page_selector = driver.find_elements(By.CSS_SELECTOR, "tr.pagination table td")
                if page_selector[0].find_element('xpath', './/a | .//span').text == 'First':
                    page_id = i+2
                else:
                    page_id = i
                page_element = page_selector[page_id].find_element('xpath', 'a')
                page_element.click()
                time.sleep(0.5)

            bg_white_list = driver.find_elements(By.CLASS_NAME, 'BgWhite')
            links_1 = []
            for element in bg_white_list:
                links_1.append((element.find_element('xpath', 'td[5]/span/a').get_attribute('href'),
                                element.find_element('xpath', 'td[8]/span').text,
                                element.find_element('xpath', 'td[3]/span').text,
                                element.find_element('xpath', 'td[5]/span/img').get_attribute('alt')))
            bg_silver_list = driver.find_elements(By.CLASS_NAME, 'BgSilver')
            links_2 = []
            for element in bg_silver_list:
                links_2.append((element.find_element('xpath', 'td[5]/span/a').get_attribute('href'),
                                element.find_element('xpath', 'td[8]/span').text,
                                element.find_element('xpath', 'td[3]/span').text,
                                element.find_element('xpath', 'td[5]/span/img').get_attribute('alt')))

            links = links + links_1 + links_2

        all_page_links = all_page_links + links

        next_page_list_selector = driver.find_elements(By.CSS_SELECTOR, "tr.pagination table td")
        if page_list_count != p:
            next_page_list_selector[-2].find_element('xpath', 'a').click()
            time.sleep(0.5)

    driver.quit()

    return all_page_links


def download_pdfs(start_date, links, date_folder, log_file):

    # temp_folder = os.path.join(base_dirname, 'data', 'temp')

    # chrome_options = Options()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument("--headless")
    # prefs = {"download.default_directory": temp_folder}
    # chrome_options.add_experimental_option("prefs", prefs)

    # chrome_driver_path = os.path.join(base_dirname, "chromedriver")
    # service = Service(chrome_driver_path)

    doc_type_dict = {}

    for link in links:

        issue_date = datetime.strptime(link[1], '%m-%d-%Y').date()
        if issue_date >= start_date:
            # print(link[0])
            # print(link[1])
            # print(link[2])
            # print(link[3])
            doc_type_dict[link[0].split('/')[-1]] = link[3]
            # driver = webdriver.Chrome(options=chrome_options, service=service)
            # driver.get(link[0])
            # time.sleep(0.5)
            # submit_button = driver.find_element("xpath", "//input[@type='submit']")
            # submit_button.click()
            # time.sleep(20)
            # driver.quit()

    # copy_pdfs(temp_folder, date_folder, log_file)
    # empty_temp_folder()

    return doc_type_dict
