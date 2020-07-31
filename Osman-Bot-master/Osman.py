from instaUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        
    def islemler(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(2)
        print("Instagram web page opened...")

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        print("Signed in...")

        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        print("Profile page opened...")
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        followerCount = len(dialog.find_elements_by_css_selector("li"))
        print("Started to counting followers..........")
        print(f"starting count: {followerCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"current count: {newCount}")
                time.sleep(1)
            else:
                break
        
        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        i = 0
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")            
            followerList.append(link)            
            i += 1
            if i == max:
                break
        print("---end of the counting followers---")
        print("All followers have been founded --> followers.txt")

        with open("followers.txt", "w",encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")


        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(2)

        dialog = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
        followingCount = len(dialog.find_elements_by_css_selector("li"))

        print("Started to counting followings..........")
        print(f"starting count: {followingCount}")

        action = webdriver.ActionChains(self.browser)

        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()

            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followingCount != newCount:
                followingCount = newCount
                print(f"current count: {newCount}")
                time.sleep(1)
            else:
                break
        
        followings = dialog.find_elements_by_css_selector("li")

        followingList = []
        i = 0
        for user in followings:
            link = user.find_element_by_css_selector("a").get_attribute("href")            
            followingList.append(link)            
            i += 1
            if i == max:
                break
        print("---end of the counting followings---")
        print("All folowings have been founded --> followings.txt")
        self.browser.close()
        self.browser.quit()
        print("browser is closed..")

        print("*****************************************")
        print("---Operation that founding users who not following you back is started---")
        print("*****************************************")
        with open("followings.txt", "w",encoding="UTF-8") as file:
            for item in followingList:
                file.write(item + "\n")

        followerList = []
        with open("followers.txt","r",encoding="UTF-8") as file1:
            for item in file1:
                followerList.append(item)

        followingList = []
        with open("followings.txt","r",encoding="UTF-8") as file2:
            for item in file2:
                followingList.append(item)

        idiotList = []
        with open("notFollowingBacks.txt","w",encoding="UTF-8") as file3:
            for item in followingList:
                if item not in followerList:
                    file3.write(item)
                    idiotList.append(item)
        print("---Operation is successful!!!---")
        print("All users that not following you back have been founded --> notFollowingBacks.txt")
        print("*coded by onurbyrl*")


insta = Instagram(username,password)
insta.islemler()