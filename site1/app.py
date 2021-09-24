import os
from flask import Flask, jsonify, request, render_template, redirect

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
# @app.route('/getname', methods=['GET', 'POST'])
def getname():
    if request.method == "POST":
        keyword = request.form.get("keyword", '')
        print (keyword)
        if keyword:
            url = "http://localhost:5001/setname?keyword=" + str(keyword)
            return redirect(url)
    return render_template('index.html')