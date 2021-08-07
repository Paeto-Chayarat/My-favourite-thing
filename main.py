from flask import Flask, render_template, request
from random import choice

web_site = Flask(__name__)


@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/myfav')
def myfav():
  return render_template('Myfav.html')

@web_site.route('/review')
def review():
  return render_template('review.html')



web_site.run(host='0.0.0.0', port=8080)