import numpy as np
import h5py
mev_to_erg = 1.60217733e-6
mev_to_gram = 1.7826627e-27
# 1 Mev/fm = mev_to_erg * 1d13 dyn
# 1 fm*fm = 1d-26 cm^2
# Pressure mev_to_erg*1.0d13/1.0d-26

hf = h5py.File('BHB_lpEOS_rho234_temp180_ye60_version_1.02_20140422.h5', 'r')

hm = h5py.File('eoscompose.h5', 'r')

gm = h5py.File('conv_bhblp.h5', 'w')

t1 = hf.get('logtemp')
r1 = hf.get('logrho')
y1 = hf.get('ye')
t1a = np.array(t1)
r1a = np.array(r1)
y1a = np.array(y1)
#print(t1a.shape,r1a.shape,y1a.shape)
#print(10**max(t1a),10**max(r1a),max(y1a))
#print(10**min(t1a),10**min(r1a),min(y1a))
x1 = hf.get('dedt')
x1a = np.array(x1)
print(x1a)

x2 = hm.get('Parameters/nb')
x2a = np.array(x2)
f2a = np.log10(x2a*1.66e15)
gm.create_dataset('logrho',data=f2a)
#print(x2,f2a)

x2 = hm.get('Parameters/t')
x2a = np.array(x2)
f2a = np.log10(x2a)
gm.create_dataset('logtemp',data=f2a)
#print(x2,f2a)

x2 = hm.get('Parameters/yq')
x2a = np.array(x2)
f2a = x2a
gm.create_dataset('ye',data=f2a)
#print(x2,f2a)

y2 = hm.get('Thermo_qty/index_thermo')
y2a = np.array(y2)
print(y2,y2a)
 
x2 = hm.get('Thermo_qty/thermo')
x2a = np.array(x2)
f2a = np.log10(x2a[1]/mev_to_gram*mev_to_erg)
gm.create_dataset('logenergy',data=f2a)
gm.create_dataset('energy_shift',data=np.zeros_like(f2a))
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo')
x2a = np.array(x2)
f2a = x2a[2]
gm.create_dataset('entropy',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo')
x2a = np.array(x2)
minp = 0
for i in x2a[3]:
	for j in i:
		for k in j:
			if k < minp:
				minp = k
print("Pressure Shift: ",minp*1.01)
f2a = np.log10((x2a[3]-minp*1.01)*mev_to_erg*1.0e13/1.0e-26)
gm.create_dataset('logpress',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo') # Doubt
x2a = np.array(x2)
f2a = x2a[4]
gm.create_dataset('mu_n',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo') # Doubt
x2a = np.array(x2)
f2a = x2a[4]
gm.create_dataset('mu_p',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo') # Doubt
x2a = np.array(x2)
f2a = x2a[7]*mev_to_erg*1.0e13/1.0e-26/1.66e15
gm.create_dataset('dpdrhoe',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo')
x2a = np.array(x2)
f2a = x2a[8]*1.0e13/1.0e-26*mev_to_gram
gm.create_dataset('dpderho',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo') # Doubt
x2a = np.array(x2)
f2a = x2a[9]
gm.create_dataset('cs2',data=f2a)
#print(x2,f2a)

x2 = hm.get('Thermo_qty/thermo') 
x2a = np.array(x2)
f2a = x2a[10]
gm.create_dataset('gamma',data=f2a)
#print(x2,f2a)

y2 = hm.get('Composition_pairs/index_yi')
y2a = np.array(y2)
#print(y2,y2a)

comps = ['X3he','XL','Xa','Xd','Xn','Xp','Xt']
for i in range(len(comps)):
	x2 = hm.get('Composition_pairs/yi')
	x2a = np.array(x2)
	f2a = x2a[i]
	gm.create_dataset(comps[i],data=f2a)
gm.create_dataset('X4li',data=np.zeros_like(f2a)) # Not in compose

y2 = hm.get('Composition_quadrupels/index_av')
y2a = np.array(y2)
#print(y2,y2a)

x2 = hm.get('Composition_quadrupels/aav')
x2a = np.array(x2)
f2a = x2a
gm.create_dataset('Abar',data=f2a)
#print(x2,f2a)

x2 = hm.get('Composition_quadrupels/zav')
x2a = np.array(x2)
f2a = x2a
gm.create_dataset('Zbar',data=f2a)
#print(x2,f2a)

x2 = hm.get('Micro_qty/micro') # Doubt
x2a = np.array(x2)
f2a = x2a * 939.56542052
gm.create_dataset('Meff',data=f2a)
#print(x2,f2a)

gm.create_dataset('pointsye',data=[60])
gm.create_dataset('pointstemp',data=[180])
gm.create_dataset('pointsrho',data=[234])
gm.create_dataset('timestamp',data=[20140422.36738426])

print("\n**GR1D Table**")
print(hf.keys())
print("\n**CompOSE Table**")
print(hm.keys())
for i in hm.keys():
	print(i)
	j = hm.get(i)
	print(np.array(j))
print("\n**Final Table**")
print(gm.keys())
