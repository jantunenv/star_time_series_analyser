import pytest
import fileio
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

