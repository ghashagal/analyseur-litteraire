from texte import Texte
from collections import Counter
from abc import ABC, abstractmethod

class AnalyseurTexte(ABC):
  @abstractmethod
  def analyser(self, texte: "Texte") -> dict: ...
  def analyser_corpus(self, texts: list["Texte"]) -> list[dict]:
    return [self.analyser(t) for t in texts]

class AnalyseurFrequence(AnalyseurTexte):
  def frequence(self) -> int :
    frequence = Counter(self.contenu.split())
    print(frequence)

class AnalyseurLongueur(AnalyseurTexte):
  def analyser(self, texte: "Texte") -> dict:
    mots = texte.resume().lower().split()
    return {"total": len(mots), "uniques": len(set(mots))}
