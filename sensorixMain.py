#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         sensorixMain.py
# Purpose:      Main module of the Physical parameters processor
#
# Author:       dipl.eng. Svilen Zlatev
#
# Created:      19-February-2018
# Copyright:    (c) 2018 by Pronix1 Ltd.
# Licence:      GNU Public License v3.0;
#----------------------------------------------------------------------------

"""
sensorixMain
"""

from flask import Flask, request, g, render_template #import main Flask class and request object
import sqlite3 as sql

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)
              
@app.route('/add-record')
def addRecord():
    return render_template('sensorix_add.html')

@app.route("/echo", methods=['POST'])
def echo(): 
    return "You said: " + request.form['text']

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000