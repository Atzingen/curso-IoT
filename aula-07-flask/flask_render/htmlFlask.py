from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("helloBootstrap.html")

@app.route("/sensores")
def sensores():
    valores = [1.2, 4, 5.7, 0.1, 3.14]  # Alterar para os valores dos sensores
    return render_template("sensores.html", valores=valores)

@app.route("/servo/<valor>")
def servo(valor):
    print "valor: ", valor      # alterar para fazer algo com o dado
    return render_template("helloBootstrap.html")

if __name__ == "__main__":
    app.run(debug=True)
