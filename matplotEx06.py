'''
Created on 2018. 5. 12.

@author: Administrator
'''
from matplotlib import font_manager, rc
import matplotlib
import matplotlib.pyplot as plt
from pygments.formatters.img import DEFAULT_FONT_NAME_WIN


font_location ="c:/Windows/fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc("font",family = DEFAULT_FONT_NAME_WIN)

plt.plot([1,2,3,4],[5,6,7,8])
plt.xlabel("x 축 한글표시")
plt.title("matplotlib 활용")
plt.show()
