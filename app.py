from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from configparser import ConfigParser

CONFIG = ConfigParser()
CONFIG.read('config.ini')

driver = CONFIG.get('MAIN', 'DRIVER_LOCATION')
email = CONFIG.get('CREDENTIALS', 'USERNAME')
password = CONFIG.get('CREDENTIALS', 'PASSWORD')
url = CONFIG.get('ORDER', 'URL')

print('\nLogging in with username:', email)

driver = webdriver.Chrome(driver)
driver.maximize_window()
driver.get(url)

input('\nConfirm Details & Press Enter to proceed!')


def login():
    try:
        print("Logging In..")
        try:
            login = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._34niwY"))
            )
            print('Logging In')
        except:
            print('Button Not Active')
        login.click()
        print('Login Button Clicked')
    except:
        print('Failed, please check id or password')
        time.sleep(0.5)
        login()


def login_submit():
    try:
        if 'Enter Password' in driver.page_source:
            print('Trying Usual method of Login.')
            email = driver.find_element_by_css_selector(".Km0IJL ._2zrpKA")
            passd = driver.find_element_by_css_selector(".Km0IJL ._3v41xv")
            email.clear()
            passd.clear()
            email.send_keys(email)
            passd.send_keys(password)
            try:
                form = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".Km0IJL ._7UHT_c"))
                )
                print('Submit Button Clickable')
            except:
                print('Submit Button Not Clickable')
            form.click()
        else:
            print('Trying Alternate method of Login.')
            email = driver.find_element_by_css_selector("._2zrpKA")
            email.clear()
            email.send_keys(email)
            loginnext = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
            )
            loginnext.click()
            loginpassword = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".jUwFiZ"))
            )
            loginpassword.click()
            time.sleep(0.5)
            passd = driver.find_elements_by_css_selector("._2zrpKA")[1]
            passd.clear()
            passd.send_keys(password)
            form = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "._1LctnI"))
            )
            form.click()
        print("Logged In Successfully")
    except:
        if ('Login &amp; Signup' not in driver.page_source and 'Login & Signup' not in driver.page_source):
            print('Logged in Manually.')
        else:
            print('login_submit Failed. Please login manually.')
            time.sleep(1)
            login_submit()


def buy_check():
    try:
        nobuyoption = True
        while nobuyoption:
            try:
                driver.refresh()
                time.sleep(0.2)
                buyprod = driver.find_element_by_css_selector("._1k1QCg ._7UHT_c")
                print(' Button Clickable: ' + time.ctime())
                nobuyoption = False
            except:
                nobuyoption = True
                print('Button not Clickable: ' + time.ctime())
        buyprod.click()
        print('Buy Button Clicked Successfully: ' + time.ctime())
        buy_recheck()
    except:
        print('buy_check Failed. Retrying: ' + time.ctime())
        time.sleep(0.5)
        buy_check()


def buy_recheck():
    try:
        WebDriverWait(driver, 4).until(
            EC.title_contains("Secure Payment")
        )
        print('Redirected to Payment')
    except:
        print('Error in Redirecting to Payment')
        time.sleep(0.5)
        buy_check()


def deliver_option():
    try:
        addr_input_final = "//label[@for='" + addr_input + "']"
        try:
            sel_addr = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, addr_input_final))
            )
            print('Address Selection Button Clickable')
        except:
            print('Address Selection Button Not Clickable')
        sel_addr.click()
        print('Address Selection Button Clicked Successfully')
    except:
        print('deliver_option Failed. Retrying.')


def deliver_continue():
    try:
        addr_sal_avl = True
        while addr_sal_avl:
            try:
                address_sel = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
                )
                address_sel.click()
                addr_sal_avl = False
                print('Address Delivery Button Clickable')
            except:
                addr_sal_avl = True
                print('Address Delivery Button Not Clickable')
        print('Address Delivery Button Clicked Successfully')
    except:
        print('deliver_continue Failed. Retrying.')


def order_summary_continue():
    try:
        press_continue = driver.find_element_by_css_selector("._2Q4i61")
        press_continue.click()
        print('Continue Button Clicked Successfully')
    except:
        print('order_summary_continue Failed. Retrying.')
        time.sleep(0.5)
        order_summary_continue()


def choose_payment():
    try:
        pay_opt_input_final = "//label[@for='" + PHONEPAY + "']"
        pay_method_sel = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, pay_opt_input_final)))
        pay_method_sel.click()
        print('Payment Method Selected Successfully')
    except:
        print('choose_payment Failed. Retrying.')
        time.sleep(0.5)
        choose_payment()

def payment_continue():
    try:
        pay = None
        try:
            pay = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "._3K1hJZ ._7UHT_c"))
            )
            print('Pay Button Clickable')
        except:
            print('Pay Button Not Clickable')
        pay.click()
        print('Pay Button Clicked Successfully')
    except:
        print('payment_continue Failed. Retrying.')
        time.sleep(0.5)
        payment_continue()

def run_script():
    login()
    login_submit()
    buy_check()
    order_summary_continue()
    start = time.time()
    print("Start time: {0}".format(start))
    if pay_mode == '1':
        choose_payment()
        payment_continue()
    end = time.time()
    total = end - start
    print("Total time taken: {0}".format(total))


if __name__ == "__main__":
    run_script()
