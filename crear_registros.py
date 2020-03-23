from app import db, Juego, Categoria, Juego_categoria

'''
ejecutar esto para crearlo desde cero
db.create_all()
'''

# añadiendo juegos
n_juegos = ['mario', 'assassins creed',
            'spec ops : the line', 'Alien : isolation']

for i in n_juegos:
    juego = Juego(nombre=i)
    db.session.add(juego)

# añadiendo categorias
n_categorias = ['aventura', 'accion', 'miedo', 'disparos']

for i in n_categorias:
    cat = Categoria(nombre=i)
    db.session.add(cat)

# definiendo las categorias de los juegos
rango = Juego_categoria.query.count()
for i in range(1, rango + 1):
    x = Juego_categoria.query.filter_by(id=i).first()
    db.session.delete(x)
# mario
j_g = Juego_categoria(n_juego=n_juegos[0], n_categoria=n_categorias[0])
db.session.add(j_g)
j_g = Juego_categoria(n_juego=n_juegos[0], n_categoria=n_categorias[1])
db.session.add(j_g)
# assassins creed
j_g = Juego_categoria(n_juego=n_juegos[1], n_categoria=n_categorias[0])
db.session.add(j_g)
j_g = Juego_categoria(n_juego=n_juegos[1], n_categoria=n_categorias[1])
db.session.add(j_g)
# spec ops: the line
j_g = Juego_categoria(n_juego=n_juegos[2], n_categoria=n_categorias[1])
db.session.add(j_g)
j_g = Juego_categoria(n_juego=n_juegos[2], n_categoria=n_categorias[3])
db.session.add(j_g)
# Alien isolation
j_g = Juego_categoria(n_juego=n_juegos[3], n_categoria=n_categorias[2])
db.session.add(j_g)

db.session.commit()
