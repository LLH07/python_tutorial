# 直接用例子來解釋為和要用 named tuple:
# 假設我現在想要表達 RGB 三個顏色，我們或許可以這樣做:

color = (55, 155, 255)
print(color[0]) # 印出 55。
# 但幾個月後你回來看，應該會忘記這三個數字代表甚麼意思。

# 方法二:
color_dict = {'red':55, 'green':155, 'blue':255}
print(color_dict['red']) # 印出 55。
# 缺點是要打很多字。

# Named Tuple 就是結合 tuple 跟 dictionary 的產物。
# 至於為何要用 tuple? 因為 tuple 是 inmutanble。

# Named Tuple:
from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue']) # 創造 named tuple。

color = Color(55, 155, 255) # 變數 color，他是一個 named tuple。
# color = (55, 155, 255) 是原本的寫法。

white = Color(255, 255, 255) # 這樣代表白色，的確好懂許多。

print(color[0])
print(color.red) # 都會印出 55。