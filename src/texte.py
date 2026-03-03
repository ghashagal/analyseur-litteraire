from collections import Counter

class Texte :
    def __init__(self, titre : str, auteur : str, contenu : str, annee : int):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.annee = annee

    def nombre_mots(self) -> int:
            return sum(len(cont.split()) for cont in self.contenu)
        
    def mots_unique(self) -> set[str]:
            count = Counter(self.contenu.split)
            uniq = set()
            for mot in count:
                  if count[mot] == 1:
                        uniq.add(mot)
            
    def frequences(self) -> int:
          frequences = Counter(self.contenu.split)
          return frequences
    
    @property
    def titre(self) -> str:
          return self._titre
    
    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre ne peut pas etre vide")
        self._titre = nouveau.strip()

    def __str__(self) -> str:
        return f"{self.titre}, {self.auteur}, {self.contenu}, {self.annee}"
    
    def __repr__(self) -> str:
         return (f"Texte(titre={self.titre!r}),"
                 f"auteur={self.auteur!r}, annee={self.annee}")
    
    def __eq__(self, other) -> bool:
         if not isinstance(other, Texte):
              return NotImplemented
         return (self.titre == other.titre and self.auteur == other.auteur) 
    
    def __lt__(self, other) -> bool:
         if not isinstance(other, Texte):
              return NotImplemented
         return (self.annee < other.annee)
      
if __name__ == "__main__":
    essai = Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)
    essai1 = Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)
    essai2 = Texte("Candide", "Voltaire", "Il fait beau aujourd'hui", 1759)
    print(essai)
    print(essai.nombre_mots())
    print(essai.mots_unique())
    print(essai.frequences())

    textes = [essai, Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)]
    textes = [essai1, Texte("Bovary", "Flaubert", "Il fait beau aujourd'hui", 1920)]
    textes = [essai2, Texte("Candide", "Voltaire", "Il fait beau aujourd'hui", 1759)]
    
    for t in sorted(textes):
        print(t)