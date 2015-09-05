from flask import Flask, render_template, request, flash

app = Flask("p12pos")
app.secret_key = "merkiowlkitty"

import p12pos.views.core
