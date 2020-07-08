#!/usr/bin/python3

from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import url_for
from flask import escape
from flask import request
import datetime
from langdetect import detect

app = Flask(__name__)
app.secret_key = "any random string"

## If the user hits the root of our API
@app.route("/")
def index():
  ## if the key "username" has a value in session
  if "username" in session:
    username = session["username"]
    time = session["time"]
    language = session["language"]
    return "Logged in as " + username + " at " + time + " your language is " + language + "<br>" + \
      "<b><a href = '/logout'>click here to log out</a></b>"

  ## if the key "username" does not have a value in session
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"

## If the user hits /login with a GET or POST
@app.route("/login", methods = ["GET", "POST"])
def login():
   ## if you sent us a POST because you clicked the login button
   if request.method == "POST":

      ## request.form["xyzkey"]: use indexing if you know the key exists
      ## request.form.get("xyzkey"): use get if the key might not exist
      session["username"] = request.form.get("username")
      session["time"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      lang = request.form.get("words")
      #session["language"] = detect(lang)
      session["language"] = detect("this is a short test string because when I pass in the variable lang above it doesn't work")
      return redirect(url_for("index"))

   ## return this HTML data if you send us a GET
#    return render_template("session-login.html")
   return """ 
   <form action = "" method = "post">
      <p><input type = text name = username placeholder = username></p>
      <p><input type = text placeholder = "type a short phrase" language = words></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
   # remove the username from the session if it is there
   session.pop("username", None)
   return redirect(url_for("index"))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=2224)
