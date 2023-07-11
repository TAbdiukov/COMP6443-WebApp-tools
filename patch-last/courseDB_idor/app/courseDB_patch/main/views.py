#!/usr/bin/env python3

from flask import url_for, redirect, current_app, jsonify, render_template

from . import bp as app  # Note that app = blueprint, current_app = flask context

# for hashing
import hashlib
import string
from baseconv import base16, base62



SCHEMA_MARKS = """
CREATE TABLE IF NOT EXISTS marks (
	sid TEXT,
	code TEXT,
	mark INTEGER,
	comment TEXT,
	hash TEXT
);
"""

SECRET_WORD = "hahaha UNSW!"
NULL = "null"

marks = [
	["s123456","COMP1511",65,"No comment"],
	["s123456","COMP9447",93,"No comment"],
	["s103945","COMP6443",21,"FLAG{ThisWouldBeAFlag}"],
	["s133713","COMP9447",99,"FLAG{ThisWouldBeAFlag}"],
	["s133713","COMP1511",84,"FLAG{ThisWouldBeAFlag}"],
]

#This is the student you are currently logged in as
CURRENTLY_LOGGED_IN_AS='s123456'

# not so fast but very collisionless hash algo based on Keccak approach
def keccakmod(s):
	rawhash = hashlib.sha3_224(s.encode('utf-8')).hexdigest().upper()
	modhash = base62.encode(base16.decode(rawhash))
	
	return modhash

def my_hash(sid):
	
	for record in marks:
		print(record)
		if(record[0] == sid):
			return keccakmod(SECRET_WORD+str(record,))

	return ""

@app.before_request
def hydrate_db():
	current_app.db.execute("DROP TABLE IF EXISTS marks")
	current_app.db.execute(SCHEMA_MARKS)
	
	for record in marks:
		hash = keccakmod(SECRET_WORD+str(record,))
		tup = tuple(record+hash.split())
	
		current_app.db.execute("INSERT INTO marks VALUES (?, ?, ?, ?, ?)",(tup,))
		
	

@app.route("/")
def root():
	#return redirect(url_for("main.vuln",sid=CURRENTLY_LOGGED_IN_AS,code="COMP1511"))
	return redirect(url_for("main.safe",hash=my_hash(CURRENTLY_LOGGED_IN_AS)))

@app.route("/user/<sid>/<code>/view")
def vuln(sid,code):
	if(CURRENTLY_LOGGED_IN_AS == sid):
		data = dict(current_app.db.execute("SELECT * from marks WHERE sid=? AND code=?",(sid,code)).first())
		return jsonify(data)
	else:
		return render_template('403.html'), 403

@app.route("/user/<hash>/view")
def safe(hash):
	try:
		data = dict(current_app.db.execute("SELECT * from marks WHERE hash=?",(hash,)).first())
		return jsonify(data)
	except Exception as e:
		return render_template('403.html'), 403
