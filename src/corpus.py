from texte import Texte, Madame_Bovary

class Corpus:

    def __init__(self, nom : str):
        self.nom = nom
        self._textes = []
    
    def ajouter(self, texte : Texte) ->None:
        self._textes.append(Texte)
    
    def total_mots(self) ->int:
        return sum(t.nombre_de_mots() for t in self._textes)
    
    def rechercher(self, mot_cle : str) -> list[Texte]:
        return [t for t in self._textes if mot_cle in t.titre]
    
    def __repr__(self) ->str:
        return...
    
bib = Corpus("BU Lettres")
bib.ajouter(Madame_Bovary)
print(bib.total_mots())