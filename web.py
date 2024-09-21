
import flask
app = flask.Flask(__name__)

@app.route("/")
def homepage():
    return flask.render_template("index.html")



app.run(host="127.0.0.1" , port= 5000)