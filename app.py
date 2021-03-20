from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import yaml
import datetime as dt


def main():
    # get credentials
    with open(r'config\account-credentials.yaml') as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)

    # variables
    email = cfg['email']
    password = cfg['password']
    time_slot = cfg['preferred_time_slot']
    location = cfg['location']
    booking_date = get_booking_date(9)
    path = r'C:\Program Files\Google\chromedriver.exe'
    driver = webdriver.Chrome(path)

    driver.get('https://ymcaywca.legendonlineservices.ca/enterprise/account/login')
    time.sleep(3)

    search = driver.find_element_by_id('account-login-email')
    search.send_keys(email)

    search = driver.find_element_by_id('account-login-password')
    search.send_keys(password)
    time.sleep(0.5)

    search.send_keys(Keys.RETURN)
    time.sleep(1)

    driver.get('https://ymcaywca.legendonlineservices.ca/enterprise/bookingscentre/index')
    time.sleep(3)

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

    btn = driver.find_element_by_class_name('btn-success').click()
    time.sleep(1)

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

    select_workout = driver.find_elements_by_xpath('//*[@id="bookingPage"]/bookings-timetable/div/div[10]/a/div/div/div[1]/div[1]')[0]
    select_workout.click()
    time.sleep(1)

    add_to_basket = driver.find_elements_by_xpath('//*[@id="timeTableDetails"]/div/div/div[4]/button[3]')[0]
    add_to_basket.click()
    time.sleep(30)

    driver.quit()


def get_booking_date(delta):
    booking_date = dt.date.today() + dt.timedelta(days=delta)
    print(booking_date)
    booking_date = booking_date.strftime('%B %d, %Y')
    return booking_date

if __name__ == '__main__':
    main()