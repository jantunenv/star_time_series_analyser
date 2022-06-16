import numpy as np
import scipy.optimize
import fitter_routines

class Tsanalyser:
	frequencies = None
	amplitudes = None
	sinfit_params = None
	def __init__(self):
		frequencies = []
		amplitudes = []
		sinfit_params = []

	def fft(self, y, spacing):

		self.amplitudes = np.absolute(np.fft.fft(y))
		#We donẗ care about negative frequencies
		self.frequencies = [f for f in np.fft.fftfreq(len(y), d=spacing) if f > 0.0]
		self.amplitudes = self.amplitudes[:len(self.frequencies)]

	def get_dominant_frequency(self):
		bestfreq = np.nan
		bestamp = np.max(self.amplitudes)
		for i in range(len(self.frequencies)):
			if(self.amplitudes[i] == bestamp):
				bestfreq = self.frequencies[i]
				break
		return(bestfreq)
		
	def sinfit_function(self, t, A, w, p, c): return A*np.sin(w*t + p) + c
	
	def sinfit_bruteforce(self, x, y, guess = np.asarray([0.0, 0.0, 0.0, 0.0], dtype=np.float64), tol = np.asarray([1.0, 1.0, 1.0, 1.0], dtype=np.float64), n_vals = [20,20,20,20]):
		a, w, p, c = guess
		fitter_routines.fitter_routines.sin_fit_brute_force(x, y, len(x), a, w, p, c, tol[0], tol[1], tol[2], n_vals[0], n_vals[1], n_vals[2], n_vals[3])
		self.sinfit_params = [a, w, p, c]
		
	def sinfit(self, x,y, guess = [0.0, 0.0, 0.0, 0.0]):
		params, cov = scipy.optimize.curve_fit(self.sinfit_function, x, y, p0 = guess)
		self.sinfit_params = params

	def get_sinfit_f(self):
		return(self.sinfit_params[1]/(2*np.pi))
