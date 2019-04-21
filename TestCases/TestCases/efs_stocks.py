import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class stocks(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/suji/Desktop/Swetha/MSD-8210/TestCases/chromedriver 2')

    def testcase(self):
        user = "testuser"
        pwd = "Teampswd1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
# login
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/")
        assert "Hello"
        time.sleep(2)


        #Stocks
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[4]/a").click()
        time.sleep(2)

        #add stock
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys("12056")
        elem = driver.find_element_by_id("id_symbol")
        elem.send_keys("test")
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("test")
        elem = driver.find_element_by_id("id_shares")
        elem.send_keys("1000")
        elem = driver.find_element_by_id("id_purchase_price")
        elem.send_keys("100")
        #elem = driver.find_element_by_id("id_purchase_date")
        #elem.send_keys("2019-04-21")
        time.sleep(4)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(4)


        # edit
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[7]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_symbol")
        elem.send_keys("google test")
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(2)


        # delete
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()




