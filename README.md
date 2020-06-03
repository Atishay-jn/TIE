# The Insurance experts

#### Summer Internship 2019. Made a flask web app for an insurance brokerage firm.

The app by default uses waitress for production envirnoment. 

## Respository structure

* static - Contains the js files and style sheets for the website.
* template - Contains 3 HTML files corresponding to the 3 pages the website has.
* a.json - Should contain information to link to a google sheet. Can be created at (https://console.developers.google.com/)
* run.py - Python script for the web application.
* requirements.txt - Contains all the project dependencies

## Features
* The website is lined to google sheet, which allows you to store any information filled on the website. The website has 2 forms, which write to the same google sheet.

* The website was hosted on AWS.

## Run

```bash
git clone https://github.com/Atishay-jn/TIE.git
cd TIE
python3 -m pip install -U pip
pip install requirements.txt
python3 run.py
```
The above assumes pip has been previously installed. Installation details: https://pip.pypa.io/en/stable/installing/

The app will run on port 80.

The installation might take a couple of minutes.
