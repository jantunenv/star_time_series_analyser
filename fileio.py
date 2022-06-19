import numpy as np
def read_file(fname):
	time_series = np.loadtxt(fname, dtype=np.float64)
	return(time_series)
