from flask import Flask, render_template, request, flash

app = Flask("p12pos")
app.secret_key = "merkiowlkitty"

@app.route("/", methods=["GET"])
def root():
    return render_template("index.html")
