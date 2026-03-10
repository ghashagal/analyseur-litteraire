from texte import Texte
class Roman ( Texte ) :
    def __init__ ( self , titre : str , auteur : str ,
        annee : int , genre : str, contenu : str ) :
        super().__init__ ( titre , auteur , contenu,  annee )
        self . genre = genre
    def resume ( self ) -> str : # override
        return f" [{ self . genre }] { self . titre } "
    
class Poeme ( Texte ) :
    def __init__ ( self , titre : str , auteur : str ,
        annee : int , vers : int, forme : str, contenu : str) :
        super().__init__ ( titre , auteur , contenu, annee )
        self . vers = vers
        self. forme = forme
    def resume ( self ) -> str : # override
        return f" Poeme de { self . vers } vers (Poeme de { self. forme})"

class Article(Texte):
    def __init__(self, revue : str, titre: str, auteur : str, annee: int, contenu : str):
        super(). __init__ (titre, auteur, contenu, annee )
        self.revue = revue
    def resume(self) -> str:
        return f" Article de {self. revue}"
    
def afficher_resumes(documents: list[Texte]) -> None:
    for doc in documents:
        print(f"{doc.titre} : {doc.resume()}")

docs = [
    Roman("Germinal", "Zola", 1885, "Naturaliste", "fdghrfhnfrjhrh"),
    Poeme("Les Fleurs du mal", "Baudelaire", 1857, 126, "sonnet", "seifbuIUGösigvöigFoöegfu"),
    Article("Lefigaro", "Les fleurs du bien", "Madame Bovary", "hufogfgifgifgg", 2340)
]
afficher_resumes(docs)
    