'''
Created on 2018. 5. 19.

@author: Administrator
'''
import cx_Oracle
from pandas import Series
import matplotlib.pyplot as plt

id = "oraman/oracle@localhost:1521/xe"
con = cx_Oracle.connect(id)

cur = con.cursor()

sql = "select * from BUNGITABLE"
cur.execute(sql)

Bungi = []
Count = []
total = 0

for pars in cur:
    print(pars)
    total += pars[1]
    Bungi.append(pars[0])
    Count.append(pars[1])

RealSeries = []
for parsent in range(len(Count)):
    RealSeries.append(Bungi[parsent] + "\n" + str(round(100*(Count[parsent]/total),2)))
print(RealSeries)

plt.rcParams["font.family"] = 'Nanum Brush Script OTF'

Bungiseries = Series(Count,index = RealSeries)
Bungiseries.plot(kind = 'pie')

plt.show()
cur.close()
con.close()



