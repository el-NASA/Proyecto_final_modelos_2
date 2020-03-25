from pyswip import Prolog
prolog = Prolog()
prolog.consult("BD.pl")

# no hay forma de hacer el findall con la libreria pyswip hasta el momento
# por lo que se hace un metodo para cada una de las consultas y luego
# se combinan para hacer algo similar al findall


class BD_prolog():
    def getCategorias(self):
        lista = []
        for soln in prolog.query("juego(_,Y,_,_,_)"):
            lista.append(soln["Y"])
        return list(set(lista))

    def getJuegos(self, categoria):
        lista = []
        for soln in prolog.query("juego(X,%r,_,_,_)" % categoria):
            lista.append(soln["X"])
        return list(set(lista))

    def getJuegosSC(self):
        lista = []
        for soln in prolog.query("juego(X,_,_,_,_)"):
            lista.append(soln["X"])
        return list(set(lista))

    def getAll(self):
        all = {}
        for i in self.getCategorias():
            all[i] = self.getJuegos(i)
        return all

    def getLink(self, nombre):
        lista = []
        for soln in prolog.query("juego(%s,_,Y,_,_)" % nombre):
            lista.append(soln["Y"])
            aux = list(set(lista))
        return aux[0]

    def getFoto(self, nombre):
        lista = []
        for soln in prolog.query("juego(%s,_,_,Y,_)" % nombre):
            lista.append(soln["Y"])
            aux = list(set(lista))
        return aux[0]

    def getDescipciones(self, nombre):
        lista = []
        for soln in prolog.query("juego(%s,_,_,_,Y)" % nombre):
            lista.append(soln["Y"])
            aux = list(set(lista))
        return aux[0]

    def setDescipciones(self):
        dict = {}
        for i in self.getJuegosSC():
            dict[i] = {'link': self.getLink(i), 'foto': self.getFoto(
                i), 'descripcion': self.getDescipciones(i)}
        return dict

    def getJuegosUsuario(self, nombre):
        lista = prolog.query("sug(%s,F)" % nombre)
        return lista
