import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class investment(unittest.TestCase):

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

        # investments
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[3]/a").click()
        time.sleep(2)

        #add investment
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys("12056")
        elem = driver.find_element_by_id("id_category")
        elem.send_keys("test")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("test")
        elem = driver.find_element_by_id("id_acquired_value")
        elem.send_keys("100")
        elem = driver.find_element_by_id("id_recent_value")
        elem.send_keys("100")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(2)

        # edit investment
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[1]/td[8]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_category")
        elem.send_keys("test")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/form/button").click()
        time.sleep(2)


        # delete investment
        elem = driver.find_element_by_xpath("//*[@id=\"app-layout\"]/div/div/div/div[3]/table/tbody/tr[8]/td[9]/a").click()
        time.sleep(2)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()






