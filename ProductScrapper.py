#!/usr/bin/env python
# coding: utf-8

# In[100]:


import requests
from bs4 import BeautifulSoup
import csv 
import re
name=[]
price=[]
website=[]
urls=[]
with open("input.txt") as file:
    
    for url in file:
        URL = url;
        s=URL.split(".com")
        urls.append(url)
        if(s[0].find("flipkart")>0):
            
            r = requests.get(URL)
            if r.status_code!=200:
                print('sorry could not fetch data')
            else:    
                website.append('flipkart')
                soup = BeautifulSoup(r.content, 'html5lib')
                shoe_name = soup.find('span', class_ = 'B_NuCI')
                if shoe_name!=None:
                     name.append(shoe_name.text)
                     
                elif shoe_name==None:
                    name.append('error')
                shoe_price =soup.find('div',class_ = '_30jeq3 _16Jk6d')
                if shoe_price!=None:
                    price.append(float(re.sub(r'[^0-9.]', '', shoe_price.text)))
                elif shoe_price==None:
                    price.append('error')
                
        elif (s[0].find("meesho")>0):
            r = requests.get(URL)
            if r.status_code!=200:
                print('sorry could not fetch data')
            else:
                website.append('meesho')
                soup = BeautifulSoup(r.content, 'html5lib')
                shoe_name  = soup.find('span', class_ = 'Text__StyledText-sc-oo0kvp-0 elstub')
                if shoe_name!=None:
                    name.append(shoe_name.text)
                    
                elif shoe_name==None:
                    name.append('error')
                shoe_price =soup.find('h4',class_ = 'Text__StyledText-sc-oo0kvp-0 fyTUEs')
                if shoe_price!=None and shoe_price.text!="Shop Non-Stop on Meesho" :
                     price.append(float(re.sub(r'[^0-9.]', '', shoe_price.text)))
                   
                else:
                    price.append('error')
        else:
            print("wrong url ")
fields = ['Website', 'Product Name', 'Product Price', 'Url'] 
rows = zip(website, name,price,urls)
filename = "output.csv"
# print(website,price)
with open(filename, 'w+') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(fields) 
    for row in rows:
        csvwriter.writerow(row)
                
#     csvwriter.writerows([website])
#     csvwriter.writerow(name)
#     csvwriter.writerow(price)
#     csvwriter.writerow(urls)
    


# In[ ]:





# In[ ]:




