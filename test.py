from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#print(x)

#TODO  🆘🆘🆘🆘🆘🆘🆘解决matplotlib中文显示乱码🆘🆘🆘🆘🆘🆘🆘🆘
# TODO python还是自带可以显示中文的字体的，输入如下代码可以查看系统可用字体
# from matplotlib.font_manager import FontManager
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
# TODO 上面的代码大家有兴趣可以自己去尝试着玩一下，下面才是重点🆘🆘🆘🆘🆘🆘🆘🆘🆘🆘🆘🆘
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']





#Numpy random.poisson() 泊松分布
#返回：以numpy数组形式返回随机样本
x = random.poisson(lam=2, size=10)

# 一、泊松分布问题：
# 假设我每天接到骚扰电话的次数服从泊松分布，并且经统计平均每天我会接到20个骚扰电话。
# 请问：
# 1、我明天接到15个骚扰电话的概率？
# 2、我明天接到24个骚扰电话以下的概率（包含24）？
from scipy import stats

p = stats.poisson.pmf(15, 20)
print("接到15个骚扰电话的概率：", p)

p = stats.poisson.cdf(24, 20)
print("接到24个骚扰电话以下的概率：", p)

from scipy import stats
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

X = range(0, 51)
Y = []
for k in X:
    p = stats.poisson.pmf(k, 20)
    Y.append(p)

plt.bar(X, Y, color="red")
plt.xlabel("次数")
plt.ylabel("概率")
plt.title("接到骚扰电话次数及概率")
plt.show()