from texte import Texte
from abc import ABC, abstractmethod 

class DocumentComplet(Texte):
    def analyser(self): return self.frequences()

class Exportateur(ABC):
    @abstractmethod
    def exporter(self) -> str: ...

class ExporterHtml(Exportateur):
    def exporter(self,texte : Texte):
        return f" <h1 >{ texte . titre } </ h1 > <p >{ texte . contenu } </p >"
    
class ExporterCsv(Exportateur):
    def exporter(self, texte : Texte):
        return " \ n " . join ( f" { m } ,{ c } " for m , c in texte . frequences () .
        items () )

class Sauvegarder(Exportateur):
    def sauvegarder(self, chemin, texte): 
     with open(chemin, "w") as f: 
        f.write(texte.contenu)

class ExportMarkdown(Exportateur): ...
# La Factory : un dict de classes suffit en Python
EXPORTATEURS: dict[str, type[Exportateur]] = {
    "html": ExporterHtml, "csv": ExporterCsv, "md": ExportMarkdown,
}
def creer_exportateur(format: str) -> Exportateur:
    cls = EXPORTATEURS.get(format)
    if cls is None:
        raise ValueError(f"Format inconnu : {format}")
    return cls()

if __name__ == "__main__":
    texte = Texte("Mon titre", "Moi", "Contenu du texte", 2024)

    exportateur = creer_exportateur("html")
    print(exportateur.exporter(texte))

    EXPORTATEURS["html"] = ExporterHtml

    exportateur = creer_exportateur("markdown")

