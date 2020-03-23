from pyswip_bd import BD_prolog
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from pyswip_bd import BD_prolog

app = Flask(__name__)
# conectamos con la BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
# conexion bd prolog
BD_pg = BD_prolog()
cats = BD_pg.getCategorias()
all = BD_pg.getAll()


def get_jgs(lista):
    l = []
    for i in lista:
        l += all[i]
    return list(set(l))


class Juego(db.Model):
    nombre = db.Column(db.String(50), primary_key=True)
    # autores = db.Column()
    # ejecutable = = db.Column()

    def __repr__(self):
        return '<Juego %r>' % self.nombre


class Categoria(db.Model):
    nombre = db.Column(db.String(50), primary_key=True)

    def __repr__(self):
        return '<Categoria %r>' % self.nombre


class Juego_categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    n_juego = db.Column(db.String(50), nullable=True)
    n_categoria = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return '<id: %r | n_juego: %r | n_cat: %r>' % (self.id, self.n_juego, self.n_categoria)


generos_sel = []


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        generos_sel.clear()
        req = request.form.to_dict().keys()
        # print(req)
        for i in req:
            generos_sel.append(i)

        return redirect('/sugerencias')

    return render_template("/index.html", categorias=cats)


@app.route('/sugerencias')
def sugerencias():

    c = list(set(generos_sel))
    j_r = get_jgs(c)
    return render_template('sugerencias.html', juegos_rec=j_r)


if __name__ == '__main__':
    app.run(debug=True)
