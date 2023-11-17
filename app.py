from flask import Flask, render_template, redirect, request
from cs50 import SQL
from helpers import apology

class Config:
    # Configure the database.
    DATABASE_URL = 'sqlite:///finance.db'

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///contact_info.db")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/testimonials")
def testimonials():
    return render_template("testimonials.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        goals = request.form["goals"]

        if not name:
            return apology("Must submit name")

        if not email:
            return apology("Must submit email")

        if not phone:
            return apology("Must submit phone number")

        if not goals:
            return apology("Must submit goals")

        db.execute("INSERT INTO people (name, email, phone, goals) VALUES(?, ?, ?, ?)", name, email, phone, goals)

        return redirect("/")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

if __name__ == "__main__":
    app.run(debug=True)