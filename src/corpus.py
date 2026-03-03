from collections.abc import Iterator

from texte import Texte


class Corpus:
    def __init__(self, nom : str):
        self.nom = nom
        self._textes = []

    def ajouter(self, texte : Texte) ->None:
        self._textes.append(texte)

    def total_mots(self) ->int:
        return sum(t.nombre_mots() for t in self._textes)
    
    def rechercher(self, mot_cle : str) -> list[Texte]:
        return [t for t in self._textes if mot_cle in t.titre]
    
    def __repr__(self) ->str:
        return
    
    def __len__ (self) -> int :
        return len(self._textes)
    
    def __getitem__ (self, index : int) -> Texte :
        return self._textes[index]
    
    def __iter__ (self)  -> Iterator[Texte] :
        return iter(self._textes)
    
    def __contains__ (self, titre : str) -> bool :
        return any(t.titre == titre for t in self._textes)
    
    def __add__ (self, other : "Corpus") -> "Corpus" :
        nouveau = Corpus (f"{self.nom} + {other.nom}")
        for t in self._textes :
            nouveau.ajouter(t)
        for t in other._textes :
            nouveau.ajouter(t)
            return nouveau


if __name__ == "__main__":
    essai = Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)
    essai1 = Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)
    essai2 = Texte("Candide", "Voltaire", "Il fait beau aujourd'hui", 1759)
    bib = Corpus("BU lettres")
    bib.ajouter(essai)
    bib.ajouter(essai1)
    bib.ajouter(essai2)


    print(bib.total_mots())

    for t in bib:
        print(t)