from lib2to3.pgen2 import driver
from turtle import title
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import HtmlTestRunner



class taskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("driver/chromedriver.exe") #Enter path of chrome driver
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    #check the title of the page using title command
    def test_01_titleDisplay1(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html")
        get_title = self.driver.title
        print(get_title)
    #check the text of the title using xpath      

    def test_02_titleDisplay2(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html")
        pageTitle = self.driver.find_element(By.XPATH, "/html/head/title")
        if (pageTitle.is_displayed()):
            print("title exists and the title of the page is:" + pageTitle)
        else:    
            print("title of the page not displaying using find_element case")
        time.sleep(2)

    #Check the visibility of grade
    def test_03_gradeVisibility(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") 
        grade_score = self.driver.find_element(By.CSS_SELECTOR, "div[class='main-box no-margin d-none d-lg-block ng-star-inserted'] span[class='score-slash']")   
        if (grade_score.is_displayed):
            print("grade is visible")
        else:
            print("grade is not visible")   
        time.sleep(2)

    #Check the grade above zero
    def test_04_ratingsAboveZero(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") 
        grade_score = self.driver.find_element(By.CSS_SELECTOR, "div[class='main-box no-margin d-none d-lg-block ng-star-inserted'] span[class='score-slash']")   
        ratingsStr = self.driver.find_element(By.CLASS_NAME, "score-info").text
        ratings = self.driver.find_element(By.CLASS_NAME, "score-shop").text
        if (float(ratings) > 0):
            print(ratingsStr)
        else:
            print("ratings is less than zero")   
        time.sleep(2)

    # Mouse Hover over the Info
    def test_05_hoverInfo(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html")
        action = ActionChains(self.driver)
        hover_info = self.driver.find_element(By.XPATH, "//span[@class='tsproi tsproi-icon-feedback-info-circle-outline ng-tns-c63-13']")
        action.move_to_element(hover_info).perform()
        print("Mouse hover over the Info successfully")
        time.sleep(2)

    #Pop up appearancs case for info icon
    def test_06_popUpAppearance(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html")
        action = ActionChains(self.driver)
        hover_info = self.driver.find_element(By.XPATH, "//span[@class='tsproi tsproi-icon-feedback-info-circle-outline ng-tns-c63-13']")
        action.move_to_element(hover_info).perform()
        information = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/review-area/review-topflop/div[1]/div[1]/div/review/review-header/loading-line[2]/div/span[1]")
        print(information.text)
        time.sleep(2)

    #filter testcase for 1 stern
    def test_07_filter1Stern(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") 
        one_stern_review = self.driver.find_element(By.XPATH, "//div[@class='main-box no-margin d-none d-lg-block ng-star-inserted']//div[@class='bar-title text-link'][normalize-space()='1 Stern']").click()
        print(self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/review-area/review-filters-active/chip/div[1]/div").text)
        time.sleep(2)

    #filter case to check only 1 Stern is selected
    def test_08_filterStern(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") 
        one_stern_review = self.driver.find_element(By.XPATH, "//div[@class='main-box no-margin d-none d-lg-block ng-star-inserted']//div[@class='bar-title text-link'][normalize-space()='1 Stern']").click()
        time.sleep(2)
        filterOption = self.driver.find_element(By.XPATH, "//span[@class='tsproi tsproi-icon-arrow-chevron-down rotate-on-open ng-tns-c53-6']").click()
        
        #If checkbox is enabled for below lines of code then output will be true otherwise output will be false

        CheckBox1Stern = self.driver.find_element(By.ID, "stars-value-1").is_selected() # for 1 stern
        print(CheckBox1Stern)
        CheckBox2Sterne = self.driver.find_element(By.ID, "stars-value-2").is_selected() # for 2 sterne
        print(CheckBox2Sterne)
        CheckBox3Sterne = self.driver.find_element(By.ID, "stars-value-3").is_selected() # for 3 sterne
        print(CheckBox3Sterne)
        CheckBox4Sterne = self.driver.find_element(By.ID, "stars-value-4").is_selected() # for 4 sterne
        print(CheckBox4Sterne)
        CheckBox5Sterne = self.driver.find_element(By.ID, "stars-value-5").is_selected() # for 5 sterne
        print(CheckBox5Sterne)

        time.sleep(2)

    #to get the sum of the stere equals to 100    
    def test_09_totalSum(self):
        self.driver.get("https://www.trustedshops.de/bewertung/info_X77B11C1B8A5ABA16DDEC0C30E7996C21.html") 
        fiveSterneValue = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/div/ratings-summary/div[2]/div[2]/div[3]/div[1]/div[3]/span[1]").text
        fourSterneValue = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/div/ratings-summary/div[2]/div[2]/div[3]/div[2]/div[3]/span[1]").text
        threeSterneValue = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/div/ratings-summary/div[2]/div[2]/div[3]/div[3]/div[3]/span[1]").text
        twoSterneValue = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/div/ratings-summary/div[2]/div[2]/div[3]/div[4]/div[3]/span[1]").text
        oneSternValue = self.driver.find_element(By.XPATH, "/html/body/presentation-frame/shop-profile/div/div/div[1]/div/ratings-summary/div[2]/div[2]/div[3]/div[5]/div[3]/span[1]").text
        fiveSterneNumValue = int(fiveSterneValue)
        fourSterneNumValue = int(fourSterneValue)
        threeSterneNumValue = int(threeSterneValue)
        twoSterneNumValue = int(twoSterneValue)
        oneSternNumValue = int(oneSternValue)
        totalSum = fiveSterneNumValue + fourSterneNumValue + threeSterneNumValue + twoSterneNumValue + oneSternNumValue
        if (totalSum > 100):
            print("This is an issue and total number of sum is: " + str(totalSum))
            
        else:
            print(totalSum)    
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")    

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output = "./Tasks/Reports"))   #Enter path of the folder to keep generated reports

