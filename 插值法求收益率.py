




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl #从pylab导入子模块mpl
mpl.rcParams["font.sans-serif"] = "SimHei" #以黑体显示中文
mpl.rcParams["axes.unicode_minus"]=False #解决保存图像是负号'-'显示为方块的问题

from scipy import interpolate
t=np.array([0.25,0.5,0.75,1.0,3.0,5.0])   #生成仅包含已有期限的数组
t_new=np.array([0.25,0.5,0.75,1.0,2.0,3.0,4.0,5.0])   #生成包括2年和4年的新数组
rates=np.array([0.027344,0.027898,0.028382,0.02882,0.030414,0.031746])      #生成仅包含已有利率的数组
types=["nearest","zero","slinear","quadratic","cubic"]      #生成包含插值方法的列表
plt.figure(figsize=(8,6))
for i in types:
    f=interpolate.interp1d(x=t,y=rates,kind=i)
    rates_new=f(t_new)
    print(i,rates_new)
    plt.plot(t_new,rates_new,'o')
    plt.plot(t_new, rates_new, '-',label=i)
    plt.xticks(fontsize=13)
    plt.xlabel(u'期限',fontsize=13)
    plt.yticks(fontsize=13)
    plt.ylabel(u'收益率',fontsize=13,rotation=90)
    plt.legend(loc=0,fontsize=13)
    plt.grid()
plt.title(u'用插值法求2年期和4年期的远期国债到期收益率',fontsize=13)
plt.savefig('Figure_7', dpi=500)
plt.show()