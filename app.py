import csv
from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__) # first instance of class

@app.route("/")
def index():
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
