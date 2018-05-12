'''
Created on 2018. 5. 12.

@author: Administrator
'''
from konlpy.tag import Twitter

twitter = Twitter()

text = "아버지 가방에 들어가신다."

malist = twitter.pos(text, norm = True, stem = True)

print(type(malist))
print(malist)

for myitem in malist:
    print("단어:", myitem[0], end="")
    print(",품사:", myitem[1])