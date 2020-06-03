import functools
import json
import os
import flask
from flask import Flask, redirect, url_for, session, request,render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('a.json', scope)

gc = gspread.authorize(credentials)
wks = gc.open("Insurance Experts Info").sheet1
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/home")
def home_page():
	return render_template("index.html")

@app.route("/home", methods=["POST"])
def quick_info():
	text = ['1']*4
	text[0] = "Quick Info"
	text[1] = request.form['Email']
	text[2] = request.form['Location']
	text[3] = request.form['Type']
	print(text)
	wks.insert_row(text)
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")
@app.route("/contact", methods=["POST"])
def form():
	text = ['1']*6
	text[0] = "Contact Us"
	text[1] = request.form['Fname']
	text[2] = request.form['Lname']
	text[3] = request.form['Email']
	text[4] = request.form['Subject']
	text[5] = request.form['Message']
	print(text)
	wks.insert_row(text)
	return render_template("contact.html")

if __name__ == "__main__":
	from waitress import serve
	serve(app, host="0.0.0.0", port=80)