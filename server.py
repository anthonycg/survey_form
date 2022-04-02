from distutils.log import debug
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "BB"

@app.route('/')
def index():
    print(request.form)
    # print(request.form['location'])
    # print(request.form['fav_lang'])

    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['username'] = request.form['username']
    session['location'] = request.form['location']
    session['fav_lang'] = request.form['fav_lang']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', username=session['username'], location=session['location'],
    fav_lang=session['fav_lang'], comments=session['comments'])

if __name__ == '__main__':
    app.run(debug=True)