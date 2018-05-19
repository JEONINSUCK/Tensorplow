import cx_Oracle
import matplotlib.pyplot as plt
import matplotlib 
from pandas.core.series import Series
from pandas.core.frame import DataFrame
from matplotlib import font_manager, rc

con = cx_Oracle.connect('oraman/oracle@localhost:1521/xe')

cur = con.cursor()

cur.execute('select * from view_region_total_two')

data0 = [] # 국가 이름
data1 = [] # 테러 발생 년도
data2 = [] # 테러 발생 빈도

# 다음 4개 지역의 2013년도와 2014년도에 대한 데이터를 조회하여 수직 막대 그래프를 그리시오.
# Western Europe, Sub-Saharan Africa, Southeast Asia, South Asia
myregion = ['Western Europe', 'Sub-Saharan Africa', 'Southeast Asia', 'South Asia']
for result in cur:
    if(result[1] == 2013 or result[1] == 2014):        
        if( result[0] in myregion) :
            data0.append( result[0])
            data1.append( result[1] )
            data2.append( result[2] )

# MultiIndex를 이용하여 시리즈 만들기(카페 50)
myseries = Series(data2, index=[ data0, data1])
  
print(myseries)
 
df = myseries.unstack()
print( df )
 
font_location = 'c:/windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname = font_location).get_name();
matplotlib.rc('font', family=font_name)
 
df.plot(kind ='bar', rot = 0)
plt.title('4개 지역  테러 발생 현황(2013~2014년)')
plt.ylim(0, 5100) 
plt.show()
 
cur.close()
con.close()