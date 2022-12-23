import requests
from bs4 import BeautifulSoup

# Send request to the server
resp = requests.get("https://www.umei.cc/meinvtupian/meinvxiezhen/") # get the source code from the server
resp.encoding = 'utf-8'
# print(resp.text)

# beautifulsoup
main_page = BeautifulSoup(resp.text, "html.parser")
# find() / find_all()
type_list = main_page.find("div", attrs={"class": "item_list infinite_scroll"}).find_all("img", attrs={"class": "lazy"})
# print(type_list)

n = 1

for t in type_list:
    # print(t.get("data-original"))
    orig = t.get("data-original")
    # print(orig)

    # create file
    f = open("tu_%s.jpg" % n, mode="wb")
    f.write(requests.get(orig).content)

    print("picture + 1")

    n += 1

