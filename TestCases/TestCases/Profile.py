import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class renter_reservation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/suji/Desktop/Swetha/MSD-8210/TestCases/chromedriver 2')

    def test_reserve(self):
        user = "sbyluppala@unomaha.edu"
        pwd = "Team1"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://albuquerqueathleticfieldsystem.herokuapp.com")
        time.sleep(1)

        # login
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li[4]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://albuquerqueathleticfieldsystem.herokuapp.com")
        assert "Logged In"
        time.sleep(2)

        #click on profile
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li[3]/a").click()
        time.sleep(2)
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[2]/li[3]/ul/li[1]/a").click()
        time.sleep(5)
        #click edit profile
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[2]/a/span").click()
        time.sleep(2)
        # edit details
        elem = driver.find_element_by_id("id_first_name")
        elem.send_keys("Swetha")
        elem = driver.find_element_by_id("id_last_name")
        elem.send_keys("Byla")
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/form/button").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()


