from google.cloud import datastore
from google.cloud import translate
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
 
# [START from_datastore]
def from_datastore(rev):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    return:
        dictionary containing movie reviews
    """
    if not rev:
        return None
    if isinstance(rev, list):
        rev = rev.pop()
    moviereview = {}
    moviereview['name'] = rev['name']
    moviereview['year'] = rev['year']
    moviereview['genre'] = rev['genre']
    moviereview['rating'] = rev['rating']
    moviereview['review'] = rev['review']
    moviereview['reviewer'] = rev['reviewer']
    moviereview['sentiment'] = rev['sentiment']
    sentiment = float(moviereview['sentiment'])
    if sentiment>=-1 and sentiment <-0.5:
    	moviereview['decision'] = "Awful"
    if sentiment>=-0.5 and sentiment <0.0:
    	moviereview['decision'] = "Bad"
    if sentiment==0.0:
    	moviereview['decision'] = "Cannot make a decision for this review"
    if sentiment>0.0 and sentiment <=0.4:
    	moviereview['decision'] = "ok!!"
    if sentiment>0.4 and sentiment <=0.8:
    	moviereview['decision'] = "Very Good"
    if sentiment>0.8 and sentiment <=1:
    	moviereview['decision'] = "Masterpiece"
    return moviereview
# [END from_datastore]


# [START getreview]
def getreview():
    """
    Takes all the rows of datastore and returns a list of all the movie reviews
    :return: all the rows containing name, year, genre, rating, review, reviewer, sentiment score and also the decision made from the sentiment score details of a movie from Moviereview datastore
    """
    ds=datastore.Client('pravallika-kavikondala')
    query=ds.query(kind='Moviereview')
    rev=list(map(from_datastore,query.fetch()))
    return rev
# [END getreview]


# [START insert]
def insert(name, year, genre, rating, review, reviewer):
    """
    Inserts user entered movie review entry into the Moviereview datastore
    :param name: String
    :param year: String
    :param genre: String
	:param rating: String
	:param review: String
	:param reviewer: String
    :return: none
    """
    ds=datastore.Client('pravallika-kavikondala')
    key=ds.key('Moviereview')
    entity=datastore.Entity(key=key)
    moviereview={}
    moviereview['name']=name
    moviereview['year']=year
    moviereview['genre']=genre
    moviereview['rating']=rating
    moviereview['review']=review
    moviereview['reviewer']=reviewer
    client=language.LanguageServiceClient()
    document=types.Document(content=review,type=enums.Document.Type.PLAIN_TEXT)
    score=client.analyze_sentiment(document=document).document_sentiment.score
    moviereview['sentiment']=score
    entity.update(moviereview)
    ds.put(entity)
# [END insert]

def gettranslation(lang):
    """
    Takes all the rows of datastore and returns a list of all the translated movie reviews
    :return: all the rows containing name, year, genre, rating, review, reviewer, and the sentiment score of the translated langugae
    """
    query=datastore.Client('pravallika-kavikondala').query(kind='Moviereview')
    all_translations = list()
    for rev in query.fetch():
        if isinstance(rev, list):
            rev = rev.pop()
        client = translate.Client()
        tr_review = {}
        tr_review['name'] = client.translate(rev['name'],target_language=lang)['translatedText']
        tr_review['year'] = rev['year']
        tr_review['genre'] = client.translate(rev['genre'],target_language=lang)['translatedText']
        tr_review['rating'] = client.translate(str(rev['rating']),target_language=lang)['translatedText']
        tr_review['review'] = client.translate(rev['review'],target_language=lang)['translatedText']
        tr_review['reviewer'] = client.translate(rev['reviewer'],target_language=lang)['translatedText']
        tr_review['sentiment'] = rev['sentiment']
        all_translations.append(tr_review)
    return all_translations