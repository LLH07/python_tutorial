Python 判斷變數範圍的順序是: LEGB。
    即: Local, Enclosing, Global, Built-in
可以使用:
    import builtins
    print(dir(builtins)) 
來查看 python 裡的 Built-in 變數。