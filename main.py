""" GlobalStats GTD Update Automation Script

   * to test the program run: $ python3 main.py test
   * monthly update: $ python3 main.py monthly
   * weekly update: $ python3 main.py weekly

    author: Ashraf Minhaj
    mail  : minhaj@programming-hero.com 
"""


"""
pip3 install selenium
pip3 install webdriver_manager
pip3 install pyvirtualdisplay
"""

import time
start_time = time.time()  # to calculate execution time

import sys
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pyvirtualdisplay import Display


# all variables here
email_id = ''
password = ''

sign_in_url = 'https://globalstats.io/login'
key = ''

# gtd: Globalstats Tracked Data 
weekly_gdt_key = 'weekly'               # gdt key and id are same
weekly_gdt_short_name = 'wkl'
monthly_gdt_key = 'monthly'
monthly_gdt_short_name = 'mth'

test_gdt_key = 'testly'
test_gdt_short_name = 'tst'

mygames_url = 'https://globalstats.io/endpoints/' + key
weekly_dlt_url = mygames_url + '/gtds/' + weekly_gdt_key
monthly_dlt_url = mygames_url + '/gtds/' + monthly_gdt_key
test_gdt_dlt_url = mygames_url + '/gtds/' + test_gdt_key
gtd_create_url  = mygames_url + '/gtds/create'

# set up logging
logging.basicConfig(
        filename="logs.log",
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')

# unpack argument
logging.info(f'Got {len(sys.argv)} vairables')
gdt = sys.argv[1]
logging.info(f'Operaiton for data:{gdt}')

logging.info('Initialize Virtual Display')
display = Display(visible=0, size=(1366, 768))
display.start()

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')  

logging.info('checking webdriver')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def sign_in():
    """ sign in to the site with given credentials """
    logging.info(f'Sign in attempt {email_id}')
    logging.info('going ' + sign_in_url)
    driver.get(sign_in_url)
    # print("Site title is", driver.title)

    # find email input and pass email id
    logging.info('Email Input')
    email_input = driver.find_element(By.ID, 'email')
    # email_input.click()
    email_input.send_keys(email_id)
    time.sleep(.500)

    # find password input and pass password
    logging.info('Password Input')
    password_input = driver.find_element(By.ID, 'password')
    # password_input.click()
    password_input.send_keys(password)
    time.sleep(.300)

    # find sign in button and click on it
    logging.info('Submit form')
    driver.find_element(By.CLASS_NAME, 'form-horizontal').submit()
    logging.info('Successful sign in')


def delete_gtd(url):
    """ delete data """
    # delete on weekly stat delete button
    logging.info(f'going to delete data {url}')
    driver.get(url)
    time.sleep(1)

    # check purge data checkbox
    logging.info('check purge data checkbox (waiting)')
    purge_check = driver.find_element(By.ID, 'purge')
    # purge_check = WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located((By.ID, 'purge')))
    driver.execute_script("arguments[0].click();", purge_check)
    # purge_check.click()
    logging.info('Purge Checked')

    # click on delete button
    logging.info('Delete data')
    driver.find_element(By.CLASS_NAME, 'form-horizontal').submit()
    logging.info(f'Sucessfully deleted GDT {url}')

def create_new_gtd(key, name, short_name):
    """ create new globalstats tracked data """
    logging.info(f'Creating new GTD by {key}')
    driver.get(gtd_create_url)

    logging.info('Input key')
    key_input = driver.find_element(By.ID, 'key')
    # key_input.click()
    key_input.send_keys(key)
    time.sleep(.500)

    logging.info('Input Name')
    name_input = driver.find_element(By.ID, 'name')
    # name_input.click()
    name_input.send_keys(name)
    time.sleep(.500)

    logging.info('Input short name')
    short_name_input = driver.find_element(By.ID, 'short_name')
    # short_name_input.click()
    short_name_input.send_keys(short_name)
    time.sleep(.200)

    logging.info("Submit - Create new GDT ")
    driver.find_element(By.CLASS_NAME, 'form-horizontal').submit()
    logging.info(f'Sucessfully created new GDT for {name}')
    

if __name__ == '__main__':
    if gdt == 'weekly':
        try:
            sign_in()
            delete_gtd(weekly_dlt_url)
            time.sleep(.600)
            create_new_gtd(key=weekly_gdt_key, name=weekly_gdt_key, short_name=weekly_gdt_short_name)
        except Exception as e:
            logging.exception(e)
    
    if gdt == 'monthly':
        try:
            sign_in()
            delete_gtd(monthly_dlt_url)
            time.sleep(.600)
            create_new_gtd(key=monthly_gdt_key, name=monthly_gdt_key, short_name=monthly_gdt_short_name)
        except Exception as e:
            logging.exception(e)

    if gdt == 'test':
        try:
            sign_in()
            delete_gtd(test_gdt_dlt_url)
            time.sleep(.600)
            create_new_gtd(key=test_gdt_key, name=test_gdt_key, short_name=test_gdt_short_name)
        except Exception as e:
            logging.exception(e)
    
    # sleep(10)

logging.info('Closing Webdriver')
driver.close()
logging.info('Stopping virtual display')
display.stop()

logging.info("Session took %s seconds" % (time.time() - start_time))
logging.info('Session End.\n\n\n')