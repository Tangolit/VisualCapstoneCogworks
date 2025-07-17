# Function to measure cosine distance between face descriptors. 
# It is useful to be able to take in a shape-(M, D) array of M descriptor vectors and a shape-(N, D) array of N descriptor vectors
# and compute a shape-(M, N) array of cosine distances – this holds all MxN combinations of pairwise cosine distances.
# Cynthia

import numpy as np

def pairwise_cosine_distance(M_descriptor, N_descriptor):
    """
    M_descriptor (np.ndarray): shape (M,D)
    N_descriptor (np.ndarray): shape (N,D)

    return : np.ndarray with shape (M, N)
    """
    #Normalize the vectors
    normed_M = M_descriptor / np.linalg.norm(M_descriptor, axis = 1, keepdims = True)
    normed_N = N_descriptor / np.linalg.norm(N_descriptor, axis = 1, keepdims = True)

    #Calculating dot product of normalized vectors
    cos_similarity = normed_M @ normed_N.T

    #Cosine Distance formula 
    cos_distance = 1 - cos_similarity

    return cos_distance


