def cutoffs(database, name):
    """
        Takes the database and the name to find the cutoffs

        database: FaceDatabase
        Gets the profiles to find the descriptors people
    """
    if name in database.getProfile():

