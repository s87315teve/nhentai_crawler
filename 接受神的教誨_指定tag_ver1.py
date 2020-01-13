#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
import threading
import queue
import time

class myThread (threading.Thread):
    def __init__(self, threadID, data_queue):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.data_queue = data_queue
    def run(self):
        download(self.data_queue)


def download(data_queue):
    global now_index
    global limit_index
    global elem_list
    while not exitFlag:
        #queueLock.acquire()
        if not path_queue.empty():
            filepath=data_queue.get()
            pic = requests.get(filepath) #變數名稱為pic
            index=filepath.rfind('/')
            filename=filepath[index+1:]  #圖片名稱
            img = pic.content #變數名稱命名為img
            pic_out = open(path+filename,'wb') #
            pic_out.write(img) #將圖片存入img
            pic_out.close() #關閉檔案
            #print(filename+" done")


tag=str(input("請輸入你想要的tag:"))
no_tag=str(input("請輸入你不要的tag:"))
start_num=int(input("請輸入想從幾號開始:"))
end_num=int(input("請輸入想到幾號結束:"))
tag_list=[]
no_tag_list=[]
language_list=[]
artist_list=[]
#輸入tag 
tag=tag.upper()
tag_list=tag.split()
#print(tag_list)
#輸入不要的tag
no_tag=no_tag.upper()
no_tag_list=no_tag.split()
#print(no_tag_list)
#輸入語言
#language=language.upper()
#language_list=language.split()
#輸入作者
#artist=artist.upper()
#artist_list=artist.split()



print("尋找中...")
start_time_all=time.time()
for god_num in range(start_num,end_num+1):
    #print("----------------------------------\n")
    god_language=str(god_num)
    length=len(god_language)
    url="https://nhentai.net/g/"+god_language+"/"
    r = requests.get(url) #將此頁面的HTML GET下來
    soup = BeautifulSoup(r.text,'html.parser')
    elem=soup.find("meta",attrs={"name":"twitter:description"})
    try:
        ifdownload=True
        #print(elem)
        tags=elem['content'].upper()
        if len(tag_list)>0:
            for tag in tag_list:
                if tags.find(tag)==-1:
                    ifdownload=False
                    continue
        if len(no_tag_list)>0:
            for no_tag in no_tag_list:
                if tags.find(no_tag)!=-1:
                    ifdownload=False
                    continue
        if ifdownload==False:
            continue
    except:
        continue
    temp=url.rfind('/')
    dirname=url[temp-length:temp] #將神的語言變成資料夾名稱
    now_index=-1
    limit_index=0
    path_queue=queue.Queue()
    elem_list=None
    exitFlag=0

    try:
        start_time=time.time()
        r = requests.get(url) #將此頁面的HTML GET下來
        if r.status_code != 404:
            #print(r.text) 印出HTML
            soup = BeautifulSoup(r.text,'html.parser') 

            #print(elem)
            
            elem_list=soup.find_all("div",class_="thumb-container")
            #print(type(elem_list))
            #for elem in elem_list:
                #print (elem['data-src'])
            #準備開始下載圖片
            import os
            if len(tag_list)>0 or len(no_tag_list)>0 or len(language_list)>0 or len(artist_list)>0:
                path=""
                if len(tag_list)>0:
                    path = path+"yes"
                    for tag in tag_list:
                        path = path+ "_"+tag                   
                if len(no_tag_list)>0:
                    path = path+"_"
                    path = path+"no"
                    for no_tag in no_tag_list:
                        path = path+"_"+no_tag
                    path = path+"_"
                if len(language_list)>0:
                    path = path+"language"
                    for language in language_list:
                        path = path+"_"+language
                    path = path+"_"
                if len(artist_list)>0:
                    path = path+"artist"
                    for artist in artist_list:
                        path =path+ "_"+artist
            else:
                path="不分類"
            if not os.path.isdir(path):     
                os.mkdir(path)        #建立以tag為名的資料夾
            path=path+"\\"+dirname
            if not os.path.isdir(path):     
                os.mkdir(path)        #建立以神的語言為名的資料夾
            path=path+"\\"



            
            print("現在正在下載 {}".format(god_num))
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
            elem_list=soup.find_all("div",class_="thumb-container")
            for elem in elem_list:
                filepath=elem.img['data-src']
                filepath=filepath.replace("https://t","https://i")
                filepath=filepath.replace("t.",".")
                path_queue.put(filepath)



            #threadList = ["Thread-1", "Thread-2", "Thread-3","Thread-4","Thread-5","Thread-6","Thread-7","Thread-8","Thread-9","Thread-10","Thread-11","Thread-12"]
            #queueLock = threading.Lock()
            print("正在接受天之聲...")
            threads = []
            threadID = 1
            n=300
            # 建立新的thread
            for tName in range(n):
                thread = myThread(threadID,path_queue)
                thread.start()
                threads.append(thread)
                threadID += 1

            # 等待queue清空
            while not path_queue.empty():
                pass

            
            exitFlag = 1

            # 等待所有thread完成

            for t in threads:
                t.join()
            print("神的語言"+dirname+"已接收完成")
            end_time=time.time()
            used_time=end_time-start_time
            print("總共花費 {} 秒".format(used_time))


        else:
            print("這不是神的語言")


    except KeyboardInterrupt:
        break
    except:
        print("這不是神的語言，或是已經出bugㄌQQ")
        break

end_time_all=time.time()
used_time=end_time_all-start_time_all
print("\n\n合計花費 {} 秒".format(used_time))
i=input("\n按任意鍵繼續...")




