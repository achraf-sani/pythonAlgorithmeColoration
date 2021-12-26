import numpy as np

def coloration(mAdjacence):
    degSommets = {}
    for i in range(len(mAdjacence)):
        degSommets[i] = sum(mAdjacence[i])
    degSommetsTrié = sorted(degSommets.items(), key=lambda x: x[1], reverse=True)
    couleurs = [0 for i in range(len(degSommetsTrié))]

    nbr_couleur_actuelle = 1
    while sum([bool(c) for c in couleurs]) != len(degSommetsTrié):
        couleur_actuelle = "C" + str(nbr_couleur_actuelle)
        sommets_coloriés = []
        for k in range(len(couleurs)):
            if couleurs[k] == 0 and nonAdjacent(sommets_coloriés, degSommetsTrié[k][0], mAdjacence):
                couleurs[k] = couleur_actuelle
                sommets_coloriés.append(degSommetsTrié[k][0])
        nbr_couleur_actuelle += 1
    
    return degSommetsTrié, couleurs

def nonAdjacent(sommets_color, sommet, mAdjacence):
    estNonAdjacent = True
    for s in sommets_color:
        if mAdjacence[sommet][s] == 1:
            estNonAdjacent = False
    return estNonAdjacent

def uneRéalisation(coloration, sommets):
    degSommet, couleurs = coloration[0], coloration[1]
    print("Sommet" + " "*6 + "deg(sommet)" + " "*6 +"couleur")
    for i in range(len(couleurs)):
        sommet = sommets[degSommet[i][0]]
        deg_sommet = str(degSommet[i][1])
        couleur = couleurs[i]
        print(sommet.center(6), deg_sommet.rjust(11), couleur.rjust(14))






exemple2 = np.array([[0, 1, 1, 0, 0, 0, 1], 
                       [1, 0, 1, 1, 0, 0, 0], 
                       [1, 1, 0, 0, 1, 1, 1], 
                       [0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1, 0],
                       [0, 0, 1, 0, 1, 0, 1],
                       [1, 0, 1, 0, 0, 1, 0]])

sommets_exemple1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
exemple1 = np.array([[0, 1, 1, 0, 0, 0, 0], 
                       [1, 0, 0, 0, 0, 0, 0], 
                       [1, 0, 0, 1, 1, 0, 0], 
                       [0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 1, 1, 0, 1, 1],
                       [0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0]])

#print(coloration(exemple1))
uneRéalisation(coloration(exemple1), sommets_exemple1)

