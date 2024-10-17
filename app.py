from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def house():
    return render_template("index.html")


@app.route('/Quienes_Somos')
def about():
    return render_template('Quienes_Somos.html')



@app.route('/Servicios')
def services():
    return render_template('Servicios.html')



@app.route('/Contactos')
def contacto():
    return render_template('Contactos.html')



@app.route('/Noticias')
def news():
    return render_template('Noticias.html')



if __name__=="__main__":
    app.run(debug=True)