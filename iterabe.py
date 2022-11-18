#!/usr/bin/python

class Itineraire():
    def __init__(self):
        self.chemin = []
        self.cur = 0

    def __getitem__(self, i):
        return self.chemin[i]

    def __len__(self):
        return len(self.chemin)

    def gauche(self, jusqua=0):
        self.chemin.append(('gauche', jusqua - self.cur))
        self.cur += jusqua

    def droite(self, jusqua=0):
        self.chemin.append(('droite', jusqua - self.cur))
        self.cur += jusqua


if __name__ == "__main__":
    mon_itineraire = Itineraire()
    mon_itineraire.gauche(jusqua=100)
    mon_itineraire.droite(jusqua=120)
    mon_itineraire.droite(jusqua=270)
    mon_itineraire.gauche(jusqua=500)
    mon_itineraire.gauche(jusqua=1080)

    for troncon in mon_itineraire:
        print(troncon)

