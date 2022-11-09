#!/usr/bin/python

import os
import sys
from PyPDF2 import PdfFileReader
import epub
import glob


class Bibliotheque():
    def __init__(self, path) -> None:
        livres = glob.glob(f"{path}*")

        # livres_obj_pdf = [Livre(l) for l in livres if l.endswith(".pdf")]
        # for i in livres_obj_pdf:
        #     i._open_pdf()

        # print(livres_obj_pdf)

        livres_obj = [Livre(l) for l in livres]
        # for i in livres_obj_epub:
        #     i._open_epub()
        print(livres_obj)


class Livre():
    def __init__(self, file_name) -> None:
        self.file_name = file_name

        if file_name.endswith(".pdf"):
            self.auteur, self.titre = self._open_pdf()
        elif file_name.endswith(".epub"):
            self._open_epub()

        self.auteur = None
        self.titre = None

    def __repr__(self) -> str:
        return f"{self.titre} par {self.auteur}"

    def _open_pdf(self):
        with open(f'{self.file_name}', 'rb') as f:
            pdf = PdfFileReader(f)
            information = pdf.getDocumentInfo()
            number_of_pages = pdf.getNumPages()

        return information.author, information.title

    def _open_epub(self):
        with epub.open_epub(f'{self.file_name}') as book:
            metadata = book.opf.metadata
            auteur = metadata.creators[0][0]
            titre = metadata.titles[0][0]
            return auteur, titre


if __name__ == "__main__":
    args = sys.argv

    bibli = Bibliotheque("./livres/")
