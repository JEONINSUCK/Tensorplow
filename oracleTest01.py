'''
Created on 2018. 5. 19.

@author: Administrator
'''
import cx_Oracle
import matplotlib.pyplot as plt
import matplotlib
from pandas.core.series import Series
from matplotlib import font_manager, rc

con = cx_Oracle.connect('oraman/oracle@localhost:1521/xe')

# cur : 커서 객체(메모리에 로딩되어 있는 데이터 집합체)
cur = con.cursor()

sql = "select * from country_summary_top_10"
cur.execute(sql)

# print(type(cur))
# print(cur)
# print(type(con))


data = []
myindex = []

for result in cur:
    print(result)
    data.append(result[1])
    myindex.append(result[0])
    
# 한글깨짐 처리

font_location = "c:\\windows\\fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname = font_location).get_name()
matplotlib.rc('font',family = font_name)

# print(myindex)
chartData = Series(data, index = myindex)
chartData.plot(kind = 'bar', rot = 30, grid = True, title = '범죄 빈도수 Top 10 국가', alpha = 0.6)
matplotlib.pyplot.show()
cur.close()
con.close()