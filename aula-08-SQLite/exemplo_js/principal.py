from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("main.html")

@app.route('/update_sensor')
def sensor():
    print 'sensor'
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(debug=True)
