# coding: utf-8
import requests
from bs4 import BeautifulSoup

god_language=str(input("請輸入神的語言:"))
length=len(god_language)
#url="https://nhentai.net/g/287314/"
url="https://nhentai.net/g/"+god_language+"/"
temp=url.rfind('/')
dirname=url[temp-length:temp] #將神的語言變成資料夾名稱



try:
    r = requests.get(url) #將此頁面的HTML GET下來
    #print(r.text) 印出HTML
    soup = BeautifulSoup(r.text,'html.parser') 
    
    #print(elem)
    print("----------------------------------")
    elem_list=soup.find_all("img",class_="lazyload")
    #print(type(elem_list))
    #for elem in elem_list:
        #print (elem['data-src'])
    #準備開始下載圖片
    import os
    path = dirname
    if not os.path.isdir(path):     
        os.mkdir(path)        #建立以神的語言為名的資料夾
    path=path+"\\"

	
    print("神的敕語：")
    if soup.h1!=None:
        temp=str(soup.h1)
        temp=temp.replace("<h1>","")
        temp=temp.replace("</h1>","")
    print(temp)
    if soup.h2!=None:
        temp=str(soup.h2)
        temp=temp.replace("<h2>","")
        temp=temp.replace("</h2>","")
        print(temp)
    print("\n一共有 %d 個章節"%len(elem_list))
    print("正在接受天之聲...")
    for elem in elem_list:
        temp=elem['data-src'].rfind('/')
        filename=elem['data-src'][temp+1:]  #圖片名稱
        pic = requests.get(elem['data-src']) #變數名稱為pic
        img = pic.content #變數名稱命名為img
        pic_out = open(path+filename,'wb') #
        pic_out.write(img) #將圖片存入img.png
        pic_out.close() #關閉檔案
        print(filename+" done")
    print("神的語言"+dirname+"已接收完成")
except:
    print("這不是神的語言")

i=input("\n按任意鍵繼續...")
