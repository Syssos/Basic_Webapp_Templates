#!/usr/bin/env python3
# flask app for website
from flask import Flask, render_template
from gpiozero import LED
from time import sleep
from gpiozero import PWMLED


app = Flask(__name__)
app.url_map.strict_slashes = False
led = PWMLED(17)


@app.route('/')
def display_home():
    """ Displays home page
    """
    return render_template("index.html")

@app.route('/about')
def goto_about():
    """ directs traffic to about page
    """
    return render_template("about.html")

@app.route("/resume")
def goto_resume():
    """ directs traffic to resume page
    """
    return render_template("resume.html")

@app.route("/pipage")
def goto_pipage():
    """ directs traffic to pi page
    """
    return render_template("pipage.html")

@app.route("/JS_test_page")
def goto_jspage():
    """ directs traffic to js page
    """
    return render_template("JS_test.html")
        
@app.route("/about")
def goto_pi():
    """ Goes to pi section in about
    """
    return render_template("about.html")

@app.errorhandler(404)
def page_not_found(e):
    """ Returns custom 404
    """
    return render_template('404.html'), 404

@app.route("/on")
def lights_on():
    """ turns led on
    """
    led.pulse(background=True)
    return ('', 204)

@app.route("/off")
def lights_off():
    """ Turns LED off
    """
    led.off()
    return ('', 204)

if __name__ == "__main__":
    app.run(host="192.168.137.171")
