import matplotlib.pyplot as plt

plt.figure(figsize = (12,7))

ax = plt.axes(projection = '3d')

x = [11,22,33,44,55]
y = [200,400,60,800,10000]
z = [13,33,55,77,99]
ax.plot(x,y,z,marker = 'o',linestyle = "--",color = "red")

x = [50,55,60,65,70]
y = [205,405,650,890,9500]
z = [13,33,55,77,99]
ax.plot(x,y,z,marker = 'o',linestyle = "--",color = "blue")

x = [110,220,330,440,550]
y = [200,400,600,800,1000]
z = [130,330,550,770,990]
ax.plot(x,y,z,marker = 'o',linestyle = "--",color = "purple")

plt.show()
