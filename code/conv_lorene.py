import numpy as np

mev_to_erg = 1.60217733e-6
mev_to_gram = 1.7826627e-27
# 1 Mev/fm = mev_to_erg * 1d13 dyn
# 1 fm*fm = 1d-26 cm^2
# Pressure mev_to_erg*1.0d13/1.0d-26


x = np.loadtxt("eos.table")

s = "frb_t0"
fp = open(s+".d","w")

print(x.shape)
fp.write("#\n#\n#\n#\n#\n")
fp.write(str(x.shape[0])+"\n")
fp.write("#\n#\n#\n")

for i in x:
	fp.write(str(i[1])+"\t"+str(i[4]*mev_to_gram/1.0e-39)+"\t"+str(i[3]*mev_to_erg*1.0e13/1.0e-26)+"\n")
