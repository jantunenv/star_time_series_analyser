import pytest
import fileio
import tsanalyser
import numpy as np

class TestIO:
	def test_read_file_1(self):
		fname = "data/sun.comb.dat"
		assert type(fileio.read_file(fname)) == np.ndarray

	def test_read_file_2(self):
		fname = "data/sun.comb.dat"
		assert len(fileio.read_file(fname)[0,:]) == 2

	def test_read_file_3(self):
		fname = "data/sun.comb.dat"
		assert len(fileio.read_file(fname)[:,0]) == 6258


class TestTsanalyser:
	def test_tsasalyer_has_frequencies(self):
		assert hasattr(tsanalyser.Tsanalyser, "frequencies")

	def test_tsasalyer_has_amplitudes(self):
		assert hasattr(tsanalyser.Tsanalyser, "amplitudes")

	def test_amplitudes_shape(self):
		spacing = 0.001
		freq = 10.0
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)
		analyser = tsanalyser.Tsanalyser()
		analyser.fft(y, spacing)
		assert len(analyser.amplitudes.shape) == 1

	def test_dominant_frequency(self):
		spacing = 0.001
		freq = 10.0
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)
		analyser = tsanalyser.Tsanalyser()
		analyser.fft(y, spacing)
		assert type(analyser.get_dominant_frequency()) == np.float64

	@pytest.mark.parametrize('freq', np.random.random(size=10)*100.0)
	def test_fourier_values(self, freq):
		spacing = 0.001
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)

		analyser = tsanalyser.Tsanalyser()
		analyser.fft(y, spacing)
		frequency = analyser.get_dominant_frequency()
		assert abs(frequency - freq) <= 0.05*freq

	@pytest.mark.parametrize('freq', np.random.random(size=10)*100.0)
	def test_sinfit_values(self, freq):
		spacing = 0.001
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)

		analyser = tsanalyser.Tsanalyser()
		#A, w, p ,c
		analyser.sinfit(x, y, [1.0, 2*np.pi*freq, 0.0, 0.0])
		frequency = analyser.get_sinfit_f()
		print(analyser.sinfit_params)
		print([1.0, 2*np.pi*freq*0.98, 0.0, 0.0])
		assert abs(frequency - freq) <= 0.01*freq
		
	@pytest.mark.parametrize('freq', np.random.random(size=2)*100.0)
	def test_bruteforce_sinfit_values(self, freq):
		spacing = 0.001
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)

		analyser = tsanalyser.Tsanalyser()
		#A, w, p ,c
		analyser.sinfit_bruteforce(x, y, [1.0, 2*np.pi*freq, 0.0, 0.0])
		frequency = analyser.get_sinfit_f()
		assert abs(frequency - freq) <= 0.01*freq
		
	@pytest.mark.parametrize('freq', np.random.random(size=2)*100.0)
	def test_bruteforce_sinfit_values_omp(self, freq):
		spacing = 0.001
		x = np.arange(0.0, 10.0, spacing)
		y = np.sin(x*2*np.pi*freq)

		analyser = tsanalyser.Tsanalyser()
		#A, w, p ,c
		analyser.sinfit_bruteforce(x, y, [1.0, 2*np.pi*freq, 0.0, 0.0], omp=True)
		frequency = analyser.get_sinfit_f()
		assert abs(frequency - freq) <= 0.01*freq
