import cx_Oracle
import matplotlib.pyplot as plt
import matplotlib
from pandas.core.series import Series
from matplotlib import font_manager, rc

con = cx_Oracle.connect('oraman/oracle@localhost:1521/xe', encoding='utf-8')

cur = con.cursor()

cur.execute('select * from region_summary_ranking')

data = [] # 발생 빈도
myindex = [] # 분기 이름(비율)

total = 0 
for result in cur:
    print(result)
    total += result[1]
    data.append( result[1] )
    myindex.append( result[0])

print( total )
newindex = []
for idx in range(len(myindex)):
    newindex.append(myindex[idx] + '\n(' + str(round(100 * data[idx]/total, 2))  + '%)') 

print(newindex)
font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name()
matplotlib.rc('font', family=font_name)

chartData = Series(data, index = myindex)
chartData.plot(kind='barh', rot = 18, alpha=0.7, title = '지역별 범죄  발생 빈도(5~8위)')
plt.show()

chartData = Series(data, index = newindex)
chartData.plot(kind='pie', title = '지역별 범죄  발생 빈도(5~8위)')
plt.show()

cur.close()
con.close()


