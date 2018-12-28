from selenium import webdriver
import time


def Gmail(driver):
    #username = input("Enter Email or Number:- ")
    #password = input("Enter Password:- ")

    driver.get("https://www.gmail.com")
    driver.find_element_by_name('identifier').send_keys(username)
    driver.find_element_by_css_selector(
        '#identifierNext > content > span').click()
    driver.implicitly_wait(8)

    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_css_selector(
        '#passwordNext > content > span').click()


def Facebook(driver):
    #username = input("Enter Email or Number:- ")
    #password = input("Enter Password:- ")
    driver.get("https://www.facebook.com/")
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('loginbutton').click()


def Github(driver):
    #username = input("Enter Email or Number:- ")
    #password = input("Enter Password:- ")
    driver.get("https://github.com/login")
    driver.find_element_by_id('login_field').send_keys(
        "akhilsunny04@gmail.com")
    driver.find_element_by_id('password').send_keys("Togariakhil143")
    driver.find_element_by_name('commit').click()


if __name__ == "__main__":
    driver = webdriver.Chrome('/home/androidts/python/chromedriver')
    n = 1
    while n != 0:
        print("choose the below choise")
        print("1.Gmail")
        print("2.Facebook")
        print("3.Github")
        print("0.Exit")
        option = int(input("Enter the choose"))
        if option == 1:
            Gmail(driver)
        elif option == 2:
            Facebook(driver)
        elif option == 3:
            Github(driver)
        elif option == 0:
            try:
                driver.close()
            except:
                print("brower alrady closed")
            n = 0
        else:
            print("Enter valid option")
