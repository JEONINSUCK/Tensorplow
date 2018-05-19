'''
Created on 2018. 5. 19.

@author: Administrator
'''

from pandas import DataFrame, Series
import pandas
import numpy

# 계층적 색인이란 축에 2개 이상의 색인을 가지는 것을 말한다
# from pandas.indexes.multi import Multiindex

myseries = Series( (numpy.arange(9) +1)*10,\
                   index = [['강감찬','강감찬','강감찬','김유신','김유신','김유신','이순신','이순신','이순신'],
                            ['갑','을','병','갑','을','병','갑','을','병',]])

print('myseries.index')
print(myseries.index)
print("-" * 30)

print("myseries")
print(myseries)
print("-" * 30)

print("myseries['강감찬']")
print(myseries['강감찬'])
print("-" * 30)

print("myseries[['이순신','강감찬']]")
print(myseries[['이순신','강감찬']])
print("-" * 30)

print( "myseries[:, '을']" )
print( myseries[:, '을'] )
print('-' * 30)

print(myseries.unstack())
print("-" * 30)

print(myseries.unstack(0))
print("-" * 30)

print(myseries.unstack(1))
print("-" * 30)

