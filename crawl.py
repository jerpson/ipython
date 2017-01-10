# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests
import time
from pandas import Series
from pandas import DataFrame
import csv


url = 'http://www.baiji.com.cn/goods-'

#伪装浏览器请求信息
headers = {
    'Cookie':'BAIDUID=506B59EB161C45F92B709E65F6944FA1:FG=1; HMACCOUNT=57980B0706493174; BIDUPSID=BC71D5C04CE3BA938F019010BF37EB25; PSTM=1433318973; MCITY=-%3A; BDUSS=095NFhpRH56RUhVc1hRcmZhZnVvdjNKbVh0Yy1EdXpKcmk5enBnVnQ0VlJOdTlYQVFBQUFBJCQAAAAAAAAAAAEAAADbTDgpxtXMq8DHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFGpx1dRqcdXN; H_PS_PSSID=1451_19033_18281_17946_20239_20857_20732_20836; HMVT=6fee620478edc136f5fe1f01d6a327a4|1473130480|',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0'
}


#获取某一个页面的数据
def get_page(url):
    try:
        web_data = requests.get(url,headers=headers)
        soup = BeautifulSoup(web_data.text,'html.parser')
        name = soup.h1.get_text()
        item = soup.findAll('div',{'class':'item selected'})
        marpri = soup.findAll(id="ECS_MARKETPRICE")
        membpri = soup.findAll('div',id="ECS_SHOPPRICE")
    except AttributeError as e:
        return None
    
    
    data = {'名称':name,
            '规格':item[0].get_text(),
            '市场价':marpri[0].get_text(),
            '会员价':membpri[0].get_text()
            }
            
    
    
def get_more_pages(start,end):
    count = 0
    data = DataFrame(columns=['名称','规格','市场价','会员价'])
    for num in range(start,end):
        get_page(url+str(num)+'.html')
        count = count+1
        data = data.append(Series([name, item,marpri,membpri], index=['名称','规格','市场价','会员价']), ignore_index=True)
        print (count)
        time.sleep(3)
        
    
get_more_pages(7138,7140)



"""
   
    
 
csvFile = open('C:\\Users\\Administrator\\Desktop\\goods.csv','wt',newline='',encoding='utf-8')
writer = csv.writer(csvFile)

csvgoods = []

csvgoods.append(name)

    data = [name,item,marpri,membpri]
    print(data)
    
 
    data = DataFrame(columns=['名称','规格','市场价','会员价'],values=data1)
    data1 = data.append(Series([name, item,marpri,membpri], index=['名称','规格','市场价','会员价']), ignore_index=True)
    print(data1)
    
    
data = DataFrame(columns=['名称','规格','市场价','会员价'])
    
    for num in range(7138,7140):
        data = data.append(Series([name, item,marpri,membpri], index=['名称','规格','市场价','会员价']), ignore_index=True)
        print(data)    
    
    """
    



