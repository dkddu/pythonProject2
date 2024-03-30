from die import Die
from plotly.graph_objs import Bar,layout
from plotly import offline
#创建实例
die_1 = Die(6)
die_2 = Die(6)
# die_3 = Die(6)
results = []
#掷骰子
for roll_number in range(5000000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
#答应投掷结果

#保存结果
frequencies =[]
max_result = die_1.num_face_size * die_2.num_face_size
frequencies = [results.count(value) for value in range(1,max_result+1)]
#数据
x_values = list(range(1,max_result+1))
data = [Bar(x=x_values,y=frequencies)]
#生成标题
x_axis_config = {'title':"consequence",'dtick':1}
y_axis_config = {"title":"frequency"}
my_layout = {
    'title': "the Result Of Rolling D6 * D6 50000 ",
    'xaxis': x_axis_config,
    'yaxis': y_axis_config
}
#生成直方图
offline.plot({'data':data,'layout':my_layout},filename='d6xd6.html')
#结果为正态分布