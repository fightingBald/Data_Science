from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns


#print(x)

#TODO  ðððððððè§£å³matplotlibä¸­ææ¾ç¤ºä¹±ç ðððððððð
# TODO pythonè¿æ¯èªå¸¦å¯ä»¥æ¾ç¤ºä¸­æçå­ä½çï¼è¾å¥å¦ä¸ä»£ç å¯ä»¥æ¥çç³»ç»å¯ç¨å­ä½
# from matplotlib.font_manager import FontManager
# fm = FontManager()
# mat_fonts = set(f.name for f in fm.ttflist)
# print(mat_fonts)
# TODO ä¸é¢çä»£ç å¤§å®¶æå´è¶£å¯ä»¥èªå·±å»å°è¯çç©ä¸ä¸ï¼ä¸é¢ææ¯éç¹ðððððððððððð
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']





#Numpy random.poisson() æ³æ¾åå¸
#è¿åï¼ä»¥numpyæ°ç»å½¢å¼è¿åéæºæ ·æ¬
x = random.poisson(lam=2, size=10)

# ä¸ãæ³æ¾åå¸é®é¢ï¼
# åè®¾ææ¯å¤©æ¥å°éªæ°çµè¯çæ¬¡æ°æä»æ³æ¾åå¸ï¼å¹¶ä¸ç»ç»è®¡å¹³åæ¯å¤©æä¼æ¥å°20ä¸ªéªæ°çµè¯ã
# è¯·é®ï¼
# 1ãææå¤©æ¥å°15ä¸ªéªæ°çµè¯çæ¦çï¼
# 2ãææå¤©æ¥å°24ä¸ªéªæ°çµè¯ä»¥ä¸çæ¦çï¼åå«24ï¼ï¼
from scipy import stats

p = stats.poisson.pmf(15, 20)
print("æ¥å°15ä¸ªéªæ°çµè¯çæ¦çï¼", p)

p = stats.poisson.cdf(24, 20)
print("æ¥å°24ä¸ªéªæ°çµè¯ä»¥ä¸çæ¦çï¼", p)

from scipy import stats
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif'] = ['SimHei']  # ç¨æ¥æ­£å¸¸æ¾ç¤ºä¸­ææ ç­¾
plt.rcParams['axes.unicode_minus'] = False  # ç¨æ¥æ­£å¸¸æ¾ç¤ºè´å·

X = range(0, 51)
Y = []
for k in X:
    p = stats.poisson.pmf(k, 20)
    Y.append(p)

plt.bar(X, Y, color="red")
plt.xlabel("æ¬¡æ°")
plt.ylabel("æ¦ç")
plt.title("æ¥å°éªæ°çµè¯æ¬¡æ°åæ¦ç")
plt.show()