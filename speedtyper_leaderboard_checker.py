from win10toast import ToastNotifier
from bs4 import BeautifulSoup
from selenium import webdriver
import time

toaster = ToastNotifier()

url = "https://www.speedtyper.dev/"
PATH = "C:\Program Files (x86)\chromedriver.exe"
webdriver = webdriver.Chrome(PATH)
webdriver.get(url)

time.sleep(2)
doc = BeautifulSoup(webdriver.page_source, "html.parser")

crown = webdriver.find_element_by_xpath(
    '//*[@id="__next"]/div/div[1]/div/header/div/div/div[1]/button[2]'
)

time.sleep(5)
crown.click()
time.sleep(5)

doc = BeautifulSoup(webdriver.page_source, "html.parser")

users = doc.find_all(
    class_="flex items-center justify-start gap-8 p-1 px-2 my-1 first:font-bold even:bg-gray-200 rounded"
)[1:]

print("\nLeadership Viewer\n")
for data in users:
    user = data.find_all(class_="ml-2")[1]
    speed = data.find(class_="w-[120px]")
    accuracy = data.find(class_="hidden sm:block w-[125px]")
    print("user:", user.string)
    print("speed:", speed.string)
    print("accuracy:", accuracy.string)
    print("------------------------------")

webdriver.quit()

toaster.show_toast("View Leaderboard", "Done!")
