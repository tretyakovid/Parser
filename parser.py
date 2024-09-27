from requests import get
import random
import time
from bs4 import BeautifulSoup


def parser(url):

    ordersList = []
    resultlist = []

    count = 1

    while count <= 2:

        currentUrl = url + str(count)
        print(currentUrl)
    
        responce = get(currentUrl)
        html_soup = BeautifulSoup(responce.text, "html.parser")
        orders_data = html_soup.find_all("li", class_="content-list__item")

        if orders_data != []:
            ordersList.extend(orders_data)
            value = random.random()
            scaled_value = 1 + (value * (10 - 5))
            time.sleep(scaled_value)
            count += 1
        else:
            print("empty")
            break

    count = 0

    while count != len(ordersList):
        info = ordersList[int(count)]
        time_ = info.find("span", {"class":"params__published-at"}).text
        if time_.split()[-2] != "дня" or time_.split()[-2] != "дней" or time_.split()[-2] != "день":
            title = info.find("div", {"class":"task__title"}).text
            price = info.find("div", {"class":"task__price"}).text
            line = title, ' ---> ', price, ' ---> ', time_
            result = "".join(line)
            resultlist.append(result)

        count += 1
    return resultlist


url = "https://freelance.habr.com/tasks?page="


result = parser(url)
count = 0
while count != len(result):
    print(result[count])
    count += 1
