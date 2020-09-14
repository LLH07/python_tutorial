#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os # built-in module in python


# 1. 有關 os module 的相關 methods:
#     1. 目錄相關: 
#         1. 列出 os 的路徑: 
#             <font color = 'blue'>dir(os)</font>
#         2. 目前所在路徑: 
#             <font color = 'blue'>os.get(cwd)</font>
#         3. 更改位置至: 
#             <font color = 'blue'>os.chdir(你要的路徑) [路徑以 string 表示]</font>
#         4. 目前位置的所有目錄: 
#             <font color = 'blue'>os.listdir()</font>
#         5. 創建新的目錄:
#             1. <font color = 'blue'>os.mdir(單一路徑)</font>
#             2. <font color = 'blue'>os.makedirs(深度路徑)</font>
#         6. 刪除目錄:
#             1. <font color = 'blue'>os.rmdir(單一路徑)</font>
#             2. <font color = 'blue'>os.removedirs(深度路徑)</font>
#         7. 更改目錄名稱:
#             <font color = 'blue'>os.rename(舊名稱, 新名稱) [名稱以 string 表示]</font>
#         8. 列出目前目錄的所有檔案:
#             <font color = 'blue'>os.walk(目前目錄) [名稱以 string 表示]</font>
#     2. 環境變數相關:
#         1. 查看環境變數:
#             <font color = 'blue'>os.environ</font>
#         2. 取得特定環境變數路徑:
#             <font color = 'blue'>os.environ.get(變數名稱)</font>
#     3. os.path useful methods:
#         1. 正確地新增檔案到目錄:
#             <font color = 'blue'>os.path.join(路徑 1, 路徑 2)</font>
#         2. 檔案名稱:
#             <font color = 'blue'>os.path.basename(路徑)</font>
#         3. 路徑名稱:
#             <font color = 'blue'>os.path.dirname(路徑)</font>
#         4. 檔案名稱與路徑名稱:
#             <font color = 'blue'>os.path.split(路徑)</font>
#         5. 查看路徑是否存在:
#             <font color = 'blue'>os.path.exists(路徑)</font>
#         6. 查看是否為路徑或檔案:
#             1. <font color = 'blue'>os.path.isdir(路徑)</font>
#             2. <font color = 'blue'>os.path.isfile(路徑)</font>
#         7. 分割檔案名稱: 
#             <font color = 'blue'>os.path.splitext(路徑)</font>
#         8. 查看更多 methods:
#             <font color = 'blue'>dir(os.path)</font>
#     

# In[2]:


print(dir(os)) # 列出電腦 os 的路徑


# In[3]:


print(os.getcwd()) # 列出目前所在路徑


# In[4]:


os.chdir(r'C:\Users\User\Desktop') # 更改目前位置: os.chdir(你要的路徑以 string 呈現)
print(os.getcwd())


# In[5]:


print(os.listdir()) # 列出目前路徑的所有目錄


# #### 在目前位置創目錄有兩種方法: mkdir() 與 makedirs()。
# #### 差別是 makedirs() 可以在用更深的目錄(目錄裡還有目錄)，mkdir() 則只能創造一層的目錄。
# #### <font color = 'red'>因此在創建目錄時，建議使用 os.makedirs()</font>

# In[6]:


os.mkdir('OS-demo_')


# In[7]:


os.makedirs('OS-demo2/second-dir_') # 用 os.mkdir() 會出現錯誤。


# #### 同樣道理: rmdirs() 與 removedirs()。
# #### <font color = 'red'>但在刪除目錄時，建議用 rmdirs()。因為比較不易出錯。</font>

# In[8]:


os.rename('OS-demo', 'os-demo')


# In[9]:


os.stat('os-demo') # 列出目標檔案的相關數據
# 注意到 st_mtime: 這是這個檔案最後被修改的時間


# In[10]:


print(os.stat('os-demo').st_mtime)
# st_mtime 是 stat 的一個 attribute。但這資料人類看不懂


# >實例所顯示的時間信息顯然不是我們所想像的那種年-月-日時:分:秒。  
# 這是因為系統記錄的時間是一個整數，這個整數表示自1970年1月1日00:00:00（國際標準時間）以來到時間記錄所要表達的時間所經過的秒數。  
# 如果要讓時間能看人肉眼看懂，還需要一些時間處理函數，例如時區轉換、時間的格式化輸出函數等。  
# 這種表示法稱為日曆時間。  

# In[11]:


# 方法是用 datetime 模組:
from datetime import datetime

mod_time = os.stat('os-demo').st_mtime
print(datetime.fromtimestamp(mod_time))
# 成功顯示時間


# ### 非常重要的技能: 列出所有檔案。
# #### 如果今天你知道檔案在桌面，但卻不知道在哪個資料夾，甚至你要的東西在資料夾內的資料夾...
# #### 這時就可以用 os.walk() 來迴圈 [他會回傳包含三個值的 tuple，存放<font color = 'red'> 目錄路徑，目錄名稱，目錄裡的檔案名稱</font>] 

# In[12]:


for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('Current Path', dirpath)
    print('Directories', dirname)
    print('Files', filename)
    print()


# #### 假設我今天要在 HOMEPATH 增加一個 test.txt 檔:

# In[13]:


print(os.environ)  # 查看電腦環境變數: 本機 -> 內容 -> 進階系統設定 -> 環境變數


# In[14]:


print(type(os.environ))


# In[16]:


print(os.environ.get('HOMEPATH')) # 查看名稱為 HOMEPATH 的環境變數的路徑。


# In[17]:


file_path = os.environ.get('HOMEPATH') + 'test.txt'
print(file_path)

# Naive 的想法是直接把你要新增的檔案名稱加在目標位置的後面，但會有個問題: "\" 會亂掉。
# 因此應該用 os.path.join()


# In[18]:


file_path2 = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path2)


# In[25]:


print(os.path.isfile(file_path2))


# In[26]:


print(dir(os.path))


# In[ ]:




