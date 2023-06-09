from wordcloud import WordCloud
import jieba

import pandas as pd
df = pd.read_csv("高考.csv",)
myfont = myfont = r'C:\Windows\Fonts\simhei.ttf'

with open("hit_stopwords.txt", "r", encoding='utf8') as f:
    stopword_list = f.readlines()
stopword_list = [i.strip() for i in stopword_list]
stopword_list.extend(['微博','高考','月','日','还'])
w = WordCloud(font_path=myfont,stopwords=stopword_list,max_words=200)
text = ''
for i in df['text']:
    text += i
data_cut = ' '.join(jieba.lcut(text))
w.generate(data_cut)
image = w.to_file('词云图.png')
