from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# conectamos con la BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


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
    categorias = Categoria.query.order_by(Categoria.nombre).all()

    if request.method == 'POST':
        generos_sel.clear()
        req = request.form.to_dict().keys()
        # print(req)
        for i in req:
            generos_sel.append(i)

        return redirect('/sugerencias')

    return render_template("/index.html", categorias=categorias)


@app.route('/sugerencias')
def sugerencias():

    c = list(set(generos_sel))
    return render_template('sugerencias.html', generos_sel=c)


if __name__ == '__main__':
    app.run(debug=True)
