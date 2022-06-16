import numpy as np

class Tsanalyser:
	frequencies = None
	amplitudes = None
	def __init__(self):
		frequencies = []
		amplitudes = []
		
	def fft(self, y, spacing):
		self.amplitudes = np.absolute(np.fft.fft(y))
		#We donẗ care about negative frequencies
		self.frequencies = [f for f in np.fft.fftfreq(len(y), d=spacing) if f>= 0.0]
		self.amplitudes = self.amplitudes[:len(self.frequencies)]
		
	def get_dominant_frequency(self):
		bestfreq = np.nan
		bestamp = np.max(self.amplitudes)
		for i in range(len(self.frequencies)):
			if(self.amplitudes[i] == bestamp):
				bestfreq = self.frequencies[i]
				break
		return(bestfreq)

#fft_data = np.fft.fft(sample)
#fft_freqs = np.fft.fftfreq(len(sample), d=1/f_rate)
