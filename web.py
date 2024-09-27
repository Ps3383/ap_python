
import flask
app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/newbook")
def newbook():
    return flask.render_template("newbook.html")

@app.route("/bookslist")
def bookslist():
    return flask.render_template("bookslist.html")

@app.route("/deletebook")
def deletebook():
    return flask.render_template("deletebook.html")



app.run(host="127.0.0.1" , port= 5000)