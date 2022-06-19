import fileio
import tsanalyser
import fitter_routines
import matplotlib.pyplot as plt
import numpy as np

def main():
	fname = "data/sun.comb.dat"
	data = fileio.read_file(fname)

	#interpolation for manipulating fft binning 
	spacing = 1.0
	x = np.arange(data[0,0], data[-1,0], spacing, dtype=np.float64)
	y = np.interp(x, data[:,0], data[:,1])

	A = np.array((np.max(y) - np.min(y))*0.5, dtype=np.float64)
	w = np.array(1/(3600.0/(2.0*np.pi)), dtype=np.float64)
	p = np.array(np.pi, np.float64)
	c = np.array(np.mean(y), np.float64)

	print(A, w, p, c)

	yfit = A*np.sin(w*x + p) + c

	analyser = tsanalyser.Tsanalyser()
	analyser.sinfit_bruteforce(x, y, guess=[A, w, p, c],
				tol=np.asarray([0.5*A, 0.2*w, np.pi, 0.0]), n_vals = [10, 100, 10, 1], omp=True)


	#print(fitter_routines.fitter_routines.__doc__)
	params = analyser.sinfit_params

	yfit2 = params[0]*np.sin(params[1]*x + params[2]) + params[3]

	plt.plot(x, y)
	plt.plot(x, yfit, 'b-')
	plt.plot(x, yfit2, 'g-')

	plt.show()


main()
