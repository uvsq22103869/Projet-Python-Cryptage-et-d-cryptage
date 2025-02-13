class ArbreB:
    def __init__(self, s_arbreg, s_arbred, valeur):
        self.s_arbreg = s_arbreg
        self.s_arbred = s_arbred
        self.valeur = valeur

    def est_vide(self):
        return self.valeur is None and self.s_arbreg is None and self.s_arbred is None

    def recherche(self, e):
        if self.est_vide():
            return False

        elif e == self.valeur:
            return True

        elif self.s_arbreg is not None:
            if self.s_arbreg.recherche(e):
                return True

        elif self.s_arbred is not None:
            if self.s_arbred.recherche(e):
                return True

        return False
    
    def insertion(self, val) :
        pass

class Sommet(ArbreB) :
    def __init__(self, s_arbreg, s_arbred, valeur, label):
        super().__init__(s_arbreg, s_arbred, valeur)
        self.label = label

    def modification(self, new_label) :
        self.label = new_label
