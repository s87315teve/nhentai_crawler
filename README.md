# nhentai_crawler使用說明

**本程式僅用於學術用途
出事不要找我(￣▽￣)**


如題，這個是可以自動到n網下載本子的程式
目前有四種版本，可以依據自己的需求選擇版本使用，在各資料夾裡面都有程式的使用說明

在不同作業系統下的注意事項：

**Windows**
* 有附上.exe檔，如果對python不熟悉的人可以直接點開.exe檔執行程式
* 如果想要執行.py檔的人，請確認電腦執行的環境是python3，因為我thread的寫法是用python3的

**MacOS / Linux**
* 請將檔案內所有的 "**\\\\**" 改成 "**/**" ，因為windows是用"\\"來劃分檔案路徑，MacOS及Linux系統則是用"/"，而為什麼要將兩個反斜線取代成一個正常的斜線則是因為反斜線是特殊字元，要特別注意
* 請確認電腦執行的環境是python3，因為我thread的寫法是用python3的


如果要自己執行py檔的人請記得安裝python的requests和beautifulsoup4
指令如下(以pip為例)
<code>pip install requests </code> 
<code>pip install beautifulsoup4 </code> 
請安裝完這兩個library後再去用python3執行

---
補充:
如果有發現bug或是建議改善的地方可以跟我說
然後我知道code可讀性不是很好，還請各位大神見諒(跪
