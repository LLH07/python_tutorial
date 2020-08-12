# 任務一: 找出 urls 內的所有網站名稱。
import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

# step 1: 有些是 https，有些是 http: 使用 ?
# step 2: 大家都有 '://': 直接打
# step 3: 有些有 www.，有些沒有: 使用 ?
# step 4: 不管有沒有 www.，大家都有一個 domain(即 google, coreyms...): 使用 \w+
# step 5: 找出 top level domain(即 .com, .gov): 使用 \.\w+

# 有相關的就把它們作為一個 group。這時有 4 個 groups:
# 第 0 個 group: 所有符合結果的。
# 第 1 個 group: 有 www. 則會顯示，沒有則為 None。
# 第 2 個 group: 印出各網站的 domain。
# 第 3 個 group: 印出各網站的 top level domain。
# 故可以使用 group method: 
for match in matches:
    print(match.group(0))

# 進一步利用:
subbed_urls = pattern.sub(r'\2\3', urls)
# 製造 subbed_urls，其內容是 pattern 的第 2 個 group + 第 3 個 group。
print(subbed_urls)

