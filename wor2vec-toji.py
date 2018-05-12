'''
Created on 2018. 5. 12.

@author: Administrator
'''
import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec
# utf-16 인코딩으로 파일을 열고 글자를 출력하기 --- (※1)
fp = codecs.open(filename='BEXX0003.txt', mode='r', encoding='utf-8')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text') # 여러 개의 태그 중에서 첫 번째만 선택한다.(카페 62)
text = body.getText()
# print( text )
# 텍스트를 한 줄씩 처리하기 --- (※2)
twitter = Twitter()
results = []
lines = text.split('\r\n')
# print( lines )
for line in lines : # 형태소 분석하기 --- (※3) # 단어의 기본형 사용
 malist = twitter.pos(line, norm=True, stem=True)
# print( malist )
 r = []
 for word in malist : # 어미/조사/구두점 등은 대상에서 제외
     if not word[1] in ["Josa", "Eomi", "Punctuation"]: 
         r.append(word[0]) 
         rl = (" ".join(r)).strip() 
         results.append(rl)
# print(rl)
# 파일로 출력하기 --- (※4)
wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp : 
    fp.write('\n'.join(results))
# Word2Vec 모델 만들기 --- (※5)
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200,
                          window=10, hs=1, min_count=2, sg=1)
saved_file_name = 'toji.model'
model.save( saved_file_name )
print( '파일 ', saved_file_name, ' 저장 완료')