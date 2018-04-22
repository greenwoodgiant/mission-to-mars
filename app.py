from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = scrape_mars.scrape()
    return render_template("index.html", mars_data=mars_data)


@app.route("/scrape")
def scrape():
    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)