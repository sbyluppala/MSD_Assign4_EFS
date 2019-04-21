import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class customer(unittest.TestCase):

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


        #customers
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()

        #edit
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[9]/a").click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Test")
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()






