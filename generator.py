# 情境: 我們要將 1, 2, 3, 4, 5 轉換成各自平方的形式，即: 1, 4, 9, 16, 25。
def square_numbers(nums):
    result = [] # 先見一個空的 list。
    for i in nums: # nums 是一個 list，遍歷他並將其平方 append 到 result。
        result.append(i * i)
    return result
# 上面這個做法的缺點是太多贅字且如果 nums 有很多資料，result 就需 append 很多次
# 又消耗記憶體。

# 因此可以用 generator。實現方法是關鍵字 yield。他會將 generator 的第一個位置
# 存起來。節省記憶體空間且執行速度較快。
def square_numbers_gen(nums):
    for i in nums:
        yield(i * i)
my_nums = square_numbers_gen([1, 2, 3, 4, 5])
print(my_nums) # 印出 <generator object square_numbers_gen at 0x033D8BB0>
print(next(my_nums)) # 要用 next 方法。此時印出 1 。
# 如果要印出全部，就要:
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
# print(next(my_nums)) # 發生錯誤，因為後面已經沒有東西了。

# 可以用 for 迴圈來避免:
for nums in my_nums:
    print(nums)


# list comprehension 一樣可以用 generator:
my_nums2 = [x * x for x in [1, 2, 3, 4, 5]]
print(my_nums2) # 印出 [1, 4, 9, 16, 25]。

# 用 generator:
my_nums3 = (x * x for x in [1, 2, 3, 4, 5])
print(my_nums3) # 印出 <generator object <genexpr> at 0x0306C930>。

''' 總結:
    1) generator 可以讓 code 看起來易懂舒服。
    2) generator 再資料量大時可以節省許多記憶體。
    3) 要留意回傳的是 generator object。
    4) return function() 是執行函數。return function 是回傳函數
'''
