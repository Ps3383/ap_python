from book_app import Book
import flask
import books_sqlite
app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template("index.html")

@app.route("/about")
def about():
    return flask.render_template("about.html")

@app.route("/newbook" , methods=["POST" ,"GET"])
def newbook():
    if flask.request.method=="POST":
        try:    
            data  = flask.request.form
            isbn  = int(data["isbn"])
            title = data["title"]
            author = data["author"]
            pages = int(data["pages"])
            price = float(data["price"])
        except(ValueError):
            return flask.render_template("error.html")

        try:
            Book(isbn,title,author,price,pages)
        except:
            return flask.render_template("error.html")
        return flask.redirect("/")

    return flask.render_template("newbook.html")

@app.route("/bookslist")
def bookslist():
    all= Book.list_of_books()
    return flask.render_template("bookslist.html" , allbooks=all)

@app.route("/deletebook", methods=["POST" , "GET"])
def deletebook():
    if flask.request.method=="POST":
        try:  
            data = flask.request.form
            isbn = int(data["isbn"])
            Book.delete_book(isbn)
            return flask.redirect("/bookslist")
        except(books_sqlite.BookNotFound):
            return flask.render_template("booknotfound.html")
        except:
            return flask.render_template("error.html")

    return flask.render_template("deletebook.html")


@app.route("/findbook", methods=["POST" , "GET"])
def find_book():
    if flask.request.method=="POST":
       try:  
            data  = flask.request.form
            isbn  = int(data["isbn"])    
            abook = (Book.find_book(isbn))
            return flask.render_template("findbook.html",mybook=abook)
       except(books_sqlite.BookNotFound):
            return flask.render_template("booknotfound.html")
       except:
            return flask.render_template("error.html")

    return flask.render_template("findbook.html")


app.run(host="127.0.0.1" , port= 5000)