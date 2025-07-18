#Rian

import matplotlib.pyplot as plt
from collections import Counter
from database import FaceDatabase
import numpy as np
from function import pairwise_cosine_distance

def cutoffs(database, name):
    """
        Takes the database and the name to find the cutoffs

        database: FaceDatabase
        Gets the profiles to find the descriptors people

        name: String
        Uses the name to find the descriptors used in the cosine distances

        Returns:
        cutoff: float
        The number for the person in the database


        for keys in profile:
        descriptor_list.append(profile[keys])
        for key in profile:
            if keys != key:
                descriptor_list_other = profile[key]
                for i in range(len(descriptor_list_other)):
                    for j in range(i + 1, len(descriptor_list_other)):
                        cosine_dist = pairwise_cosine_distance(descriptor_list, descriptor_list_other)
                        cosine_dists.append(cosine_dist)
    """
    profile = database.get_profiles()
    cosine_dists = []
    cosine_dists_same = []
    descriptor_list = []
    descriptor_list_full = []
    for key in profile:
        descriptor_list.append(profile[key])
        descriptor_list = descriptor_list[0]

        cosine_dist = pairwise_cosine_distance(descriptor_list, descriptor_list)
        cosine_dists_same.append(cosine_dist)

        descriptor_list = []
    
    for ind, key in enumerate(profile.keys()):
        if key == name:
            count_cosine_dists_same = Counter(np.array(cosine_dists_same[ind]).ravel())
        else:
            cosine_dists = (np.concatenate([np.array(cosine_dists_same[ind-1]), np.array(cosine_dists_same[ind-2])]))
            count_cosine_dists = Counter(cosine_dists.ravel())
    mean = np.array(cosine_dists_same).mean()
    std = np.array(cosine_dists_same).std()
    cutoff = mean - 0.64 * std
    return count_cosine_dists_same, count_cosine_dists
        
#test

database = FaceDatabase()

for j in range(10):
    rian = np.random.rand(512)
    database.add_image_descriptor("Rian", rian)
for j in range(10):
    rian = np.random.rand(512)
    database.add_image_descriptor("Akshith", rian)
for j in range(10):
    rian = np.random.rand(512)
    database.add_image_descriptor("Aditya", rian)

#counts = cutoffs(database, "Rian")
counts2 = cutoffs(database, "Akshith")
print(counts2)
plt.bar(counts2[1].keys(), counts2[1].values(), width= 0.00015)
plt.bar(counts2[0].keys(), counts2[0].values(), width= 0.00015)
plt.show()








        

