import os
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/setname', methods=['GET', 'POST'])
def setname():
    keyword = request.args.get('keyword', '')
    return render_template('index.html', name=keyword)