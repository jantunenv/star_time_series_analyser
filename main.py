import fileio
import tsanalyser
import matplotlib.pyplot as plt
import numpy as np

def main():
	fname = "data/sun.comb.dat"
	data = fileio.read_file(fname)


	#interpolation for manipulating fft binning 
	spacing = 1.0
	x = np.arange(data[0,0], data[-1,0], spacing)
	y = np.interp(x, data[:,0], data[:,1])

	analyser = tsanalyser.Tsanalyser()
	analyser.fft(y, spacing)

	fig, ax = plt.subplots(2,1)

	print(1/analyser.get_dominant_frequency())

	ax[0].plot(x, y)
	ax[1].plot(analyser.frequencies[0:100], analyser.amplitudes[0:100],'.')

	plt.show()


main()
