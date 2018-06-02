import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name()
matplotlib.rc('font', family=font_name)

thetherfile = "C:\\Users\\user\\Desktop\\Tenserflow\\thether.csv"
colnames = ['id', 'theater', 'cnt'] # 제목으로 넣을 컬럼 이름
dfthether = pd.read_csv( thetherfile, names=colnames, header=None )
dfthether = dfthether.rename(index=dfthether.id)
dfthether = dfthether.reindex(columns=['theater', 'cnt'])
dfthether.index.name = 'id'
# print( dfthether )
# print( )

# 극장별('theater') 상영 횟수('cnt') 집계
mygrouping = dfthether.groupby('theater')['cnt']
sumrSeries = mygrouping.sum()
meanSeries = mygrouping.mean() # 평균
sizeSeries = mygrouping.size()

df = pd.concat([sumrSeries,meanSeries,sizeSeries],axis=1)
df.columns = ['합계','평균','개수']
print(df)

df.plot(kind='barh', rot=0)
plt.title('3개 극장 집계 데이터')
# plt.show()
# plt,savefig()


labels = []
explode = ()
for key in sumrSeries.index:
    mydata = key + '(' + str(sumrSeries[key]) + ')'
    labels.append(mydata)
    explode = explode + (0,)

fig1, ax1 = plt.subplots()
mytuple = tuple(labels)
ax1.pie(sumrSeries, explode=explode, labels=mytuple, autopct='%1.1f%%', shadow=False, startangle=90)
ax1.axis('equal')
plt.show()