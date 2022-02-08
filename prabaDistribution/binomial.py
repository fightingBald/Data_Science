# _*_ coding : utf-8 _ * _ 
# @Time : 07/02/2022 16:25
# @Author : Huayi TANG
# File : binomial
# @Project : Data_Science
import matplotlib
import numpy as np
import scipy.stats as stats
import matplotlib.style as style
import matplotlib.pyplot as plt
from IPython.core.display import HTML

#TODO 画布 plt.rcParams参数设置
# 参数设定
from scipy.stats import binom

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['figure.figsize'] = (14,7)#TODO 调整生成的图表最大尺寸
style.use('fivethirtyeight')#TODO 设置画布背景
                            # 参数可以是一个 URL 或者路径，指向自己定义的 mplstyle 文件
fig = plt.figure(dpi=100)#TODO 设置分辨率 每英寸点数

plt.xlabel("赢球场次")  #设置X轴Y轴名称
plt.ylabel("柱状图-概率 红线-密度累计曲线")
plt.title("二项分布：\n"
          "我每场球赢球概率为0.5， 明天我要打20场球,我20场球里赢n场分别对应的概率")

plt.ylim(0,1.5) #设置y轴上下限

#arange([start,]
        # stop[,
        # step,],
# dtype=None)
#生成一个 ndarray
print(np.arange(20))#[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(type(np.arange(20)))#<class 'numpy.ndarray'>

#PMF（连续性叫PDF）
#柱子的位置由x以及align确定 ，柱子的尺寸由height和 width 确定
#垂直基准位置由bottom确定(默认值为0
vertor_X= np.arange(20)
Proba_Mass_at_X = stats.binom.pmf(#height 表示柱状图的高度，也就是y坐标值，数据类型为int或float类型，
                                vertor_X, # TODO x轴的取值序列
                                p = .5,#每场比赛我赢球的概率
                                n=20 #明天我打20场比赛
                                )
vertor_Y=[round(i,4) for i in Proba_Mass_at_X]

for i in range(0,len(vertor_Y)):
    print('赢球{0}场的概率为{1:.4f}'.format(vertor_X[i],vertor_Y[i]))
bar = plt.bar(x= vertor_X,#x x轴的取值序列，一般采用arange函数产生一个序列；
                        #TODO 序列 每根柱子以哪个准确的x坐标值为中心点
        height=vertor_Y,
        #width=.75,#width 表示柱状图的宽度，取值在0~1之间，默认为0.8
        #alpha=0.75, # alpha：透明度
        label = "横坐标：我能赢n场 竖坐标：其对应的概率",
        tick_label =  np.arange(20),#tick_label 下标标签
        color= 'green' ,#柱状图颜色
        edgecolor = 'black', #边框颜色
        linewidth='2', #边框宽度
        #orientation= 'vertical'# 柱状图是竖直还是水平，竖直："vertical"，水平条："horizontal"#
        )
# 显示数据标签
plt.bar_label(bar, label_type='edge')
plt.legend(loc="upper left") # plt.bar(TODO Lable)
                            # 的位置在左上，没有这句会找不到label去哪了


#CDF（累计密度函数）

vertor_CDF=stats.binom.cdf(#height 表示柱状图的高度，也就是y坐标值，数据类型为int或float类型，
                                vertor_X, # TODO x轴的取值序列
                                p = .5,#每场比赛我赢球的概率
                                n=20, #明天我打20场比赛
                                )
plt.plot(vertor_X,vertor_CDF,color = 'red')










#LEGEND# 用于设置文字说明
plt.text(x=4, y=0.7, #（x，y）参数是句子尾的坐标。
        s='PMF(已经过标准化)',
        alpha= 1,
        fontsize=15,
        weight='bold',
        color= "green",
        verticalalignment = "top",
        horizontalalignment = "right"
)
plt.text(x=14.5, y=0.9, #（x，y）参数是句子尾的坐标。
        s='CDF',
        alpha= 0.75,
        fontsize=15,
        weight='bold',
        color= "red",
        #verticalalignment = "top",
        #horizontalalignment = "right"
)

#TICKS(刻度)
tick = print(range(21)[::2])#python3 中range返回的是一个itrable 类为range的对象 而不再是列表
for i in range(21)[::2]:
    print(i)
# 0
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20
plt.xticks(tick)
plt.tick_params(axis='both',#选择对哪个轴操作，默认是’both’
                which='major',#可选{‘major’, ‘minor’, ‘both’} 选择对主or副坐标轴进行操作
                labelsize = '18'#float/str, 刻度值字体大小
                )
#绘制平行于x轴的水平参考线
plt.axhline(y = 0.005,
            color='black',
            linewidth = 1.3,
            alpha=.7)



#TITLE SUBTITLE &FOOTER
plt.text(x = 4,y = 0.8,
         s = '以下是二项分布的概率质量函数PMassF以及累计概率函数CumulativeDensityFunction',
         fontsize = 10,
         weight='bold',
         alpha=0.85
         )
# plt.text(x = -2.5,y = 1.25,
#          s = '二项分布--OVERView',
#          fontsize = 26,
#          weight='bold',
#          alpha=0.75
#          )










#TODO 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥从上到下执行 画上去就不管上一个了🔥🔥🔥🔥🔥🔥
#TODO 🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥从上到下执行 画上去就不管上一个了🔥🔥🔥🔥🔥🔥
fig = plt.figure()#🔥🔥🔥🔥🔥开一个新画布 接下来的所有代码 再开新画布之前都是这个画布上的🔥🔥
Proba_Mass_at_X = stats.binom.pmf(
                                vertor_X, # TODO x轴的取值序列
                                p = .2,#每场比赛我赢球的概率
                                n=20 #明天我打20场比赛
                                )
vertor_Y=[round(i,4) for i in Proba_Mass_at_X]
plt.scatter(vertor_X,vertor_Y)
plt.plot(vertor_X,vertor_Y,
         label='姜书峰胜率0.2打20场球',)


Proba_Mass_at_X = stats.binom.pmf(
                                vertor_X, # TODO x轴的取值序列
                                p = .5,#每场比赛我赢球的概率
                                n=20 #明天我打20场比赛
                                )
vertor_Y=[round(i,4) for i in Proba_Mass_at_X]
plt.scatter(vertor_X,vertor_Y)
plt.plot(vertor_X,vertor_Y,label='我胜率0.5打20场球')


Proba_Mass_at_X = stats.binom.pmf(
                                vertor_X, # TODO x轴的取值序列
                                p = .8,#每场比赛我赢球的概率
                                n=20 #明天我打20场比赛
                                )
vertor_Y=[round(i,4) for i in Proba_Mass_at_X]
plt.scatter(vertor_X,vertor_Y)#散点图
plt.plot(vertor_X,vertor_Y,label='乔丹胜率0.8打20场球')#连线图

plt.legend(loc="upper left")
plt.show()



#TODO 随机构造符合二项分布的样本 用什么函数构造样本
# 他们肯定就满足什么分布（在这里是 十次试验里实验成功的次数-
#                           '赢几次球' 这个事件满足二项分布 ）
#
fig = plt.figure()
singleSample_seed1 = binom.rvs(p=0.5,n=10,size = 1)
print(singleSample_seed1)
#就他妈一次 胜场次只有一个数据
# 换言之 采样只有一个
# 能看出来个几把分布 我考试考砸了一次就说明我水平拉么
# 采他妈个20次！TODO 胜率0.5👇
sample_seed1 = binom.rvs(p=0.5,n=10,
                         size = 20)
print(sample_seed1) #在无数个胜率为0.5的人打十场球
                    # 随机 采20个样- 采他们获胜次数
#                       这里可以看成一届巡回赛10场比赛
#                       我他妈打了20次巡回赛所采集到的数据
#                       满足相应参数的二项分布
#[4 6 3 4 5 6 6 5 3 7 3 5 6 5 4 6 5 6 4 6]
plt.scatter(range(0,sample_seed1.size),sample_seed1)#散点图
plt.plot(range(0,sample_seed1.size),sample_seed1,color='blue')#连线图
# 采他妈个20次！TODO 胜率0.3👇
sample_seed1 = binom.rvs(p=0.3,n=10,
                         size = 20)
print(sample_seed1)
#[4 6 3 4 5 6 6 5 3 7 3 5 6 5 4 6 5 6 4 6]
plt.scatter(range(0,sample_seed1.size),sample_seed1)#散点图
plt.plot(range(0,sample_seed1.size),sample_seed1,color='darkblue')#连线图










#TODO 以下一个胜率0.2 一个胜率0.9 都是采样80次
sample_seed2 = binom.rvs(p=0.2,n=10,
                         size = 80)
print(sample_seed2)#在无数个胜率为0.2的人打十场球 他们获胜次数
                    # 随机 采80个样- 采他们获胜次数
plt.scatter(range(0,sample_seed2.size),sample_seed2)#散点图
plt.plot(range(0,sample_seed2.size),sample_seed2,color= 'orange')#连线图

sample_seed2 = binom.rvs(p=0.9,n=10,
                         size = 80)
print(sample_seed2)#在无数个胜率为0.2的人打十场球 他们获胜次数
                    # 随机 采80个样- 采他们获胜次数
plt.scatter(range(0,sample_seed2.size),sample_seed2)#散点图
plt.plot(range(0,sample_seed2.size),sample_seed2,color= 'orange')#连线图
plt.show()

