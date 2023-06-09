import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

font = {'family' : 'SimSun',
        'size'  : '12'}

plt.rc('font', **font)

df = pd.read_csv("高考.csv",)

from snownlp import SnowNLP
df['emotion'] = df['text'].apply(lambda x: SnowNLP(x).sentiments)
bins = np.arange(0, 1.1, 0.1)
plt.hist(df['emotion'], bins, color = '#4F94CD', alpha=0.9)
plt.xlim(0, 1)
plt.xlabel('情感分')
plt.ylabel('数量')
plt.title('情感分直方图')
plt.savefig("情感分直方图.png",dpi=300)
plt.show()
