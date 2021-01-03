import matplotlib.pyplot as plt
import numpy as np
import math

# Get Data
seqdata = np.loadtxt("seq.d")
seqcopy = seqdata.copy()
print(seqdata.shape)
rotdata = np.loadtxt("kepp.d")
rotcopy = rotdata.copy()
print(seqdata.shape)
stadata = np.loadtxt("static.d")
stacopy = stadata.copy()
print(stadata.shape)
#kepdata = np.loadtxt("ermehgerd.d")
#kepcopy = kepdata.copy()
#print(kepdata.shape)
pj = 0
pt = 0
# Convert to log scale
for j in seqcopy:
	j[12] = math.log(j[12])
for j in rotcopy:
	j[12] = math.log(j[12])
for j in stacopy:
	j[12] = math.log(j[12])
#for j in kepcopy:
#	j[12] = math.log(j[12])

fig, ax = plt.subplots(2, 2, figsize=(16,16))
# Mass vs log(rho_c)
ax[0][0].plot(seqcopy[:,12],seqcopy[:,4],color='red')
ax[0][0].plot(rotcopy[:,12],rotcopy[:,4],color='orange')
ax[0][0].plot(stacopy[:,12],stacopy[:,4],color='black')
#ax[0][0].plot(kepcopy[:,12],kepcopy[:,4],color='blue')
# Freq vs log(rho_c)
ax[0][1].plot(seqcopy[:,12],seqcopy[:,5],color='red')
ax[0][1].plot(rotcopy[:,12],rotcopy[:,5],color='orange')
ax[0][1].plot(stacopy[:,12],stacopy[:,5],color='black')
#ax[0][1].plot(kepcopy[:,12],kepcopy[:,5],color='blue')
# Freq vs J/Mb2
#ax[1][0].plot(seqcopy[:,3]/seqcopy[:,9]/seqcopy[:,9],seqcopy[:,5],color='red')
#ax[1][0].plot(rotcopy[:,3]/rotcopy[:,9]/rotcopy[:,9],rotcopy[:,5],color='orange')
#ax[1][0].plot(stacopy[:,3]/stacopy[:,9]/stacopy[:,9],stacopy[:,5],color='black')
#ax[1][0].plot(kepcopy[:,3]/kepcopy[:,9]/kepcopy[:,9],kepcopy[:,5],color='blue')
# Freq vs J 
ax[1][0].plot(seqcopy[:,3],seqcopy[:,5],color='red')
ax[1][0].plot(rotcopy[:,3],rotcopy[:,5],color='orange')
ax[1][0].plot(stacopy[:,3],stacopy[:,5],color='black')
#ax[1][0].plot(kepcopy[:,3],kepcopy[:,5],color='blue')
# Freq vs T/W
ax[1][1].plot(seqcopy[:,8],seqcopy[:,5],color='red')
ax[1][1].plot(rotcopy[:,8],rotcopy[:,5],color='orange')
ax[1][1].plot(stacopy[:,8],stacopy[:,5],color='black')
#ax[1][1].plot(kepcopy[:,8],kepcopy[:,5],color='blue')
# Labels
ax[0][0].set(xlabel='log(rho_c)', ylabel='Mg/Msol')
ax[0][1].set(xlabel='log(rho_c)', ylabel='Freq')
ax[1][0].set(xlabel='J', ylabel='Freq')
ax[1][1].set(xlabel='T/W', ylabel='Freq')
plt.savefig("currplot.png")
plt.show()
