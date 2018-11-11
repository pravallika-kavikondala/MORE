from model_datastore import from_datastore, getreview, insert, gettranslation
from IModel import IModel

class Model(IModel):
    def __init__(self, app):
        self.arg=app

    def fetchall(self):
        """
        Gets all tuples from the Moviereviews datastore
        :return: all the tuples containing name, year, genre, rating, review, reviewer details of a movie from moviereviews table
        """
        return getreview()

    def addreview(self, name, year, genre, rating, review, reviewer):
        """
        Inserts entry into Moviereviews datastore 
        :param name: String
        :param year: String
        :param genre: String
		:param rating: String
		:param review: String
		:param reviewer: String
        :return: none
        """
        insert(name, year, genre, rating, review, reviewer)

    def fetchtranslation(self, language):
        """
        Gets all tuples from the Moviereviews datastore and translates them into an other language
        :return: all the tuples containing name, year, genre, rating, review, reviewer details of a movie from moviereviews table
        """
        return gettranslation(language)
