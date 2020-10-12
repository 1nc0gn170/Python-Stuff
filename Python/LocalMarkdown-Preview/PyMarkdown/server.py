#!/usr/bin/python3

from flask import Flask,request,render_template,jsonify
from markdown import markdown

app = Flask(__name__)
app.debug = 1

def modify(content):
	print(content)
	return content.replace("<table>","<table border='1'>")

@app.route("/save",methods=["POST"])
def save():
	if (request.method == "POST"):
		md = request.form.get("markdown")
		if (md):
			with open("source.md",'w') as md_file:
				md_file.write(md)
				md_file.close()
		return jsonify({"status":"success"}),200
	return jsonify({"status":"invalid"}),400


@app.route("/parse",methods=["GET","POST"])
def parse():
	if (request.method == "POST"):

		md_json = request.get_json()['data']

		md_res = markdown(md_json,extensions=['tables',"fenced_code","markdown_markup_emoji.markup_emoji"])

		return ({"output":modify(md_res)}),200

	return jsonify({"status":"invalid"}),400


@app.route("/show")
def show():
	return render_template("test.html"),200


@app.route("/")
def Markdown():
	return render_template("markdown.html"),200

app.run()

