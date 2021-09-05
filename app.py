from flask import Flask
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello_world():

    return ("<p> <a href=http://localhost:5000/about-us name='About Us'>About Us</a> </p> "
            "<p> Hello World!</p>")


@app.route("/about-us")
def about_us():
    return ("<a href=http://localhost:5000/ name='Home'>Home</a>"
            "<p>About Us Page Coming Soon..</p>"
            f"<a href={escape(url_for('profile', name='Wipro'))} name='Home'>Wipro</a>")


@app.route("/show_profile/<name>")
def profile(name):
    return ("<a href=http://localhost:5000/ name='Home'>Home</a>"
            f"<p>Hi {escape(name)}</p>")


