from flask import Flask, request, render_template, flash
from markupsafe import Markup
#from django.shortcuts import render

import os
import json

app = Flask(__name__)

@app.route("/")
def render_home():
    countries = get_nations()
    #funfact0 = get_index(state)
    return render_template("home.html")

@app.route("/pagetwo")
def render_fragile():
    countries = get_nations()
    country = request.args.get('state')
    
    return render_template("Fragility-By-State.html", state_options=countries)
@app.route("/pagethree")
def render_matt():
    countries1=get_nations()
    yearopt=get_year()
    return render_template("page3.html", state_options=countries1, year_options=yearopt)
@app.route("/pagefour")
def render_four():
    countries = get_year()
    
    return render_template("page4.html", year_options=countries)
@app.route("/pagetwoAnswers")
def render_answers():
    countries = get_nations()
    
    option1=request.args.get("state")
    print(option1)
    country=get_index(option1)
    return render_template("Fragility-By-State.html", state_options=countries, funfact1= option1 + "'s " + "Fragility Index in 1996 was " + str(country))
@app.route("/pagethreeAnswers")
def render_page2answers():
    countries1=get_nations()
    yearopt=get_year()
    option1=request.args.get("matthew")
    option2=request.args.get("year")
    indexyeah=get_sebas(option1, option2)
    return render_template("page3.html", state_options=countries1, year_options=yearopt, funfact4= option1+" 's Fragility Index in "+option2+" was "+ str(indexyeah) )
@app.route("/pagefourAnswers")
def render_lorenzo():
    option1=request.args.get("nikita")
    zaydenf=get_greatest(option1)
    amber=get_lowest(option1)
    fleming=get_highc(option1)
    toiletrius=get_average(option1)
    fabio="The Country With the Highest Fragility Index in" + str(option1) + " was "+ fleming + " at " + str(zaydenf)
    amberf="The Country With the Lowest Fragility Index in" + str(option1) + " had an index " + str(amber)
    toiletskib="The Average Index in " + str(option1) + " was " + str(toiletrius)
    countries = get_year()
    return render_template("page4.html", year_options=countries, funfact7=fabio, funfact8=amberf, funfact9=toiletskib)
    

    
    return render_template("page4.html", state_options=countries, molwane=jaden)
def get_year():
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    years=[]
    for c in nations:
        if c["Year"] not in years:
            years.append(c["Year"])
    options=""
    for s in years:
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
def get_nations():
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    countries=[]
    for c in nations:
        if c["Country"] not in countries:
            countries.append(c["Country"])
    options=""
    for s in countries:
        options += Markup("<option value=\"" + str(s) + "\">" + str(s) + "</option>") #Use Markup so <, >, " are not escaped lt, gt, etc.
    return options
def get_sebas(country, year):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    for c in nations:
        if str(c["Year"])==year and c["Country"]==country:
            return c["Metrics"]["State Fragility Index"]
def get_index(country):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    for c in nations:
        if c["Year"]==1996 and c["Country"]==country:
            return c["Metrics"]["State Fragility Index"]
def get_emiliano(country):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    options=[]
    emilianosyear=1996
    for c in nations:
        if c["Year"]==emilianosyear and c["Country"]==country:
            options.append(c["Metrics"]["State Fragility Index"])
            emilianosyear+=1
def get_greatest(year):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    sebasindex=0
    for c in nations:
        if str(c["Year"])==year:
            if c["Metrics"]["State Fragility Index"] > sebasindex:
                sebasindex=c["Metrics"]["State Fragility Index"]
    return sebasindex
def get_highc(year):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    sebasindex=0
    dejesus=""
    for c in nations:
        if str(c["Year"])==year:
            if c["Metrics"]["State Fragility Index"] > sebasindex:
                sebasindex=c["Metrics"]["State Fragility Index"]
                dejesus=c["Country"]
    return dejesus
def get_lowest(year):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    sebasindex=100
    for c in nations:
        if str(c["Year"])==year:
            if c["Metrics"]["State Fragility Index"] < sebasindex:
                sebasindex=c["Metrics"]["State Fragility Index"]
    return sebasindex

def get_average(year):
    with open('state_fragility.json') as state_data:
        nations=json.load(state_data)
    sebasindex=0
    for c in nations:
        if str(c["Year"])==year:
            sebasindex += (c["Metrics"]["State Fragility Index"])
    sebasindex=sebasindex/178
    return sebasindex
    


        

  
        

def is_localhost():
    """ Determines if app is running on localhost or not
    Adapted from: https://stackoverflow.com/questions/17077863/how-to-see-if-a-flask-app-is-being-run-on-localhost
    """
    root_url = request.url_root
    developer_url = 'http://127.0.0.1:5000/'
    return root_url == developer_url
    

if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production