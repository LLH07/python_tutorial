# Decorator 就是將 function A 當作 function B 的 parameter。
# 直接來個例子吧:
def decorator_func(original_func):
    def wrapper_func(*args, **kwargs): # 3. 回傳值的真實內容。
        print('在 display function 被執行前')
        return original_func(*args, **kwargs)
    return wrapper_func # 2. 變數的內容就是這個回傳值。


def display():
    print('Display function ran')

'''
decorated_display = decorator_func(display) # 1. 創建變數 decorated_display
decorated_display() # 4. 執行變數。
'''

# 上面是 decorator 做簡單的舉例。第 12-13 行看起來滿亂的，因此可以這麼修改:
@decorator_func
def display():
    print('display function ran')
display() # 跟 display = decorator_func(display)，並 display() 的意思是一樣的。

@decorator_func
def display_info(name, age):
    print('display_info ran with arguments: ({}, {})'.format(name, age))

display_info('John', 25) # 出現錯誤訊息-> TypeError: wrapper_func() takes 0 positional arguments but 2 were given

# 要解決這個問題，只要在 decorator function 裡面的 wrapper function 加上關鍵字: *args, **kwargs 即可。
# 注意第 4 行。


'''
    本節重點:
        1. 關鍵字 @
        2. 關鍵字 *args, **kwargs
        3. Decorator 實例: 寫一個測試 function 執行時間的函式，並將它視為 decorator，套用在不同的函數上。
        
'''