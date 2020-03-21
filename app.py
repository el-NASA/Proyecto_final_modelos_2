from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# conectamos con la BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Juego(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    # autores = db.Column()
    # ejecutable = = db.Column()

    def __repr__(self):
        return '<Juego %r>' % self.id


class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Categoria %r>' % self.id


nombres = ['accion', 'aventura']


@app.route('/', methods=['POST', 'GET'])
def index():
    categorias = Categoria.query.order_by(Categoria
                                          .nombre).all()
    render_template("index.html", categorias=categorias)
    if request.method == 'POST':
        c_escogidas = request.form['content']
        return render_template("sugerencias.html")
    else:
        return render_template("index.html", categorias=categorias)


@app.route('/sugerencias/')
def sugerencias():
    return render_template('sugerencias.html')


if __name__ == '__main__':
    app.run(debug=True)
