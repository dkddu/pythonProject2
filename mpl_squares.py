import matplotlib.pyplot as plt


# 设置默认字体为自定义字体
plt.rcParams['font.family'] = ['sans-serif']
squres = [1,4,9,16,25]
input_value = [1,2,3,4,5]
plt.style.use('seaborn')
fig ,ax = plt.subplots()
ax.plot(input_value,squres,linewidth=3)
#横纵坐标加上标签题目
ax.set_title("square number",fontsize= 24)
ax.set_ylabel("square of the value",fontsize= 14)
ax.set_xlabel("value",fontsize= 14)
ax.tick_params(axis='both',labelsize= 14)
plt.show()