import numpy as np
import scipy.optimize

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
		
	def sinfit(self, x,y, guess = [0.0, 0.0, 0.0, 0.0]):
		params, cov = scipy.optimize.curve_fit(self.sinfit_function, x, y, p0 = guess)
		self.sinfit_params = params

	def get_sinfit_f(self):
		return(self.sinfit_params[1]/(2*np.pi))
