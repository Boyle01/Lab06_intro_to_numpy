"""Compute statistics on vocal previous vocal analysis."""

import numpy as np

#%% write down the data

# You may refer to your own data in a previous lab or the data in
# assets/data/processed.csv 

# TODO: in a numpy array, write down the max_rms for males
# TODO: in a numpy array, write down the max_rms for females
# TODO: in a numpy array, write down the max_cumu_freq for males
# TODO: in a numpy array, write down the max_cumu_freq for females

# Please name these python variables anything that makes sense to you.
# the RMS is referring to the amplitude of the audio waveform samples, which
# is similar to overall volume. The max_cumu_freq are peak frequencies based
# on which frequencies in the audio are loudest without any particular
# threshold set.

#%%
test = np.array([314,52,56,787])