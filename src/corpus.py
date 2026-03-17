from documentcomplet import ExporterCsv, ExporterHtml
from texte import Texte




class Corpus:

    def __init__(self, nom : str):
        self.nom = nom
        self._textes = []
        self.ExporterHtml = ExporterHtml()
        self.ExporterCsv = ExporterCsv()

    
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
    
    
    
if __name__ == "__main__":

    Madame_Bovary = Texte("Bovary", "Flaubert", "Je ne suis pas pret de deguster ma merguez", 1997)
    corpus = Corpus("mon corpus")
    corpus.ajouter(Madame_Bovary)
    
    bib = Corpus("mon corpus")
    bib.ajouter(Madame_Bovary)

    Echec = Texte("Les Echecs de Ma Vie", "Bugnon", "Je suis un echec, ma vie n'a pas de sens", 2026 )
    corpus2 = Corpus("mon corpus2")
    bib1 = Corpus("mon corpus2")
    bib1.ajouter(Echec)

    bib3 = bib + bib1

    for t in bib3:
        print(t)

