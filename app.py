from pyswip_bd import BD_prolog
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BD_pg = BD_prolog()  # conexion bd prolog
cats = BD_pg.getCategorias()  # obtiene todas las categorias que hay en la bd
all = BD_pg.getAll()  # obtiene un diccionario de categorias con una lista de juegos
l_juegos = BD_pg.getJuegosSC()  # obtiene todos los juegos de la bd
# obtiene un diccionario en el que cada juego tiene sus otros datos de la bd
juegos = BD_pg.setDescipciones()
# obtiene un diccionario con el nombre, contraseña y los juegos que juega
info_usuarios = BD_pg.setInfoUsuarios()

# esta función se usa en la ruta principal para hacer la lista de las carategorias escogidas


def get_jgs(lista):
    l = []
    for i in lista:
        l += all[i]
    return list(set(l))


# esta lista se usa para guardar los generos seleccionados
# se usa en las 2 rutas de la pagia
generos_sel = []

# se define lo que hace la ruta de inicio


@app.route('/galaga')
def galaga():
    return render_template('/galaga.html')


@app.route('/profile/galaga')
def galagap():
    return render_template('/galaga.html')


@app.route('/caza')
def caza():
    return render_template('/caza.html')


@app.route('/profile/caza')
def cazap():
    return render_template('/caza.html')


@app.route('/saltarin')
def saltarin():
    return render_template('/saltarin.html')


@app.route('/profile/saltarin')
def saltarinp():
    return render_template('/saltarin.html')


@app.route('/j_2048')
def j_2048():
    return render_template('/j_2048.html')


@app.route('/profile/j_2048')
def j_2048p():
    return render_template('/j_2048.html')


@app.route('/busca_flores')
def busca_flores():
    return render_template('/busca_flores.html')


@app.route('/profile/busca_flores')
def busca_floresp():
    return render_template('/busca_flores.html')


@app.route('/covid_runner')
def covid_runner():
    return render_template('/covid_runner.html')


@app.route('/profile/covid_runner')
def covid_runnerp():
    return render_template('/covid_runner.html')


@app.route('/register')
def register():
    return render_template('/register.html')


@app.route('/', methods=['POST', 'GET'])
def index():
    user = None
    if request.method == 'POST':
        if request.method == 'POST':
            if request.form['username'] in list(info_usuarios.keys()):
                user = request.form['username']
                if request.form['password'] in info_usuarios[user]['password']:
                    print("acceso\n")
                    i = '0'
                    return redirect('/profile/%s' % request.form['username'])
                else:
                    print("error contra\n")
                    return redirect('/')
            else:
                print("no encontrado")
                return redirect('/')
    return render_template("/login.html")


@app.route('/categorias', methods=['POST', 'GET'])
def categorias():
    if request.method == 'POST':
        generos_sel.clear()  # limpia la lista de las categorias
        req = request.form.to_dict().keys()
        for i in req:  # llena la lista con la selección
            generos_sel.append(i)
        return redirect('/sugerencias')
    return render_template("categorias.html", categorias=cats)


# se define la ruta de sugerencias


@app.route('/sugerencias')
def sugerencias():
    # se hace una lista de las categorias sin que se repitan
    c = list(set(generos_sel))
    j_r = get_jgs(c)  # se obtienen los juegos de esas categorias
    return render_template('sugerencias.html', juegos_rec=j_r, juegos=juegos)


@app.route("/profile/<username>")
def profile(username):
    user = None
    if username in info_usuarios:
        user = info_usuarios[username]
        print("\n")
        lista = []
        for i in info_usuarios[username]['juegos']:
            if info_usuarios[username]['juegos'][i] != ' 0':
                lista.append(i)
        print(juegos[lista[0]])
    return render_template('sugerenciasU.html', juegos_rec=lista, juegos=juegos)


if __name__ == '__main__':
    app.run(debug=True)
