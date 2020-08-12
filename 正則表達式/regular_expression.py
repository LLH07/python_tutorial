# 以下例子都使用 Regexs.md 當參考。
# raw string -> 叫 python 把 "/" 當作其字面上的意思。

import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

pattern = re.compile(r'abc') # 這是我要找的 pattern
matches = pattern.finditer(text_to_search) # 在 text_to_research 中找符合的結果


# 範例一: 將 text_to_search 中的電話號碼過濾出來。
pattern2 = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d') 
# [.-] 稱為 character set。 會找出 '.' 或 '-' 任一符合的資料。注意，只會 match 其中一個。
# 所以它是找不到 321--555--4321 的。
matches2 = pattern2.finditer(text_to_search)
print("-------------------------------------------------------------------------")

# 範例二: 
pattern3 = re.compile(r'[1-5]') # 找出範圍在 1 到 5 的結果。
pattern4 = re.compile(r'[89]00[.-]\d\d\d[.-]\d\d\d\d') # 找出 800-555-1234 與 900-555-1234
pattern5 = re.compile(r'[a-zA-Z]') # 找出有出現英文字母的結果(大寫或小寫)
# 像 pattern2 這種打法很容易出錯，因此可以使用 quantifiers:
pattern6 = re.compile(r'\d{3}.\d{3}.\d{4}')

# 範例三: 將 text_to_search 中男士的名字找出來。
pattern7 = re.compile(r'Mr\.?\s[A-Z]\w*')
# 有些 Mr 後有一點，有些沒有: 使用 '?'。
# 有人的姓氏只有一個字母(即 Mr. T): 使用 '*'。

# 範例四: 將 text_to_search 中所有的名字找出來。
pattern8 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# 將結果以 re.Match object 方式呈現。
matches8 = pattern8.finditer(text_to_search)

# 將結果以 list 方式呈現。
matches_l_8 = pattern8.findall(text_to_search)
for match in matches8:
    print(match)


# 更多 method:
sentence = 'Start a sentence and then bring it to an end'
pattern9 = re.compile(r'Start')
matches2 = pattern9.match(sentence)
print(matches2) # 印出 <re.Match object; span=(0, 5), match='Start'>

pattern10 = re.compile(r'then')
matches3 = pattern10.match(sentence)
print(matches3) # 印出 None，因為 match() 只能找尋 sentence 的第一個字。

# 如果要搜尋整個 string:
pattern11 = re.compile(r'then')
matches4 = pattern11.search(sentence)
print(matches4) # 印出 <re.Match object; span=(21, 25), match='then'>
# 沒找到一樣回傳 None。

# flag:
# 如果你要找的字大小寫混砸，你可能想用 pattern12 的寫法。
# 但 pattern13, pattern14 的結果一樣可以達成。
pattern12 = re.compile(r'[Ss][Tt][Aa][Rr][Tt]')
pattern13 = re.compile(r'start', re.IGNORECASE) # IGNORECASE 不管大小寫，只要字是對的，就找的到。
pattern14 = re.compile(r'start', re.I)

matches5 = pattern14.search(sentence)
print(matches5)
