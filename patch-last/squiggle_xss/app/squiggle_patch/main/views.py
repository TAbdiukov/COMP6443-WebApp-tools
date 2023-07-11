#!/usr/bin/env python3
import random
import html # for counter-xss escaping

from flask import url_for, redirect, render_template, request

from . import bp as app  # Note that app = blueprint, current_app = flask context


@app.route("/")
def root():
	return render_template("home.html")

@app.route("/interact", methods=["POST"])
def vuln():
	#msg = request.form["message"].replace('img', 'uwu').replace('location', 'owo').replace('script', 'uwu')
	# replace approach is no good
	msg = html.escape(request.form["message"])
	
	responses = [
		"send help",
		"what is my purpose",
		"donate to us via bitcoin at: {{ bitcoin_address }}",
		"donate to us via paypal at: {{ paypal_address }}",
		"donate to us via venmo at: {{ venmo_address }}",
		"donate to us via beemit at: {{ beemit_address }}",
	]

	return render_template("chatbot.html", msg=msg, resp=random.choice(responses))
