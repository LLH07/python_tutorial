sorted(li) -> function
li.sort()  -> method

new_li = li.sort() # 印出 None
new_li = sorted()  # 印出排序好的
這兩者中，sorted() function 是較好的，因為:
    他不只可以排序 list，連 tuple, dictionary 也可以。如果是排序 dictionary，python 會依照 key 來排序。
    sorted(你要排序的，key = 排序的方法)。排序的方法可以是: abs()