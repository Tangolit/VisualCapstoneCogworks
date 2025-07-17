#Rian

import matplotlib.pyplot as plt
from collections import Counter
#from database import FaceDatabase
import numpy as np
#from function import pairwise_cosine_distance
import os
print(os.listdir())
def cutoffs(database, name):
    """
        Takes the database and the name to find the cutoffs

        database: FaceDatabase
        Gets the profiles to find the descriptors people

        name: String
        Uses the name to find the descriptors used in the cosine distances

        Returns:
        cutoff: float
        The number for the person in the da
    """
    profile = database.getProfile()
    cosine_dists = []
    if name in profile:
        for i in range(profile[name]):
            for j in range(profile[name]):
                cosine_dist = pairwise_cosine_distance(profile[name][i], profile[name][j])
                cosine_dists.append(cosine_dist)
    
    count_cosine_dists = Counter(cosine_dists)
    return count_cosine_dists





        

