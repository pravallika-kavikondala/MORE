from flask import session,request

class Presenter:

    def __init__(self,model):
        """
        Initializing model
        Returns nothing
        """
        self.model=model
        
    def home(self):
    	"""
    	Presents user with HTML page containing 2 links to view or add a movie review
    	"""
        return 'home.html'
        
    def review(self):
        """
        Presents user with HTML page to view all the movie reviews
        """
        data = self.model.fetchall()
        return ('review.html', data)
        
    def getreview(self):
        """
        Presents user with HTML form to submit a movie review
        """
        return 'add.html'
        
    def addreview(self, name, year, genre, rating, review, reviewer):
        """
        Function definition for adding a review
        """
        self.model.addreview(name, year, genre, rating, review, reviewer)
        return 'home'
        
    def translated_review(self, reqlang):
        """
        Presents user with a drop down to select a specific language to translate all the reviews
        """
        langs=self.model.fetchtranslation(reqlang)
        return('translates.html', langs)