## JEU 2048 ##

#Djessim Bouiche
#Gabriel Levy
#Yacine Boulachgour
#Namsai Souvanthong

#### MODULES / BIBLIOTHEQUES 

import tkinter as tk
import random as rd
from tkinter import messagebox

taille_case = 100

#### PARTIE INTERFACE #####

import tkinter as tk


fenetre = tk.Tk()
fenetre.title('2048')
label_title = tk.Label(fenetre, text = "2048", font = ("Arial", 20), bg = "#df9d97", fg = "white")
label_title.pack()

fenetre.geometry("800x800") 


canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")

taille_case = 100
liste_carre = []

def draw(): 
    """Dessiner le carré avec des dimensions de taille_casextaille_case pixels pour chaque case"""
    for i in range(4):
        for j in range(4):
            canvas.create_rectangle(i*taille_case, j*taille_case, (i+1)*taille_case, (j+1)*taille_case)
            text_carre = tk.Label(canvas, font = ("Arial",64),fg = "white")
            liste_carre.append({
                "x":i, 
                "y":j,
                "valeur":0,
                "label": text_carre
            })
            text_carre.place(x=i*taille_case + 1, y=j*taille_case + 1,width = taille_case -2 , height=taille_case -2)



def gauche():
    update_labels()
    return

def droite():
    update_labels()
    return

def haut():
    "Déplace toutes les tuiles vers le bas et fusionner si nécessaire."
    global liste_carre_disponible

    for colonne in range(4):
        nouvelle_colonne = [liste_carre_disponible[ligne * 4 + colonne][2] for ligne in range(4) if liste_carre_disponible[ligne * 4 + colonne][2] != 0]
        nouvelle_colonne = [0] * (4 - len(nouvelle_colonne)) + nouvelle_colonne

        for ligne in range(3, 0, -1):
            if nouvelle_colonne[ligne] == nouvelle_colonne[ligne - 1] and nouvelle_colonne[ligne] != 0:
                nouvelle_colonne[ligne] *= 2
                nouvelle_colonne[ligne - 1] = 0

        nouvelle_colonne = [0] * (4 - len([valeur for valeur in nouvelle_colonne if valeur != 0])) + [valeur for valeur in nouvelle_colonne if valeur != 0]

        for ligne in range(4):
            liste_carre_disponible[ligne * 4 + colonne][2] = nouvelle_colonne[ligne]

    update_canvas()
    return

def bas():
    """Déplace toutes les tuiles vers le haut et gère les fusions."""
    global liste_carre_disponible

    for colonne in range(4):
        nouvelle_colonne = [liste_carre_disponible[ligne * 4 + colonne][2] for ligne in range(4) if liste_carre_disponible[ligne * 4 + colonne][2] != 0]
        nouvelle_colonne += [0] * (4 - len(nouvelle_colonne))

        for ligne in range(3):
            if nouvelle_colonne[ligne] == nouvelle_colonne[ligne + 1] and nouvelle_colonne[ligne] != 0:
                nouvelle_colonne[ligne] *= 2
                nouvelle_colonne[ligne + 1] = 0

        nouvelle_colonne = [valeur for valeur in nouvelle_colonne if valeur != 0]
        nouvelle_colonne += [0] * (4 - len(nouvelle_colonne))

        for ligne in range(4):
            liste_carre_disponible[ligne * 4 + colonne][2] = nouvelle_colonne[ligne]

    update_canvas()
    return

def get_random_free_cell():
    case_libre = []
    for carre in liste_carre:
        if carre["valeur"]==0:
            case_libre.append(carre)
    return case_libre[rd.randint(0,len(case_libre))]

# permet de mettre à jour les cases 
def update_labels(): 
    for carre in liste_carre:
        if carre["valeur"] < 2:
            carre["label"].config(text = str(""))
        else:
            carre["label"].config(text = str(carre["valeur"]))

def start():
    get_random_free_cell()["valeur"] = 2
    get_random_free_cell()["valeur"] = 2
    update_labels()

# Boutons
left_button = tk.Button(fenetre, text="←", fg = "black", font=("Arial","15"),command= gauche)  #command=gauche
right_button = tk.Button(fenetre, text="→", fg = "black", font=("Arial","15"),command = droite) #command=droite
up_button = tk.Button(fenetre, text="↑",  fg = "black", font=("Arial","15"),command=haut) #command=haut
down_button = tk.Button(fenetre, text="↓", fg = "black", font=("Arial","15"),command=bas)#command=bas

left_button.place(relx=0.80, rely=0.5, anchor="center")   # command = gauche
right_button.place(relx=0.90, rely=0.5, anchor="center")  # command = droite
up_button.place(relx=0.85, rely=0.42, anchor="center")    # command = haut
down_button.place(relx=0.85, rely=0.58, anchor="center")  #command = bas


draw() #appelle la fonction qui dessine les cases

start()
# Ajouter le canevas à la fenêtre
canvas.pack(expand=True)

liste_carre_disponible = [[i,j,0] for i in range(4) for j in range(4)]

#Initailisation du score
score = 0
check = 0
#List stockant les carrés
liste_carre = []
liste_carre_disponible = [] # pas le bon nom -> tous les carrés de la grille

#afficher label score 
#Afficher le score
score_label = tk.Label(fenetre, text="Score : " + str(score), font = ("helvetica", "20"))
score_label.pack()

#augmenter le score 
def augmenter_score():
    global score
    score_label.config(text="Score : " + str(score))

def update_canvas():
#Fonction pour mettre à jour la grille et fusionner les case
    global canvas
    global liste_carre_disponible
    global colors
    
    canvas.delete("all") # supprime tout les éléments concernés pour canva
    
    for i in range(4):
        #parcours les 4 lignes et colonnes de la grille,x0 y0 : coin haut gauche du carré,x1 y1 coin bas droit du carré,valeur permet de trouver la valeur dans la case dispo
        for j in range(4):
            x0 = j * taille_case
            y0 = i * taille_case
            x1 = x0 + taille_case
            y1 = y0 + taille_case
            valeur = liste_carre_disponible[i*4+j][2]
            couleur = colors.get(valeur, "#FFFFFF")
            canvas.create_rectangle(x0, y0, x1, y1, fill=couleur, outline="#000000")
            if valeur != 0:
                canvas.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(valeur), font=("Courrier", 20, "bold"))
        
    canvas.pack()

#Initialisation de la liste des carrés disponibles
def chiffre_dans_une_case():
#Fonction qui ajoute une case(tuile) aléatoirement
    global liste_carre_disponible
    global liste_carre
    #n = nb de cases dispo
    #cases vide contient les indices des cases vides
    n = len(liste_carre_disponible)
    cases_vides = []
    
    for i in range(n):
        if liste_carre_disponible[i][2] == 0:
            cases_vides.append(i)
        

    if cases_vides:
        index = rd.choice(cases_vides)
        i, j = liste_carre_disponible[index][:2]
        valeur = rd.choice([2, 2 , 2 , 2 , 2 , 2 , 2 , 2 , 4])
        #rd.choice choisit case vide au hasard, on récupère alors l'indice de la case, 90% de chance d'avoir un 2 10% d'avoir un 4

        liste_carre_disponible[index][2] = valeur
            #on choisit un carré(=rectangle particulier mais rectangle qd meme,o, affiche le nombre ds la case, on stock ces 2 objets dans une liste : liste carre
        carre = canvas.create_rectangle(j*taille_case, i*taille_case, (j+1)*taille_case, (i+1)*taille_case, fill=colors[valeur], outline="#000000")
        carre_texte = canvas.create_text(j*taille_case + taille_case/2, i*taille_case + taille_case/2, text=str(valeur), font=("Courrier", 20, "bold"))
        liste_carre.append((carre, carre_texte))
            #len case_vide==1 veut dire que c la dernière case vide, donc plus de case/tuile ne peut etre ajoutée

        if len(cases_vides) == 1:
            messagebox.showinfo("2048", "Partie terminée \nVotre score est de : {}".format(score))
            relancer()

# relancer la partie avec la fonction relancer
def relancer():
    """Permet de relancer la partie"""
    global liste_carre_disponible
    global score
    score = 0
    augmenter_score()
    liste_carre_disponible = [[i,j,0] for i in range(4) for j in range(4)]
    #on réinitialise la liste de carré dispo

    update_canvas()
    chiffre_dans_une_case()

fenetre.mainloop()
