import json
import requests
from bs4 import BeautifulSoup

f = open("/home/zoe/Documents/Exam1_1.json","r")
data={}
data = json.load(f)

urllist1 = []
urllist2 = []
for i in range(len(data)):
    url1 = data[i]['sum_title_url']
    urllist1.append(url1)
    data_s = data[i]['spotlist']
    for j in range(len(data_s)):
        url2 = data_s[j]['url']
        urllist2.append(url2)

for k1 in range(len(urllist1)):
    response = requests.get(urllist1[k1])
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("div",{"class":"indent"}).findAll("p")
    for obj in result:
        t = soup.find("h1").getText()
        with open("sum_"+str(t[0:4])+".text","w") as fn:
            for obj in result:
                print(obj.text,file=fn)

for k2 in range(len(urllist2)):
    response = requests.get(urllist2[k2])
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("div",{"class":"indent"}).findAll("p")
    for obj in result:
        t = soup.find("h1").getText()
        with open("spot_"+str(t[0:4])+".text","w") as fn:
            for obj in result:
                print(obj.text,file=fn)

f.close()

print("Hello World!")
