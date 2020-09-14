```python
import os # built-in module in python
```

1. 有關 os module 的相關 methods:
    1. 目錄相關: 
        1. 列出 os 的路徑: 
            <font color = 'blue'>dir(os)</font>
        2. 目前所在路徑: 
            <font color = 'blue'>os.get(cwd)</font>
        3. 更改位置至: 
            <font color = 'blue'>os.chdir(你要的路徑) [路徑以 string 表示]</font>
        4. 目前位置的所有目錄: 
            <font color = 'blue'>os.listdir()</font>
        5. 創建新的目錄:
            1. <font color = 'blue'>os.mdir(單一路徑)</font>
            2. <font color = 'blue'>os.makedirs(深度路徑)</font>
        6. 刪除目錄:
            1. <font color = 'blue'>os.rmdir(單一路徑)</font>
            2. <font color = 'blue'>os.removedirs(深度路徑)</font>
        7. 更改目錄名稱:
            <font color = 'blue'>os.rename(舊名稱, 新名稱) [名稱以 string 表示]</font>
        8. 列出目前目錄的所有檔案:
            <font color = 'blue'>os.walk(目前目錄) [名稱以 string 表示]</font>
    2. 環境變數相關:
        1. 查看環境變數:
            <font color = 'blue'>os.environ</font>
        2. 取得特定環境變數路徑:
            <font color = 'blue'>os.environ.get(變數名稱)</font>
    3. os.path useful methods:
        1. 正確地新增檔案到目錄:
            <font color = 'blue'>os.path.join(路徑 1, 路徑 2)</font>
        2. 檔案名稱:
            <font color = 'blue'>os.path.basename(路徑)</font>
        3. 路徑名稱:
            <font color = 'blue'>os.path.dirname(路徑)</font>
        4. 檔案名稱與路徑名稱:
            <font color = 'blue'>os.path.split(路徑)</font>
        5. 查看路徑是否存在:
            <font color = 'blue'>os.path.exists(路徑)</font>
        6. 查看是否為路徑或檔案:
            1. <font color = 'blue'>os.path.isdir(路徑)</font>
            2. <font color = 'blue'>os.path.isfile(路徑)</font>
        7. 分割檔案名稱: 
            <font color = 'blue'>os.path.splitext(路徑)</font>
        8. 查看更多 methods:
            <font color = 'blue'>dir(os.path)</font>
    


```python
print(dir(os)) # 列出電腦 os 的路徑
```

    ['DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', 'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', 'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_get_exports_list', '_putenv', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', 'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', 'utime', 'waitpid', 'walk', 'write']
    


```python
print(os.getcwd()) # 列出目前所在路徑
```

    C:\Users\User\python_tutorial
    


```python
os.chdir(r'C:\Users\User\Desktop') # 更改目前位置: os.chdir(你要的路徑以 string 呈現)
print(os.getcwd())
```

    C:\Users\User\Desktop
    


```python
print(os.listdir()) # 列出目前路徑的所有目錄
```

    ['Blair - Chrome.lnk', 'Cisco Webex Meetings.lnk', 'desktop.ini', 'Game Center.lnk', 'Google Office', 'LINE.lnk', 'MinGW Installer.lnk', 'OneSafe PC Cleaner.lnk', 'os-demo', 'OS-demo2', 'OS-demo_', 'practice.py', 'SharpKeys.exe', 'Sourcetree.lnk', 'Test Report(2020.09.07 送修)', 'test.osp', 'test.py', 'Visual Studio Code.lnk', 'World of Tanks ASIA.lnk', 'WPS', '~$(微積分甲版) 1080827.docx', '點金靈.LNK']
    

#### 在目前位置創目錄有兩種方法: mkdir() 與 makedirs()。
#### 差別是 makedirs() 可以在用更深的目錄(目錄裡還有目錄)，mkdir() 則只能創造一層的目錄。
#### <font color = 'red'>因此在創建目錄時，建議使用 os.makedirs()</font>


```python
os.mkdir('OS-demo_')
```


    ---------------------------------------------------------------------------

    FileExistsError                           Traceback (most recent call last)

    <ipython-input-6-0a8a805e5bd1> in <module>
    ----> 1 os.mkdir('OS-demo_')
    

    FileExistsError: [WinError 183] 當檔案已存在時，無法建立該檔案。: 'OS-demo_'



```python
os.makedirs('OS-demo2/second-dir_') # 用 os.mkdir() 會出現錯誤。
```


    ---------------------------------------------------------------------------

    FileExistsError                           Traceback (most recent call last)

    <ipython-input-7-b09ad02c297c> in <module>
    ----> 1 os.makedirs('OS-demo2/second-dir_') # 用 os.mkdir() 會出現錯誤。
    

    c:\users\user\appdata\local\programs\python\python37-32\lib\os.py in makedirs(name, mode, exist_ok)
        219             return
        220     try:
    --> 221         mkdir(name, mode)
        222     except OSError:
        223         # Cannot rely on checking for EEXIST, since the operating system
    

    FileExistsError: [WinError 183] 當檔案已存在時，無法建立該檔案。: 'OS-demo2/second-dir_'


#### 同樣道理: rmdirs() 與 removedirs()。
#### <font color = 'red'>但在刪除目錄時，建議用 rmdirs()。因為比較不易出錯。</font>


```python
os.rename('OS-demo', 'os-demo')
```


```python
os.stat('os-demo') # 列出目標檔案的相關數據
# 注意到 st_mtime: 這是這個檔案最後被修改的時間
```




    os.stat_result(st_mode=16895, st_ino=98516241848731915, st_dev=486342311, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1600051928, st_mtime=1600047626, st_ctime=1600047626)




```python
print(os.stat('os-demo').st_mtime)
# st_mtime 是 stat 的一個 attribute。但這資料人類看不懂
```

    1600047626.5589492
    

>實例所顯示的時間信息顯然不是我們所想像的那種年-月-日時:分:秒。  
這是因為系統記錄的時間是一個整數，這個整數表示自1970年1月1日00:00:00（國際標準時間）以來到時間記錄所要表達的時間所經過的秒數。  
如果要讓時間能看人肉眼看懂，還需要一些時間處理函數，例如時區轉換、時間的格式化輸出函數等。  
這種表示法稱為日曆時間。  


```python
# 方法是用 datetime 模組:
from datetime import datetime

mod_time = os.stat('os-demo').st_mtime
print(datetime.fromtimestamp(mod_time))
# 成功顯示時間
```

    2020-09-14 09:40:26.558949
    

### 非常重要的技能: 列出所有檔案。
#### 如果今天你知道檔案在桌面，但卻不知道在哪個資料夾，甚至你要的東西在資料夾內的資料夾...
#### 這時就可以用 os.walk() 來迴圈 [他會回傳包含三個值的 tuple，存放<font color = 'red'> 目錄路徑，目錄名稱，目錄裡的檔案名稱</font>] 


```python
for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('Current Path', dirpath)
    print('Directories', dirname)
    print('Files', filename)
    print()
```

    Current Path C:\Users\User\Desktop
    Directories ['Google Office', 'os-demo', 'OS-demo2', 'OS-demo_', 'Test Report(2020.09.07 送修)', 'WPS']
    Files ['Blair - Chrome.lnk', 'Cisco Webex Meetings.lnk', 'desktop.ini', 'Game Center.lnk', 'LINE.lnk', 'MinGW Installer.lnk', 'OneSafe PC Cleaner.lnk', 'practice.py', 'SharpKeys.exe', 'Sourcetree.lnk', 'test.osp', 'test.py', 'Visual Studio Code.lnk', 'World of Tanks ASIA.lnk', '~$(微積分甲版) 1080827.docx', '點金靈.LNK']
    
    Current Path C:\Users\User\Desktop\Google Office
    Directories []
    Files ['Google Docs.lnk', 'Google Sheets.lnk', 'Google Slides.lnk']
    
    Current Path C:\Users\User\Desktop\os-demo
    Directories []
    Files []
    
    Current Path C:\Users\User\Desktop\OS-demo2
    Directories ['second-dir', 'second-dir_']
    Files []
    
    Current Path C:\Users\User\Desktop\OS-demo2\second-dir
    Directories []
    Files []
    
    Current Path C:\Users\User\Desktop\OS-demo2\second-dir_
    Directories []
    Files []
    
    Current Path C:\Users\User\Desktop\OS-demo_
    Directories []
    Files []
    
    Current Path C:\Users\User\Desktop\Test Report(2020.09.07 送修)
    Directories ['Detailed Report']
    Files []
    
    Current Path C:\Users\User\Desktop\Test Report(2020.09.07 送修)\Detailed Report
    Directories []
    Files ['K2NRCX00K91509C.pdf']
    
    Current Path C:\Users\User\Desktop\WPS
    Directories []
    Files ['Excel 2016.lnk', 'Power point 2016.lnk', 'Word 2016.lnk']
    
    

#### 假設我今天要在 HOMEPATH 增加一個 test.txt 檔:


```python
print(os.environ)  # 查看電腦環境變數: 本機 -> 內容 -> 進階系統設定 -> 環境變數
```

    environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\User\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'LLH', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\User', 'LOCALAPPDATA': 'C:\\Users\\User\\AppData\\Local', 'LOGONSERVER': '\\\\LLH', 'NUMBER_OF_PROCESSORS': '12', 'ONEDRIVE': 'C:\\Users\\User\\OneDrive', 'ONEDRIVECONSUMER': 'C:\\Users\\User\\OneDrive', 'OS': 'Windows_NT', 'PATH': 'c:\\users\\user\\appdata\\local\\programs\\python\\python37-32\\lib\\site-packages\\pywin32_system32;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\iCLS\\;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;C:\\Windows\\System32\\OpenSSH\\;C:\\Program Files (x86)\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\Intel(R) Management Engine Components\\DAL;C:\\Program Files\\Intel\\WiFi\\bin\\;C:\\Program Files\\Common Files\\Intel\\WirelessCommon\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA NvDLISR;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files\\Git\\cmd;C:\\MinGW\\bin;C:\\Program Files (x86)\\Vim\\vim82;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37-32\\Scripts\\;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37-32\\;C:\\Users\\User\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\heroku\\bin', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.CPL', 'PROCESSOR_ARCHITECTURE': 'x86', 'PROCESSOR_ARCHITEW6432': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 158 Stepping 10, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '9e0a', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files (x86)', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Users\\User\\Documents\\WindowsPowerShell\\Modules;C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\User\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\User\\AppData\\Local\\Temp', 'USERDOMAIN': 'LLH', 'USERDOMAIN_ROAMINGPROFILE': 'LLH', 'USERNAME': 'User', 'USERPROFILE': 'C:\\Users\\User', 'WINDIR': 'C:\\WINDOWS', 'WSLENV': 'WT_SESSION::WT_PROFILE_ID', 'WT_PROFILE_ID': '{61c54bbd-c2c6-5271-96e7-009a87ff44bf}', 'WT_SESSION': '670dda9f-cde1-4284-bc8a-969af1e266c1', 'JPY_INTERRUPT_EVENT': '3520', 'IPY_INTERRUPT_EVENT': '3520', 'JPY_PARENT_PID': '2900', 'TERM': 'xterm-color', 'CLICOLOR': '1', 'PAGER': 'cat', 'GIT_PAGER': 'cat', 'MPLBACKEND': 'module://ipykernel.pylab.backend_inline'})
    


```python
print(type(os.environ))
```

    <class 'os._Environ'>
    


```python
print(os.environ.get('HOMEPATH')) # 查看名稱為 HOMEPATH 的環境變數的路徑。
```

    \Users\User
    


```python
file_path = os.environ.get('HOMEPATH') + 'test.txt'
print(file_path)

# Naive 的想法是直接把你要新增的檔案名稱加在目標位置的後面，但會有個問題: "\" 會亂掉。
# 因此應該用 os.path.join()
```

    \Users\Usertest.txt
    


```python
file_path2 = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(file_path2)
```

    \Users\User\test.txt
    


```python
print(os.path.isfile(file_path2))
```

    True
    


```python
print(dir(os.path))
```

    ['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfullpathname', '_getvolumepathname', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys']
    


```python

```
