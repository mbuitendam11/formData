from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import relationship
from typing import List

app = Flask(__name__)
app.config['SECRET_KEY'] = "os.environ.get('FLASK_KEY')"
Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def index():

    return render_template("form.html")

@app.route("/failed", methods=["GET", "POST"])
def failed():
    return "<p>This didnt work</p>"

@app.route("/submit", methods=["GET", "POST"])
def submit():
    return "<p>Submitted</p>"
    '''if request.method == "POST":
        
        # Need to somehow GET information 

        try: # Succeed
            return url_for("index")
        except: # Failed
            print("Something went wrong!")
            return url_for("failed")'''


if __name__ == "__main__":
    app.run(debug=True)