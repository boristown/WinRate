import numpy as np

def scale_to_0_1(lst):
    ndarray = np.array(lst)
    scaled = np.interp(ndarray, (ndarray.min(), ndarray.max()), (0, 1))
    return scaled.tolist()