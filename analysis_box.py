from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

font = {'family' : 'SimSun',
        'size'  : '12'}

plt.rc('font', **font)

df = pd.read_csv("高考.csv",)

df2 = df[df['like_count'] < 1000]
df_like = df2['like_count'].values.tolist()
plt.figure(figsize=(14,6))
plt.boxplot(df_like, labels=["点赞分析"])
plt.ylabel("数量")
plt.title("点赞数-箱线图")
plt.savefig("点赞数-箱线图.png",dpi=300)
plt.show()
plt.close()