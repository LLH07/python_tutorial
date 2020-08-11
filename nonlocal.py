# 我將用一隻範例程式來解說 nonlocal 的概念。
# 判斷順序: LEGB。
'''
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer() 
印出 inner x(來自 inner x function 的 local), outer x(來自 outer x function 的 local)。
'''

'''
def outer():
    x = 'outer x'
    def inner():
        print(x)
    inner()
    print(x)
outer()
印出 outer x(在 inner function 找不到 x，但在 enclosing 的 function(就是 outer) 找到 x)
與 outer x(來是 outer function 的 local)
'''

'''
def outer():
    def inner():
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer()
印出錯誤訊息。因位在執行第 34 行的 print(x) 時，x 不在 local，也不在 enclosing(他根本沒有 enclosing)
，也不在 global，也不在 python 的 Built-in 裡，故出現錯誤。
'''

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
    inner()
    print(x)
outer()
印出 inner x, inner x。第一個 inner x 來自第 45 行的 print(x)。第 47 行的 print(x)，由於我在裡面的 function
設定 x 是 nonlocal(想像成它不是 inner() 的 local，所以做的事會影響外面的 outer())
因此還是印出 inner x。
