import requests
import bs4
url="https://www.amazon.in/"
res=requests.get(url)
print(res)
htmlData=res.content
print(htmlData)
parseData=bs4.BeautifulSoup(htmlData)
print(parseData.prettify())
print(parseData.title.string)
#H2Tags=parseData.find("h2")
#print(H2Tags)
H2Tags=parseData.find_all("h2")
for h2 in H2Tags:
    print(h2)
    print(h2.string)