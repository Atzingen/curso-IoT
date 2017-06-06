from flask import Flask, render_template, request
import mosquitto
app = Flask(__name__)


@app.route("/")
def hello():
    topico = request.args.get('topico', 0)
    valor = request.args.get('valor', 0, type=int)
    print topico, valor
    mosquitto.publica(topico, valor)
    return render_template("helloMQTT.html")

@app.route("/sensores")
def sensores():
    valores = [1.2, 4, 5.7, 0.1, 3.14]
    return render_template("sensores.html", valores=valores)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
