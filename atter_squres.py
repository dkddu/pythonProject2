import  matplotlib.pyplot as plt
import numpy as np
x_values = range(1,5001)
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig,ax = plt.subplots()
c = [(255/255,228/255,181/255)]
ax.scatter(x_values,y_values,s=10,cmap=plt.cm.Blues,c=y_values)
ax.set_title("square number",fontsize= 24)
ax.set_ylabel("square of the value",fontsize= 14)
ax.set_xlabel("value",fontsize= 14)
ax.tick_params(axis='both',which='major',labelsize= 14)
ax.axis([0,5100,0,5000**3+100000000000])
plt.show()