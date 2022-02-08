# _*_ coding : utf-8 _ * _ 
# @Time : 07/02/2022 17:39
# @Author : Huayi TANG
# File : bar
# @Project : Data_Science
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(9,6))
n = 8
X = np.arange(n)+1 #X是1,2,3,4,5,6,7,8,柱的个数

#TODO 生成n个
# uniform(0.5,1.0)均匀分布的随机数
# normal正态分布的随机数
Y1 = np.random.uniform(0.5,
                       1.0,
                       n)
plt.bar(X,
        Y1, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='one', lw=1)

#TODO 生成n个
# uniform(0.5,1.0)均匀分布的随机数
Y2 = np.random.uniform(0.5,
                       1.0,
                       n)
plt.bar(X+0.35,
        Y2,
        alpha=0.9, width = 0.35, facecolor = 'yellowgreen', edgecolor = 'white', label='second', lw=1)



plt.legend(loc="upper left") # label的位置在左上，没有这句会找不到label去哪了

plt.show()
