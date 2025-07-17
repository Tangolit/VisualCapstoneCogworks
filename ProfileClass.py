

#goal: Create a Profile class with functionality to 
#store face descriptors associated with a named individual.
#abhyut 

class Profile:

    """Stoes face descriptors for a named individual."""

    def __init__(self,name):
        self.name=name 
        self.descriptors=dict()
    def add_descriptor(self,descriptor):
        """Adds a descriptor to the profile."""
        self.descriptor.append(descriptor)

