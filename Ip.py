#!/usr/bin/python

#Classe 3 256 adresses sur le réseau
#Classe 2 65536 adresses sur le réseau
#Classe 1 16777216 adresses sur le réseau


class IPV4():
    def __init__(self, ip) -> None:
        self.ip = ip
        splitted = ip.split(".")
        first = str(bin(int(splitted[0])))[2:]
        if len(first)==8 and first[:3] == "110":
            self.classe = "A"
            self.adresse = ".".join(splitted[1:])
            self.reseau = splitted[0]
        elif len(first) == 8 and first[:2] == "10":
            self.classe = "B"
            self.adresse = ".".join(splitted[2:])
            self.reseau = ".".join(splitted[:2])
        elif first[0] == "1":
            self.classe = "C"
            self.adresse = splitted[-1]
            self.reseau = ".".join(splitted[:3])
        else:
            raise Exception("Ip non valide")

    def __repr__(self) -> str:
        return f"{self.ip} : Classe={self.classe}, Réseau={self.reseau}, Adresse d'équipement={self.adresse}"

if __name__ == "__main__":
    ip = IPV4("10.0.0.1")
    print(ip)