from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pagina__inicial():
  return render_template('index.html')

@app.route("/cardapio")
def pagina__cardapio():
  return render_template('cardapio.html')


@app.route("/reserva")
def pagina__reserva():
  return render_template('reserva.html')

if __name__ == "__main__":
 app.run(debug=True)