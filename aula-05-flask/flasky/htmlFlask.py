from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("helloBootstrap.html")

@app.route("/sensores")
def sensores():
    valores = [1.2, 4, 5.7, 0.1, 3.14]
    return render_template("sensores.html", valores=valores)

if __name__ == "__main__":
    app.run(debug=True)
