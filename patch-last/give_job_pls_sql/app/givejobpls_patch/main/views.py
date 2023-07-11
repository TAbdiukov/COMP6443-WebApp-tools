#!/usr/bin/env python3
import secrets
import string # for hackshield

from flask import url_for, redirect, current_app, jsonify, request

from . import bp as app  # Note that app = blueprint, current_app = flask context

# Make any changes to the data/schema here

SCHEMA = """
CREATE TABLE IF NOT EXISTS applications (
	id INTEGER ,
	job TEXT,
	name TEXT,
	contact TEXT,
	flag TEXT
);
"""

# secrets.token_hex(10) - seems safe enough
# https://docs.python.org/3/library/secrets.html
DATA = [
	["a2dsa4qs21B", "window washer", "zain afzal", "verygoodwindowwashing@gmail.com", None],
	[secrets.token_hex(10), "button pusher", "zain afzal", "verygoodbuttonpushing@gmail.com", None],
	[secrets.token_hex(10), "something doer", "zain afzal", "verygoodsomethingdoing@gmail.com", None],
	[secrets.token_hex(10), "flag holder", "zain afzal", "verygoodflagholding@gmail.com", "flag{wow_a_flag}"],

]


@app.before_request
def hackshield():
	# let buffer be the holder of request path
	buf = request.full_path
	buf = buf.lower() # lower it
	buf = buf.replace(" ", "") # strip whitespaces anywhere
	# i suppose whitespaces are allowed in general, hence they are not in blockedCharacter
	
	# blockedCharacter - now stores less information due to buf design
	for blockedCharacter in [
		"all",
		"and",
		";",
		",",
		"'",
		"or",
		"-",
		"#",
		chr(34), # the full size quotation mark, against SQLi
		"%", # against char->text hackery
		"<", # against XSS
		">", # against XSS
		"*", #against SQLI
		"from", #against SQLI
		"select", #against sqli commands
		"alter", #against sqli commands
		"delete", #against sqli commands
		"drop", #against sqli commands
		"insert", #against sqli commands
		"create", #against sqli commands
		"copy", #against sqli commands
		"+", # against SQLi logic tricks
		"&", # against SQLi logic tricks
		"|", # against SQLi logic tricks
		"like", # against SQLi logic tricks
		"::", # against SQLi logic tricks (postgresql)
		"=" # against SQLi logic tricks
		"/**/", # against SQLi postgre commenting out
	]:
		if blockedCharacter in request.full_path:
			return "hackshield activated. Prepare for annihilation", 403


@app.before_request
def hydrate_db():
	current_app.db.execute("DROP TABLE IF EXISTS applications")
	current_app.db.execute(SCHEMA)

	for record in DATA:
		current_app.db.execute("INSERT INTO applications VALUES (?, ?, ?, ?, ?)", (tuple(record),))


@app.route("/")
def root():
	return redirect(url_for("main.vuln", id="a2dsa4qs21B"))


@app.route("/application/<id>")
def vuln(id):
	try:
		data = dict(current_app.db.execute("SELECT * FROM applications WHERE id=?", (id,)).first())
		return jsonify(data)
	except Exception as e:
		return "hackshield may be activated if you continue. Your identity is sent to the police", 404
