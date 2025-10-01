from flask import Flask,render_template
app = Flask(__name__)
@app.route('/Templetes')
def Templetes():
    return render_template("portfolio.html")


if __name__ == "__main__":
    app.run(debug=True)