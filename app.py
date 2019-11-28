from flask import Flask, request, render_template
from CustomUser import *
from main import *

app = Flask(__name__)
@app.route('/')

def my_form():
    return render_template('home.html')

@app.route('/', methods=['POST'])
def my_form_post():
	username = request.form['user']
	rating = request.form.getlist('rating')
	movie = request.form.getlist('movie')
	userRating = {}
	movieRating = {}
	for ind, m in enumerate(movie):
		if rating[ind]:
			movieRating[m] = int(rating[ind])
	userRating[username] = movieRating
	for usr in userRating:
		print(usr)
	user = username
	newUser = CustomUser(user, movieRating)
	print(newUser)
	
	movieList = getMovieList(newUser)
	for x in movieList:
		print(x[0] + ": " + str(x[1]))
	return render_template('output.html', name = username, movieRating = movieList)