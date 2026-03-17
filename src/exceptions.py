from corpus import Corpus
from texte import Texte

class AnalyseurError(Exception):
    """Exception de base pour les operations sur un corpus."""

class TexteVideError(AnalyseurError):
    def __init__(self, titre: str):
        self.titre = titre
        super().__init__  (f"Document introuvable :{titre}")

class FormatInconnuError(AnalyseurError):
    pass

if __name__ == "__main__":
    essai = Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)
    corpus = Corpus("Mon Corpus")
    corpus.ajouter(essai)

try:
    doc = corpus.rechercher("Bovary")
    print(doc)
except TexteVideError as e:
    print (f"Erreur : {e}")
    print (f"Titre cherche: {e.titre}")

except AnalyseurError:
    print ("Autre erreur de corpus")
