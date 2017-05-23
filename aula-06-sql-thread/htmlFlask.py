from flask import Flask, render_template
app = Flask(__name__)
import db_sqlite

@app.route("/")
def hello():
    valores = db_sqlite.retorna_dados_sensores(50)
    print valores
    return render_template("helloBootstrap.html")

@app.route("/sensores")
def sensores():
    valores = db_sqlite.retorna_dados_sensores()
    return render_template("sensores.html", valores=valores)

if __name__ == "__main__":
    app.run(debug=True)
