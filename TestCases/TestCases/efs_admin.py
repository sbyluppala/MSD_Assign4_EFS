import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/suji/Desktop/Swetha/MSD-8210/TestCases/chromedriver 2')

    def testcase(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        time.sleep(1)
# login
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem = driver.find_element_by_xpath("//*[@id=\"login-form\"]/div[3]/input").click()
        assert "Hello"
        time.sleep(2)


        #customer

        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[3]/table/tbody/tr[1]/th/a").click()
        time.sleep(2)
        # add customer
        elem = driver.find_element_by_xpath("//*[@id=\"content-main\"]/ul/li/a").click()
        time.sleep(2)

        elem = driver.find_element_by_id("id_name")
        elem.send_keys("test")
        time.sleep(2)
        elem = driver.find_element_by_id("id_address")
        elem.send_keys("4300 Avenida Manana")
        time.sleep(2)
        elem = driver.find_element_by_id("id_cust_number")
        elem.send_keys("12099")
        time.sleep(2)
        elem = driver.find_element_by_id("id_city")
        elem.send_keys("Omaha")
        time.sleep(2)
        elem = driver.find_element_by_id("id_state")
        elem.send_keys("NE")
        time.sleep(2)
        elem = driver.find_element_by_id("id_zipcode")
        elem.send_keys("68124")
        time.sleep(2)
        elem = driver.find_element_by_id("id_email")
        elem.send_keys("ssb@gmail.com")
        time.sleep(2)
        elem = driver.find_element_by_id("id_cell_phone")
        elem.send_keys("3333333334")
        time.sleep(2)

        elem = driver.find_element_by_xpath("//*[@id=\"customer_form\"]/div/div/input[1]").click()
        time.sleep(2)



        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()





