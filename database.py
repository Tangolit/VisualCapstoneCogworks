"""
Functionality to create, load, and save a database of profiles, add function to return profile
Functionality to add and remove profiles 
Functionality to add an image to the database, given a name (create a new profile if the name isn’t in the database, otherwise add the image’s face descriptor vector to the proper profile)
Akshith
"""

import pickle
import torch

class FaceDatabase:
    def __init__(self):
        self.profiles = {}

    def add_profile(self, name):
        if name not in self.profiles:
            self.profiles[name] = []

    def remove_profile(self, name):
        if name in self.profiles:
            del self.profiles[name]

    def add_image_descriptor(self, name, descriptor):
        if name not in self.profiles:
            self.profiles[name] = []
        self.profiles[name].append(descriptor)

    def save(self, path):

        with open(path, "wb") as f:
            pickle.dump(self.profiles, f)
        print(f"database saved to '{path}")
    
    def load(self, path):
        with open(path, "rb") as f:
            self.profiles = pickle.load(f)
        print(f"database loaded from '{path}")

    def get_profiles(self):
        return self.profiles


