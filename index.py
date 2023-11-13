import firebase_admin
from firebase_admin import credentials, firestore

firebase_admin.initialize_app(cred)
db = firestore.client()


from flask import Flask, render_template, request

from datetime import datetime, timezone, timedelta


app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>廖彥維的履歷</h1>"
    homepage += "<a href=/about>廖彥維簡介網頁</a><br>"
    homepage += "<a href=/holland>hollandcode結果</a><br>"
    homepage += "<a href=/work>工作結果</a><br>"
    return homepage


@app.route("/holland")
def holland():
    return render_template("hollandcode.html")
    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/work")
def work():
    return render_template("work.html")



#if __name__ == "__main__":
    #app.run()
    

