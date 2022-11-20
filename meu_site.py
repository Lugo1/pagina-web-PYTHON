from flask import Flask, render_template, request, flash

# Render_Template es para que visualize lo que esta en HTML y no en .py
#Flask recomienda que nombrees con "app"

app = Flask(__name__)
app.secret_key = "Conttraseña_o_cualquier_otro"
###################### Criar a 1era pagina do site######################
# Toda pagina Web tiene siempre un: ROUTE y una FUNCION
#ROUTE: es el camino que tienes que pasar despues del corchet "/"..... Lugo.com/
#FUNCION: es lo que quieres exibir en la pagina
#...empezamos creando una funcion:
#...Luego colocamos al inicio "@app.route()"...y route es para definir el link de la pagina. Atribue una nueva funcionalidad a la funcion.
#...
@app.route("/")
def homepage():
    flash("Cúal es tu nombre?")
    return render_template("homepage.html")
    #return "Mi primera página WEB...mis primeros pasos...123"

@app.route("/greet", methods=["POST", "GET"])
def nombres():
    flash("Waoo!: " + str(request.form['name_input']))
    flash("Gracias por comentar!!!"+"Pareces inteligente! :)")
    return render_template("homepage.html")
    #return render_template("nombres.html")
    #return "<p>1. Juan...</p><p>2. Emi... </p><p>3. Jona </p>EMAIL: @@@"

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)




####################### ultimo colocar o site no ar######################
# Colocaremos este Site en el servidor: "heroku" este es gratuito
# Quien coloca en el aire?--> este comando "app.run()"

if __name__ == "__main__":
    app.run(debug=True)
# "debug=True": activa en el Site los cambios, facilita para ya no estar parando y rodando nuevamente.
# " if __name__ == "__main__": ": ...corre lo que esta dentro de el.