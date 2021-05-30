import numpy as np
import matplotlib.pyplot as plt

pars = np.loadtxt("parameters.txt")

print(pars[3::4])

l = ['dd2_s0','dd2_s2','bhb_s0','bhb_s2']
x = [np.linspace(2.889849,3.6016294,50),
     np.linspace(2.794987,3.2786616,50),
     np.linspace(2.434994,3.0411717,50),
     np.linspace(2.392974,2.7737618,50)]
count = 0
for i in pars[3::4]:
	plt.plot(x[count],i[0]*x[count]**2+i[1]*x[count]+i[2],label=l[count])
	count=count+1
plt.legend()
plt.savefig("comb")
plt.show()

