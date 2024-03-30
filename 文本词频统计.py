import  jieba
from plotly.graph_objs import Bar,layout
from plotly import offline
#检查三国志中人物出场概率
#读取文本
with open("三国志.txt") as f:
    txt = f.read()
exclude = {"荆州","不能","太祖",'将军', '以为', '太守', '天下', '先主', '不能', '陛下', '大将军', '刺史','于是', '不可', '尚书', '所以', '不得', '司马', '天子', '元年',  '文帝', '汉中', '都尉', '三年', '百姓', '左右', '二年',
'校尉','遣使', '建安', '中郎将', '侍中', '太子', '春秋', '从事', '可以', '至于', '然后', '如此','不敢', '即位', '有所', '之后','军事','先帝', '大夫', '冀州', '都督', '诸葛','皇帝', '正月', '司空', '宣王', '五年' ,                                                                                                                                                                                                         '关内',
'魏书', '成都', '不足','明帝', '而已', '四年', '辽东','太尉', '今日', '前后', '国家', '夫人', '六年', '皇后', '洛阳','诸军', '妻子', '益州', '八月', '太后', '社稷', '所在', '将士',
'文王', '司徒', '长安', '不知','假节', '车骑', '十二月', '十月','足以', '不如', '英雄', '曹公'}
words = jieba.lcut(txt)
#创建字典储存
counts= {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "本初" or word == "本初曰":
        word = "袁绍"
    elif word =="仲谋" or word =="仲谋曰":
        word = "孙权"
    elif word == "孔明曰" or word == "诸葛亮":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    elif word == "子龙" or word == "子龙曰":
        word = "赵云"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) +1
for word in exclude:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
frequencies =[]
x_values = []
for i in range(10):
    word,count = items[i]
    frequencies.append(count)
    x_values.append(word)
    # print("{0:<10}{1:>5}".format(word,count))
print(x_values)
# frequencies =[]
# max_result = die_1.num_face_size * die_2.num_face_size
# frequencies = [results.count(value) for value in range(1,max_result+1)]
# #数据
data = [Bar(x=x_values,y=frequencies)]
#生成标题
x_axis_config = {'title':"consequence",'dtick':1}
y_axis_config = {"title":"frequency"}
my_layout = {
    'title': "the Result Of three nations ",
    'xaxis': x_axis_config,
    'yaxis': y_axis_config
}
#生成直方图
offline.plot({'data':data,'layout':my_layout},filename='三国.html')

