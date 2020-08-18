first_name = 'Lebeon'
last_name = 'James'

# 如果想要印出一個句子，其中有很多自己定義的變數，或許可以用 format 方法來寫。
# 但其缺點是當有很多變數時，必須要一個一個對照。
# 此時可以用 f-string 。
sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

# fstring:
sentence2 = f'My name is {first_name} {last_name}'
print(sentence2)

# 進一步，裡面可以再加入其他 method:
sentence3 = f'My name is {first_name.upper()} {last_name.upper()}'

# 範例 1:
for n in range(1, 11):
    sentence = f'The value is {n:02}' # 留兩個字元的空間。
    print(sentence)

# 範例 2:
pi = 3.14159265
sentence4 = f'Pi is equal to {pi:.4f}'
print(sentence4)

# 現在想要印出某人的生日，可以用:
from datetime import datetime
birthday = datetime(1999, 1, 1)
sentence5 = f'Jay has a birthday on {birthday}'
# 印出 Jay has a birthday on 1999-01-01 00:00:00
# 但我希望印出 January 01, 1999 的格式:
sentence6 = f'Jay has a birthday on {birthday:%B %d, %Y}'
print(sentence6)

# datetime 的 format 參數可以上網自行查找。