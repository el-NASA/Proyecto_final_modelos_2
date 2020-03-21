from flask import Flask, render_template
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


@app.route('/')
def index():
    return render_template("index.html", nombres=nombres)


if __name__ == '__main__':
    app.run(debug=True)
