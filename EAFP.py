# EAFP(Easier to Ask Forgivness than Permission) 與 Duck typing 想表達
# 的意思是一樣的: 寫 code 時，做就對了! 如果有例外錯誤，再想辦法解決他。

# 先舉一個相反的例子，這種風格叫 LBYL(Look Before You Leap，又可稱 Non-Pythonic)
# 現在有一個字典，我們想將值表示出來:
person = {'name': 'Jess', 'age': 23, 'job':'Programmer'}

if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} age years old. I am a {job}.".format(**person))
else:
    print("Missing some keys.")

# 這個程式是可以正常運作的。但缺點是不易讀懂，且再寫之前要考慮的很全面(要確認姓名，年齡，職業都在字典中)
# 邏輯是先確認條件，再給 permission。

# EAFP(Pythonic) 的寫作風格:
try:
    print("I'm {name}. I'm {age} age years old. I am a {job}.".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))

# 可以看出明顯不同是這次直接讓你做，如果有例外情形，再做處理。