# Recomendaciones venta de juegos

Es una pagina web hecha con **Flask** que usa **Prolog** junto a **Python** para hacer recomendaciones de juegos según las preferencias de los usuarios.


Es nuestro proyecto final para la clase de modelos de programación de en la Universidad Distrital Francisco José de Caldas

|Integrante|Código|
|---|---|
|Daniel Alejandro Rodríguez Suárez|20172020009|
|Jordy Esteban Pineda Velandia|20172020119|
|Nestor David Bohorquez Galeano|20172020083|

Para poder probar el proyecto debes:
* Tener instalado *pip3* y *virtualenv*
* Descargar y descomprimir el archivo en una carpeta.
*  Crear un **entorno virtual** en la carpeta escribiendo en la terminal: `virtualenv env`
*  Activar el entonrno virtual con: `source env/bin/activate`
* Instalar los requerimientos con: `pip3 install requirements.txt`
* Escribir en la termial `python3 app.py`
* Finalmente en el navegador ir a `http://127.0.0.1:5000/` (ó a la ip que flask haya asignado)

### Funcionamiento
Las sugrencias funfionan gracias a una serie de consultas hechas a una base de datos hecha en Prolog, algo que hay que tener en cuenta es que para poder combinar usar Prolog junto a Python se usó la libreria **Pyswip**, que no parece estar completa ya que hay varias consultas nativas de Prolog como `findall` que no encontramos como implementar.

Por lo tanto para hacer las consultas sin esto, se usó una combinación de funciones que hacen consultas a la base de datos y que retornan listas, para luego combinar estas funciones y poder hacer dos diccionarios:

1. Diccionario con las categorias y las listas de los juegos que pertenecen a ellas.
2. Diccionario de juegos que tiene a su vez un subdiccionario con sus caracteristicas

Estos se obtienen desde el inicio, no se pueden hacer (o desconocemos como) las consultas directas a la base de datos porque Prolog (o la libreria) se rompe haciendolo de esta forma (leimos que era debido a la imposibildad de Prolog para  trabajar con multihilos).

#### Paradigmas de programación dentro del proyecto
La idea del proyecto final es usar nuesto conocimiento de los diferentes paradigmas de programación para un objetivo, en este caso hacer recomendaciones de video juegos.

Los paradigmas usados son:
* Imperativo: `app.py`
* Orientado a objetos: `pyswip_bd.py`
* Lógico: `BD.pl`
