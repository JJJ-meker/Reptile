import requests
from bs4 import BeautifulSoup


class downloader(object):
    def __init__(self):
        self.html='https://blog.snowstar.org/'
        self.names=[]
        self.urls=[] 
        
    def get_download_url(self):
        response=requests.get(url=self.html)
        data=response.text
        a_bf=BeautifulSoup(data,'html.parser')
        a=a_bf.find_all('a',class_='button')
        target=BeautifulSoup(str(a))
        text_url=target.find_all('a')
        for item in text_url:
            src=item['href']
        
        
    def get_contents(self,html):
            res=requests.get(url=html)
            date=res.text
            bf=BeautifulSoup(date,'html.parser')
            texts=bf.find_all('div',class_='entry-content')
            return texts
    
    def writer(self,path,text):
            write_flag=True
            with open(path,'a',encoding='utf-8')as f:
                f.writelines(text)
                f.write('\n\n')

if __name__=="__main__":
    dl=downloader()
    dl.get_download_url()
    
'''
Created on 2019-11-10

@author: jjj
'''
