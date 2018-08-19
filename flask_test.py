#!/usr/bin/env python3
# flask app for website
from flask import Flask, render_template
from gpiozero import LED

app = Flask(__name__)
# app.url_map.strict_slashes = False

@app.route('/')
def display_home():
    """ Displays home page
    """
    return render_template("index.html")

@app.route('/about')
def goto_about():
    return render_template("about.html")

@app.route("/LED_on")
def lights_on():
    """ turns led on
    """
    return LED(17).blink()
    
if __name__ == "__main__":
    app.run(host="192.168.137.80")
