from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
poorname=[] #List to store the name of the product
pprices=[]
for i in range(0,15):
 url="https://www.poorvika.com/s?categories_slug=categories_slug%3A%3D%5B%60smartphones%60%5D&stock_status=stock_status%3A%3D%5B%60In+Stock%60%5D&page="+str(i)
 response = requests.get(url)
 htmlcontent = response.content
 soup = BeautifulSoup(htmlcontent,"html.parser")
 print(soup.prettify)
 for data in soup.findAll('div',class_='product-cardlist_card_description_eduH5'):
    print(data)
    names=data.find('b')
    price=data.find('span', attrs={'class':'whitespace-nowrap'})
    poorname.append(names.text) # Add product name to list
    pprices.append(price.text[2:])
    respo= dict(zip(poorname,pprices))
#print(respo)
#print(len(products))
#print(len(prices))
pdf=pd.DataFrame({"Productname":poorname,"Product Prices":pprices})
print(pdf)
pdf.to_csv("amazon.csv")
res = dict(zip(poorname,pprices))
print(res)
#inp1=input()
#price1=res.get(inp1)
########################### FLIPKART ###########################
flipname=[] #List to store the name of the product
fprices=[]
for i in range(0,15):
 url="https://www.flipkart.com/mobiles/pr?sid=tyy,4io&otracker=categorree&page="+str(i)
 response = requests.get(url)
 htmlcontent = response.content
 soup = BeautifulSoup(htmlcontent,"html.parser")
 print(soup.prettify)
 for data in soup.findAll('div',class_='_3pLy-c row'):
    print(data)
    names=data.find('div',class_='_4rR01T').get_text()
    price=data.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    flipname.append(names) # Add product name to list
    fprices.append(price.text[1:])
    respo= dict(zip(flipname,fprices))
#print(respo)
#print(len(products))
#print(len(prices))
fdf=pd.DataFrame({"Productname":flipname,"Product Prices":fprices})
print(fdf)
fdf.to_csv("Flipkart.csv")
res = dict(zip(flipname,fprices))
print(res)
#inp1=input()
#price1=res.get(inp1)
##################################### AMAZON #############################################
products=[] #List to store the name of the product
prices=[]
for i in range(0,30):
 url="https://www.amazon.in/s?i=electronics&rh=n%3A1389432031&fs=true&page=3&qid=1708577474&ref=sr_pg_"+str(i)
 response = requests.get(url)
 htmlcontent = response.content
 soup = BeautifulSoup(htmlcontent,"html.parser")
 for data in soup.findAll('div',class_='a-section a-spacing-small puis-padding-left-small puis-padding-right-small'):
    names=data.find('span',class_='a-size-base-plus a-color-base a-text-normal')
    price=data.find('span', attrs={'class':'a-offscreen'})
    products.append(names.text) # Add product name to list
    prices.append(price.text[1:])
    respo= dict(zip(products,prices))
#print(respo)
#print(len(products))
#print(len(prices))
df=pd.DataFrame({"Productname":products,"Product Prices":prices})
print(df)
df.to_csv("Amazon.csv")
res = dict(zip(products,prices))
print(res)
import numpy as np
import pandas as pd
poor=99999999
flip=99999999
amazon=999999999
n=input("Enter product name")
for i in range(len(pdf['Productname'])):
    if(n in pdf['Productname'].iloc[i]):
        poor=int(pdf['Product Prices'].iloc[i].replace(',',''))
for i in range(len(fdf['Productname'])):
    if(n in fdf['Productname'].iloc[i]):
        flip=int(fdf['Product Prices'].iloc[i].replace(',',''))
for i in range(len(df['Productname'])):
    if(n in df['Productname'].iloc[i]):
        amazon=int(pdf['Product Prices'].iloc[i].replace(',',''))
print(poor,flip,amazon)
print(min(poor,flip,amazon))
