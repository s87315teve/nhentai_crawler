# coding: utf-8
import requests
from bs4 import BeautifulSoup
import threading
import queue

god_language=str(input("請輸入神的語言:"))
length=len(god_language)
#url="https://nhentai.net/g/287314/"
url="https://nhentai.net/g/"+god_language+"/"
temp=url.rfind('/')
dirname=url[temp-length:temp] #將神的語言變成資料夾名稱
now_index=-1
limit_index=0
path_queue=queue.Queue()
elem_list=None
exitFlag=0
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
            print(filename+" done")



try:
    r = requests.get(url) #將此頁面的HTML GET下來
    if r.status_code != 404:
        #print(r.text) 印出HTML
        soup = BeautifulSoup(r.text,'html.parser') 
        
        #print(elem)
        print("----------------------------------")
        elem_list=soup.find_all("div",class_="thumb-container")
        #print(type(elem_list))
        #for elem in elem_list:
            #print (elem['data-src'])
        #準備開始下載圖片
        import os
        path = dirname
        if not os.path.isdir(path):     
            os.mkdir(path)        #建立以神的語言為名的資料夾
        path=path+"\\"

            
        
        print("正在接受天之聲...")
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
        elem_list=soup.find_all("div",class_="thumb-container")
        for elem in elem_list:
            filepath=elem.img['data-src']
            filepath=filepath.replace("https://t","https://i")
            filepath=filepath.replace("t.",".")
            path_queue.put(filepath)

        threads = []
        threadID = 1
        n=1000
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

        
    else:
        print("這不是神的語言")
except:
    print("這不是神的語言，或是已經出bugㄌQQ")
    i=input("\n按任意鍵繼續...")


i=input("\n按任意鍵繼續...")
