import numpy as np
def read_file(fname):
	time_series = np.loadtxt(fname)
	return(time_series)
