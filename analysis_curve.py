from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

font = {'family' : 'SimSun',
        'size'  : '12'}

plt.rc('font', **font)

df = pd.read_csv("高考.csv",)
print(df.head())
print(df.shape)

print(df.columns)
df["time_2"] = pd.to_datetime(df["publish_time"])
df["day"] = df["time_2"].dt.hour
df_cmt_date = df["day"].value_counts()
df_cmt_date = df_cmt_date.reset_index()
df_cmt_date.columns = ["时间", "评论数量"]
df_cmt_date = df_cmt_date.sort_values(by = "时间",axis = 0,ascending = True)
df_cmt_date = df_cmt_date.reset_index(drop=True)
plt.bar(df_cmt_date["时间"], df_cmt_date["评论数量"])
plt.title("评论数量统计（按发帖时间）-条形图")
plt.savefig("评论数量统计（按发帖时间）-条形图.png",dpi=300)
plt.show()
plt.close()