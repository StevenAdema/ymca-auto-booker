from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import yaml
import datetime as dt


def main():
    # get credentials
    with open(r'config\config.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    # create web driver for Heroku app
    chrome_optinos = webdriver.ChromeOptions()
    chrom_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver =  webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    
    # variables
    email = cfg['email']
    password = cfg['password']
    location = cfg['location']
    time_slot = get_time_slot(cfg)
    # booking_date = get_booking_date(9)
    booking_date = 'April 01, 2021'
    path = cfg['chrome_driver_path']
    # driver = webdriver.Chrome(path)

    driver.get('https://ymcaywca.legendonlineservices.ca/enterprise/account/login')
    time.sleep(3)

    # login to YMCA
    search = driver.find_element_by_id('account-login-email')
    search.send_keys(email)
    search = driver.find_element_by_id('account-login-password')
    search.send_keys(password)
    time.sleep(0.5)
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    # open booking page and select location, workout
    driver.get('https://ymcaywca.legendonlineservices.ca/enterprise/bookingscentre/index')
    time.sleep(3.5)
    select = driver.find_element_by_class_name('select2-search__field')
    select.send_keys(location)
    time.sleep(0.5)
    select.send_keys(Keys.RETURN)
    time.sleep(1)
    radio = driver.find_element_by_id('booking-behaviour-option373')
    radio.click()
    time.sleep(1)
    checkbox = driver.find_element_by_id('booking-activity-option0372')
    checkbox.click()
    time.sleep(1)
    btn = driver.find_element_by_class_name('btn-success')
    btn.click()
    time.sleep(1)

    # select workout date and slot
    booking = driver.find_element_by_id('unique-identifier-2')
    time.sleep(0.5)
    booking.send_keys(Keys.CONTROL + 'a')
    time.sleep(0.5)
    booking.send_keys(Keys.DELETE)
    time.sleep(0.5)
    booking.send_keys(booking_date)
    time.sleep(0.5)
    booking.send_keys(Keys.RETURN)
    time.sleep(1)
    select_workout = driver.find_elements_by_xpath(time_slot)[0]
    select_workout.click()
    time.sleep(1)

    # add to cart
    add_to_basket = driver.find_elements_by_xpath('/html/body/div[1]/div[2]/div/div/bookings-timetable/timetable-item-details/div/div/div/div[4]/button[3]')[0]
    add_to_basket.click()
    time.sleep(5)

    basket = driver.find_elements_by_xpath('/html/body/div/div[2]/div/universal-basket-summary/div[2]/form/div[2]/div[2]/universal-basket-options/universal-basket-continue-options/button[1]')[0]
    basket.click()
    time.sleep(2)

    terms_checkbox = driver.find_element_by_xpath('/html/body/div/div[2]/div/universal-basket-summary/div[2]/form/div[2]/div[1]/div[4]/universal-basket-payment-details/div/div/div[4]/universal-basket-terms-conditions/ul/li/div[1]/label/input')
    terms_checkbox.click()
    time.sleep(10)

    # close driver
    driver.quit()


def get_time_slot(cfg):
    ''' Convert the preferred time slot to the appropriate div from the web form '''
    preferred_time_slot = cfg['preferred_time_slot']
    time_slot_div = str(cfg['timeslots_dict'][preferred_time_slot])
    time_slot_xpath = '/html/body/div[1]/div[2]/div/div/bookings-timetable/div/div[' + time_slot_div + ']'
    return time_slot_xpath


def get_booking_date(delta):
    ''' Add 7 days to today's date in the appropriate format '''
    booking_date = dt.date.today() + dt.timedelta(days=delta)
    booking_date = booking_date.strftime('%B %d, %Y')
    return booking_date


if __name__ == '__main__':
    main()