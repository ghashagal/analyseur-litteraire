from collections import Counter

class Texte:

    def __init__(self, titre: str, auteur: str, contenu:str, annee: int):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.annee = annee

    def nombre_de_mots(self) ->int:
        return sum(len(coupage.split())for coupage in self.contenu)

    def mots_uniques(self) -> set[str]:
        cnt = Counter(self.contenu.split())
        uniq = set()
        for mot in cnt:
            if cnt[mot] == 1:
                uniq.add(mot)
        return uniq
    
    def frequence(self) ->int:
        frequence = Counter(self.contenu.split()) 
        print(frequence)
        return frequence

    # titre setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        self._titre = nouveau.strip()
    
    def __repr__(self) ->str:
        return f"Texte(titre = {self.titre}, auteur= {self.auteur}, annee = {self.annee})"

Madame_Bovary = Texte("Bovary", "Flaubert", "Je ne suis pas pret de deguster ma merguez", 1997)
print(Madame_Bovary)
print(Madame_Bovary.mots_uniques)
print(Madame_Bovary.frequence)




