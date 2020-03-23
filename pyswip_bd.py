from pyswip import Prolog
prolog = Prolog()
prolog.consult("BD.pl")


class BD_prolog():
    def getCategorias(self):
        lista = []
        for soln in prolog.query("juego(_,Y)"):
            lista.append(soln["Y"])
        return list(set(lista))

    def getJuegos(self, categoria):
        lista = []
        for soln in prolog.query("juego(X,%r)" % categoria):
            lista.append(soln["X"])
        return list(set(lista))

    def getAll(self):
        all = {}
        for i in self.getCategorias():
            all[i] = self.getJuegos(i)
        return all

    def get_jgs(self, lista):
        l = []
        for i in lista:
            l += self.getAll()[i]
        return list(set(l))


BD = BD_prolog()
# print(BD.getAll().keys())
print(BD.get_jgs(['aventura', 'accion', 'plataformas']))
