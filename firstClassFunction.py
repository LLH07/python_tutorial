# First Class Funcion 總歸一句話: function 是一種 object。
# 也就是說，function 可以被當作回傳值，可以被當作別的 function 的 parameters。
# 或可以被當作變數。
# 直接舉例:
def square(x):
    return x * x

f = square(5)
f2 = square
print(square) # 印出 <function square at 0x00E307C8>。
print(f2) # 印出 <function square at 0x010507C8>
print(f2(5)) # 印出 25
print(f) # 印出 25
# 這時候 f2 就是 square 這個 function。

# funcion 作為回傳值:
def logger(msg):
    def log_message():
        print('Log', msg)
    return log_message
log_hi = logger('HI!')
log_hi() # 印出 Log HI!

'''
可以看出當 logger() 被呼叫並將 'HI!' 參數丟入，log_message() 這個 inner function
同時接收了 'HI!'。但在 21 行時，我們只是將呼叫 logger()並回傳 log_message 這個 function
是直到第 22 行才呼叫 log_hi，因此印出 Log HI!。

至於 log_hi 會記住 'HI!' 這個參數，是因為一個叫做 closure 的特性。
'''
# 補充: python 內建的 map 函數就是使用 first class function 的概念。