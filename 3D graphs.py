import matplotlib.pyplot as plt

plt.figure(figsize = (8,8))

ax = plt.axes(projection = '3d')

x = [1,2,3,4,5]

y = [2,4,6,8,10]

z = [1,3,5,7,9]

ax.plot(x,y,z,marker = 'o',linestyle = "--",color = "blue")


ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_zlabel("Z label")

ax.set_title("3D line plot")

plt.show()




