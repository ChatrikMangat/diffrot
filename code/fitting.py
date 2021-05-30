import numpy as np
import matplotlib.pyplot as plt

from skspatial.objects import Line
from skspatial.objects import Points
from skspatial.plotting import plot_3d

s = "dd2_s2_quasi.d"
dd2_x = np.loadtxt(s)

dd2_mb = dd2_x[:,9]
dd2_f = dd2_x[:,5]
dd2_j = dd2_x[:,3]

"""
dd2 = []
for i in range(len(dd2_mb)):
	dd2.append([dd2_mb[i],dd2_f[i],dd2_j[i]]) 
points = Points(dd2)
line_fit = Line.best_fit(points)
fig = plot_3d(line_fit.plotter(t_1=10, t_2=7, c='k'), points.plotter(c='b', depthshade=False))
plt.show(fig)
"""

#print(dd2_mb,dd2_j,dd2_f)

a1, b1, c1 = np.polyfit(dd2_j, dd2_f, 2)
print(a1,b1,c1)
a2, b2, c2 = np.polyfit(dd2_mb, dd2_j, 2)
print(a2,b2,c2)
a3, b3, c3 = np.polyfit(dd2_mb, dd2_f, 2)
print(a3,b3,c3)
a4, b4, c4 = np.polyfit(dd2_mb[:-1], dd2_f[:-1]/dd2_j[:-1], 2)
print(a4,b4,c4)

fig,ax = plt.subplots(1,4,figsize=(15,4))

x1 = np.linspace(min(dd2_j),max(dd2_j),50)
x2 = np.linspace(min(dd2_mb),max(dd2_mb),50)
x3 = np.linspace(min(dd2_mb),max(dd2_mb),50)
x4 = np.linspace(min(dd2_mb),max(dd2_mb),50)

ax[0].scatter(dd2_j,dd2_f)
ax[0].plot(x1,a1*x1**2+b1*x1+c1, color="red")
ax[1].scatter(dd2_mb,dd2_j)
ax[1].plot(x2,a2*x2**2+b2*x2+c2, color="red")
ax[2].scatter(dd2_mb,dd2_f)
ax[2].plot(x3,a3*x3**2+b3*x3+c3, color="red")
ax[3].scatter(dd2_mb[:-1],dd2_f[:-1]/dd2_j[:-1])
ax[3].plot(x4,a4*x4**2+b4*x4+c4, color="red")
plt.savefig(s[:-8])
plt.show()

