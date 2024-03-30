#GovRptWordCloudv2.py
import jieba
import wordcloud
from imageio.v2 import imread
mask = imread("E:/下载/5-star-icon-31.png")
f = open("E:/下载/新时代中国特色社会主义.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path = "msyh.ttc", mask = mask,width = 1000, height = 700, background_color = "white")
w.generate(txt)
w.to_file("E:/下载/g.png")