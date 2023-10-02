from flask import Flask, render_template, request  #adicionar para trabalhar com os métodos GET e POST

site = Flask(__name__) 

@site.route("/")     
@site.route("/index")  
def indice():
    return render_template ("login.html")

@site.route("/cadastro")
def contato():
    return render_template("cadastro.html") 


@site.route("/autenticar", methods=['POST']) 
def autenticar():
    usuario = request.form.get('email')
    senha = request.form.get('senha')
    return f"usuario: {usuario} e senha: {senha}"

if __name__ == "__main__":
    site.run(host='0.0.0.0', port=8080, debug=False)
     