#!/usr/bin/env python3

import subprocess
from urllib.parse import unquote, urlparse

from flask import url_for, redirect

from . import bp as app  # Note that app = blueprint, current_app = flask context


@app.route("/")
def root():
	return redirect(url_for("main.vuln", provider="www.google.com", content_id="teapot"))


@app.route("/<path:provider>/<content_id>", methods=["GET", "POST"])
def vuln(provider, content_id):
	# Imagine the URL filtering being carried out here. It's not relevant for the patch.
	# scheme = "ftp"  # or "gopher" or "https"

	# Make the url absolute if its not
	if "//" not in provider:
		provider = "https://" + provider

	
	scheme = ["ftp",  "gopher", "https"]
	bad_scheme = ["file", "idkwhatelse"]
	
	protocol = provider.replace("://", "//").split("//")[0]
	print("protocol: "+protocol)
	
	if(protocol in scheme):
		# all good
		
		raw_url = unquote(f"{provider}/{content_id}")
		# raw_url =  file:///C:/0.txt
		parts = urlparse(raw_url, scheme="https")
		url = parts.geturl()

		try:
			sp = subprocess.run(["curl", url], capture_output=True, timeout=1)
		except subprocess.TimeoutExpired:
			return "timed out", 500

		if sp.returncode:
			return "failed to get url", 500

		return sp.stdout
	elif (protocol in bad_scheme):
		return "prepare to get roasted by the police", 403
	else:
		return "bad request", 400
