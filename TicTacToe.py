#!/usr/bin/python

from asyncio import streams
import numpy as np

class TicTacToe():
    def __init__(self) -> None:
        self.grille = [[".",".", "."],[".",".", "."],[".",".", "."]]

    def place(self, row ,col,c):
        if row <=3 and col <=3 and self.grille[row-1][col-1] == ".":
            self.grille[row-1][col-1] = c
        else:
            raise Exception("Emplacement non valide")

    def vainqueur(self):
        #On vérifie chaque ligne
        for i in range(3):
            first = ""
            win = True
            for j in range(3):
                if self.grille[i][j] == ".":
                    win = False
                    break
                elif first == "":
                    first = self.grille[i][j]
                elif first != self.grille[i][j]:
                    win = False
                    break
            
            if win:
                return first.nom

       #On vérifie chaque colonne
        for i in range(3):
            first = ""
            win = True
            for j in range(3):
                if self.grille[j][i] == ".":
                    win = False
                    break
                elif first == "":
                    first = self.grille[j][i]
                elif first != self.grille[j][i]:
                    win = False
                    break
            
            if win:
                return first.nom
        

        #On vérifie les deux diagonales
        if self.grille[0][0] == self.grille[1][1] and self.grille[0][0] == self.grille[2][2]:
            return self.grille[0][0].nom

        if self.grille[2][0] == self.grille[1][1] and self.grille[2][0] == self.grille[0][2]:
            return self.grille[2][0].nom

    def is_grille_pleine(self):
        for i in range(3):
            for j in range(3):
                if self.grille[i][j] == ".":
                    return False
        return True

    def __str__(self) -> str:
        l1 = " ".join(list(map(str, self.grille[0])))
        l2 = " ".join(list(map(str, self.grille[1])))
        l3 = " ".join(list(map(str, self.grille[2])))
        
        tableau = f"{l1}\n{l2}\n{l3}\n"
        return tableau

class Joueur():
    def __init__(self, jeu, nom, pion) -> None:
        self.jeu = jeu
        self.nom = nom
        self.pion = pion

    def joue(self, row, col):
        self.jeu.place(row,col,self)

    def __str__(self):
        return self.pion

if __name__ == "__main__":
    jeu = TicTacToe()
    bob = Joueur(jeu, "Bob", "X")
    alice = Joueur(jeu, "Alice", "O")
    
    print(jeu)
    bob.joue(3,1)
    alice.joue(1,2)
    bob.joue(2,2)
    alice.joue(1,1)
    bob.joue(1,3)
    print(jeu)
    print(jeu.vainqueur())