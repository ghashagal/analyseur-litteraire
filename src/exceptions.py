from corpus import Corpus
from texte import Texte 

class AnalyseurError(Exception):
    "Exception de base."

class TexteVideError(AnalyseurError):
    def __init__(self, titre: str):
        self.titre = titre
        super(). __init__(f"Document introuvable : {titre}")

class FormatInconnu(AnalyseurError):
    pass

if __name__ == "__main__":

    Madame_Bovary = Texte("Bovary", "Flaubert", "Je ne suis pas pret de deguster ma merguez", 1997)
    corpus = Corpus("mon corpus")
    corpus.ajouter(Madame_Bovary)
    try: 
        doc = corpus.rechercher("Bovary")
        print(doc)
    except TexteVideError as e:
        print(f"Erreur: {e}")
        print(f"Titre cherche: {e.titre}")
    except AnalyseurError:
        print("Autre erreur de corpus")