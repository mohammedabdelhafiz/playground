from flask import Flask, render_template  
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome all"

@app.route('/play')
def firstplay():
    return render_template("basic.html")

@app.route('/last')
def secondplay ():
    return render_template("basic_two.html")


if __name__=="__main__":       
    app.run(debug=True)   