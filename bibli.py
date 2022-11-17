import os
import sys
from PyPDF2 import PdfFileReader
import epub
import glob
from pathlib import Path
import concurrent.futures
import configparser
import time
from multiprocessing import Pool as ProcessPool

config = configparser.RawConfigParser().read("bibli.conf")


def combiner_paths(path, extensions):
    fichiers = []
    for e in extensions:
        fichiers.extend(Path(path).glob(e))
    return fichiers


class Bibliotheque():
    def __init__(self, path) -> None:
        # paths_epub = Path(path).glob("*.epub")
        # paths_pdf = Path(path).glob("*.pdf")

        paths = combiner_paths(path, ("*.pdf", "*.epub"))
        print("path recupere")
        start = time.time()

        res = list(map(Livre, paths))
        self.livres = set(res)
        with ProcessPool(processes=10) as executor:
            result = executor.map(Livre, paths)
            for livre in result:
                if livre not in self.livres:
                    self.livres.add(livre)
                # else:
                    # livre.force_del()

        self.auteurs = set(map(lambda x: getattr(x, "auteur"), self.livres))
        print("finito en", time.time()-start, "secondes")

class Livre():
    def __init__(self, path) -> None:
        self.path = path
        self.file_name = path.name
        self.auteur = None
        self.titre = None

        if path.suffix == ".pdf":
            self._open_pdf()
        elif path.suffix == ".epub":
            self._open_epub()

    def __repr__(self) -> str:
        return f"{self.titre} par {self.auteur}"

    def _open_pdf(self):
        with self.path.open(mode='rb') as f:
            pdf = PdfFileReader(f,strict=False)
            information = pdf.metadata
            self.auteur = information.author
            self.titre = information.title

    def _open_epub(self):
        with epub.open_epub(f'{self.path}') as book:
            metadata = book.opf.metadata
            auteur = metadata.creators[0][0]
            titre = metadata.titles[0][0]
            self.auteur = auteur
            self.titre = titre

    def force_del(self):
        self.path.unlink()
        del self

    def __hash__(self) -> int:
        return hash((self.auteur, self.titre))

    def __eq__(self, __o: object) -> bool:
        return (self.auteur == __o.auteur and self.titre == __o.titre)



if __name__ == "__main__":
    args = sys.argv

    bibli = Bibliotheque("./livres/")
