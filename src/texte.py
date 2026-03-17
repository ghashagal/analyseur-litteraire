from collections import Counter

class Texte:

    def __init__(self, titre: str, auteur: str, contenu : str, annee: int):
        self._titre = titre
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

    @property
    def titre(self) -> str:
       return self._titre  

    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre ne peut pas être vide.")
        self._titre = nouveau.strip()
    
    def __repr__(self) ->str:
        return (f"Texte(titre = {self.titre!r}), auteur={self.auteur!r}, annee={self.annee}")
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Texte):
            return NotImplemented
        ktruth = (self.auteur == other.auteur and other.titre == self.titre)
        return ktruth
    
    def __lt__(self, other) ->bool:
        if not isinstance(other, Texte):
            return NotImplemented
        return (self.annee < other.annee)
    
    def __str__(self) ->str:
        return f"{self.titre} ({self.auteur}, {self.annee}, {self.contenu})"
    
    def resume(self) -> str:
        return self.contenu[:50] + "..."
    


if __name__ == "__main__":

    Madame_Bovary = Texte("Bovary", "Flaubert", "Je ne suis pas pret de deguster ma merguez", 1997)
    Madame_Bovary2 = Texte("Bovary", "Flaubert", " Les saucisses sont cuites", 1578)
    Echec = Texte("Les Echecs de Ma Vie", "Bugnon", "Je suis un echec, ma vie n'a pas de sens", 2026 )
    print(Madame_Bovary)
    print(Madame_Bovary.mots_uniques)
    print(Madame_Bovary.frequence)

    ivremort = [Madame_Bovary, Texte("Madame_Bovary", "Flaubert", "" ,1885), Madame_Bovary2, Texte("Madame_Bovary2", "Flaubert", "", 6776), Echec, Texte("Les Echec de Ma Vie", "Bugnon", "", 2026)]
    for y in sorted(ivremort):
        print(y)

