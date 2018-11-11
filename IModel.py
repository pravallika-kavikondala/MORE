from abc import ABCMeta, abstractmethod

class IModel:
    __metaclass__=ABCMeta
    
    def fetchall(self, databaseName):
        """
        Gets all Moviereview datastore entries along with the sentiment analysis performed on the comments
        """
        pass
        
    def addreview(self, name, year, genre, rating, review, reviewer):
        """
        Inserts a movie review into Moviereview datastore together with sentiment analysis performed on the comments  
        """
        pass
        
    def fetchTranslation(self, language):
        """
        Gets all Moviereviews translated into choosen language
        """
        pass     