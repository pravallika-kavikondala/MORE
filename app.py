"""
A simple  Movie Review flask app.
"""
from flask import Flask,render_template,request,redirect,url_for
from Model import Model
from presenter import Presenter
from google.cloud import translate

app = Flask(__name__)	#My Flask app
model = Model(app)
presenter = Presenter(model)

#Route that gives the landing page: Home Page for our Movie Review app
@app.route("/")
def home():
    return render_template(presenter.home())

#Route that provides Review view: Supports viewing all the movie reviews
@app.route("/review")
def review():
    data = presenter.review()
    return render_template(data[0],review=data[1])

#Route that provides Adding view: Supports a user to submit a movie review through a form
@app.route("/add", methods=['GET','POST'])
def add():
    if request.method=="GET":
        return render_template(presenter.getreview())
    if request.method == "POST":
        data = presenter.addreview(request.form['name'], request.form['year'], request.form['genre'], request.form['rating'], request.form['review'], request.form['reviewer'])
        return redirect(url_for(data))

#Route that provides Translation view: Supports a user to translate a movie review into another language through a drop-down 
@app.route("/translates", methods=['GET', 'POST'])
def translates():
    translate_client=translate.Client()
    langs=translate_client.get_languages()
    if request.method == "GET":
        return render_template('translates.html', languages=langs)
    if request.method == "POST":
        data=presenter.translated_review(request.form['reqlang'])
        return render_template(data[0], review=data[1], languages=langs)
        
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)