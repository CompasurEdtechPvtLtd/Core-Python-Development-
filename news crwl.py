import urllib.request as url
import bs4
path = "https://www.foxnews.com"
print(path)
response=url.urlopen(path)
data = bs4.BeautifulSoup(response,'lxml')

politicsli= data.find('li',class_="menu-politics")
polticsa = politicsli.find('a')['href']
polticsa

buisnessli= data.find('li',class_="menu-business")
buisnessa=buisnessli.find('a')['href']
buisnessa

entli= data.find('li',class_="menu-entertainment")
enta=entli.find('a')['href']
print(enta)

sportli= data.find('li',class_="menu-sports")
sporta=sportli.find('a')['href']
sporta

print("""
pass 1 for sport
pass 2 for entertainment
pass 3 for politics
pass 4 for buisness
""")
while True:      
    choice = int(input("enter your coice"))
    if choice==1:
        path1= "https:"+sporta
        print(path1)
        response=url.urlopen(path1)
        data = bs4.BeautifulSoup(response,'lxml')
        
        xya=data.find("div",class_="content article-list")
        
        h4List=xya.findAll("h4",class_="title")
        for i in range(len(h4List)):
            print(i+1,"  --->",h4List[i].text)
            
        print("*******************************************")
        
            
    if choice==2:
        path2= "https:"+enta
        response=url.urlopen(path2)
        data = bs4.BeautifulSoup(response,'lxml')
        
        xya=data.find("div",class_="content article-list")
        
        h4List=xya.findAll("h4",class_="title")
        for i in range(len(h4List)):
            print(i+1,"  --->",h4List[i].text)
            

        print("*******************************************")
        
    if choice==3:
        path2= "https:"+polticsa
        response=url.urlopen(path2)
        data = bs4.BeautifulSoup(response,'lxml')
        
        xya=data.find("div",class_="content article-list")
        
        h4List=xya.findAll("h4",class_="title")
        for i in range(len(h4List)):
            print(i+1,"  --->",h4List[i].text)
            


        print("*******************************************")
        
    if choice==4:
        path2= "https:"+buisnessa
        print(path2)
        response=url.urlopen(path2)
        data = bs4.BeautifulSoup(response,'lxml')
        xya=data.findAll("div",class_="content article-list")
        h3List=xya[2].findAll("h3",class_="title")
        for i in range(len(h3List)):
            x = h3List[i].text.replace("\n","")
            print(i+1,"  --->",x)
        
