from texte import Texte
from abc import ABC, abstractmethod 

class DocumentComplet(Texte):
    def analyser(self): return self.frequences()

class Exportateur(ABC):
    @abstractmethod
    def exporter(self) -> str: ...

class ExporterHtml(Exportateur):
    def exporter(texte : Texte):
        return f" <h1 >{ texte . titre } </ h1 > <p >{ texte . contenu } </p >"
    
class ExporterCsv(Exportateur):
    def exporter(texte : Texte):
        return " \ n " . join ( f" { m } ,{ c } " for m , c in texte . frequences () .
        items () )

class Sauvegarder(Exportateur):
    def sauvegarder(self, chemin, texte): 
     with open(chemin, "w") as f: 
        f.write(texte.contenu)
