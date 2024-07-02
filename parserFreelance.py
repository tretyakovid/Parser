from requests import get
import random
import time
from bs4 import BeautifulSoup


def freelanceParser(url):

    topList = []
    list = []

    position = True

    while position == True:
    
        responce = get(url)
        html_soup = BeautifulSoup(responce.text, "html.parser")
        topList_data = html_soup.find_all("li", class_="content-list__item")

        if topList_data != []:

            topList.extend(topList_data)
            value = random.random()
            scaled_value = 1 + (value * (10 - 5))
            time.sleep(scaled_value)
        else:
            print("empty")
            break
    
        position = False

    count = 0

    while count <= 11:
        info = topList[int(count)]
        title = info.find("div", {"class":"task__title"}).text
        price = info.find("div", {"class":"task__price"}).text
        time_ = info.find("span", {"class":"params__published-at"}).text
        # responses = info.find("span", {"class":"params__responses"}).text
        # if (not responses):
        #     responses = print("ОТКЛИКОВ НЕТ")
        line = title, ' ---> ', price, ' ---> ', time_
        result = "".join(line)

        list.append(result)

        count += 1
    return list

url = "https://freelance.habr.com/tasks"


topList = freelanceParser(url)
count = 0
while topList != []:
    print(topList[count])
    count += 1
    if count == 10:
        print("Первые " + str(count) + " заказов выведены") 
        input()
        break