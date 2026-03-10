from texte import Texte, Madame_Bovary, Echec



class Corpus:

    def __init__(self, nom : str):
        self.nom = nom
        self._textes = []
    
    def ajouter(self, texte : Texte) ->None:
        self._textes.append(texte)
    
    def total_mots(self) ->int:
        return sum(t.nombre_de_mots() for t in self._textes)
    
    def rechercher(self, mot_cle : str) -> list[Texte]:
        return [t for t in self._textes if mot_cle in t.titre]
    
    def __repr__(self) ->str:
        return
    
    def __len__(self) ->int:
        return len(self._textes)
    
    def __getitem__(self, index: int) -> Texte:
        return self._textes[index]
    
    def __contains__(self, titre : str) -> bool:
        return any(t.titre == titre for t in self._textes)
    
    def __iter__(self):
        return iter(self._textes)
    
    def __add__(self, other: "Corpus") -> "Corpus":
        nouveau = Corpus(f"{self.nom} + {other.nom}")
        for t in self._textes:
            nouveau.ajouter(t)
        for t in other._textes:
            nouveau.ajouter(t)
            return nouveau
    


bib = Corpus("BU Lettres")
bib.ajouter(Madame_Bovary)

bib1 = Corpus("BU Math")
bib1.ajouter(Echec)

bib3 = bib + bib1

for t in bib3:
    print(t)

