
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

        # click on reservation
        elem = driver.find_element_by_xpath("//*[@id=\"myNavbar\"]/ul[1]/li[2]/a").click()
        time.sleep(2)
        #click on one park to filter
        elem = driver.find_element_by_xpath("//*[@id=\"sidebar\"]/ul/li[4]/a").click()
        time.sleep(2)
        #select a property
        elem = driver.find_element_by_xpath("//*[@id=\"main\"]/div[1]/a[2]").click()
        time.sleep(2)
        # click on schedule
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/a").click()
        time.sleep(2)
        # click new reservation
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/a[3]").click()
        # select details in the form
        elem = driver.find_element_by_id("id_prop_name")
        elem.send_keys("Chelwood_Basketballcourt")
        elem = driver.find_element_by_id("id_Name_of_the_organization")
        elem.send_keys("Test Org Name")
        elem = driver.find_element_by_id("id_Team_Name")
        elem.send_keys("Test team Name")
        elem = driver.find_element_by_id("id_Size_of_the_team")
        elem.send_keys("5")
        elem = driver.find_element_by_id("day")
        elem.send_keys("04/27/2019")
        elem = driver.find_element_by_id("id_timeslot")
        elem.send_keys("M1- 6.00 A.M to 8.00 A.M")
        time.sleep(5)
        #click submit
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[1]/form/button").click()
        assert "Your Reservation has been confirmed!"
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
        unittest.main()


