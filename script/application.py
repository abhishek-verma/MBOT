#<!--{{ url_for('static', filename=image_links[0][0]) }}-->
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import meme_scrapping, api
from api import app, mysql
import json
import requests
import urllib.request


#app = Flask(__name__)

@app.route("/scrape")
def scrape_memes():
    memes = meme_scrapping.scrape()
    return("Something to be displayed")

@app.route("/", methods = ['POST', 'GET'])
def home():
    #local_url = 'images/nba-finals-game-t-cavaliers-vs-warriors-tonight-at-9-5596587.png'
    req = 'http://127.0.0.1:5000/api/memes/all'
    r = requests.get(url= req)
    meme_data = json.loads(r.content.decode('utf-8'))
    '''if request.method == 'POST':
        selectedValues = request.form['textbox']
        print(selectedValues)
        return (selectedValues)'''
    return render_template('home_page.html', **locals())


if __name__ == "__main__":
    app.run(debug=True)
