import  matplotlib.pyplot as plt
from  andom_walk import RandomWalik
scale = 255
while True:
    rw = RandomWalik(50000)
    rw.fill_walk()

    plt.style.use('classic')
    fig ,ax = plt.subplots(figsize=(15,9))
    point_number = range(rw.number_points)
    ax.scatter(rw.x_values,rw.y_values,s=1,cmap=plt.cm.Blues,edgecolor="none",c=point_number)
    #突出起点和终点
    ax.scatter(0,0,color=(118/scale,238/scale,198/scale),edgecolor="none",s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],color=(255/scale,106/scale,106/scale),edgecolor="none",s=100)
    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)
    # ax.plot(rw.x_values,rw.y_values,linewidth=1)
    plt.show()

    keep_running = input("Make another running?(y/n）: ")
    if keep_running == "n":
        break