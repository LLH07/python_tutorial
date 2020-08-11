影片網址: https://www.youtube.com/watch?v=QVdf0LgmICw&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=18
Python 判斷變數範圍的順序是: LEGB。
    即: Local, Enclosing, Global, Built-in
可以使用:
    import builtins
    print(dir(builtins)) 
來查看 python 裡的 Built-in 變數。

Enclosing 則是跟 nested function(巢狀函數) 有關。