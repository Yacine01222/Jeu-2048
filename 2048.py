## JEU 2048 ##

#Djessim Bouiche
#Gabriel Levy
#Yacine Boulachgour
#Namsai Souvanthong

#### MODULES / BIBLIOTHEQUES 
import tkinter as tk
import random as rd
import tkinter as tk

TAILLE_CASE = 100

def gauche():
    for i in range(4): # une boucle qui décale tant que c'est possible 
        for y in range(4): 
            for x in range(3, 0, -1):
                carre = liste_carre[x + y * 4]
                voisine = liste_carre[x + y * 4 - 1]
                if carre["valeur"] == voisine["valeur"] or voisine["valeur"] == 0: 
                    voisine["valeur"] += carre["valeur"]
                    carre["valeur"] = 0
    
    turn()
    return

def droite():
    turn()
    return

def haut():
    turn()
    return

def bas():
    turn()
    return

# Choisir de manière aléatoire une case vide 
def get_random_free_cell():
    case_libre = []
    for carre in liste_carre:
        if carre["valeur"]==0:
            case_libre.append(carre)
    
    return case_libre[rd.randint(0, len(case_libre) - 1)]

# permet de vérifier si toutes les cases sont remplies 
def is_complete_grid() -> bool:
    for carre in liste_carre:
        if carre["valeur"] == 0:
            return False
        
    return True

# permet de mettre à jour les cases 
def update_labels(): 
    for carre in liste_carre:
        if carre["valeur"] < 2:
            carre["label"].config(text = str(""))
        else:
            carre["label"].config(text = str(carre["valeur"]))

# permet d'initialiser le jeu
def start():
    init_grid()
    get_random_free_cell()["valeur"] = 2
    get_random_free_cell()["valeur"] = 2
    update_labels()

# permet de générer la grille
def init_grid():
    """Dessiner le carré avec des dimensions de taille_case*taille_case pixels pour chaque case"""
    for y in range(4):
        for x in range(4):
            canvas.create_rectangle(x * TAILLE_CASE, y * TAILLE_CASE, (y+1) * TAILLE_CASE, (x+1) * TAILLE_CASE)
            text_carre = tk.Label(canvas, font = ("Arial",64),fg = "white")
            liste_carre.append({
                "valeur": 0,
                "label": text_carre
            })
            text_carre.place(x=x * TAILLE_CASE + 1, y=y * TAILLE_CASE + 1, width=TAILLE_CASE -2 , height=TAILLE_CASE -2)


#effectue un tour de jeux 
def turn():
    if is_complete_grid() == False:
        get_random_free_cell()["valeur"] = 2

    update_labels() #mise à jour d'affichage 


fenetre = tk.Tk()
fenetre.title('2048')
label_title = tk.Label(fenetre, text = "2048", font = ("Arial", 20), bg = "#df9d97", fg = "white")
label_title.pack()

fenetre.geometry("800x800") 


canvas = tk.Canvas(fenetre, width=395, height=395, borderwidth=2, relief="solid")
liste_carre = []

# Boutons
left_button = tk.Button(fenetre, text="←", fg = "black", font=("Arial","15"),command= gauche)
right_button = tk.Button(fenetre, text="→", fg = "black", font=("Arial","15"),command = droite)
up_button = tk.Button(fenetre, text="↑",  fg = "black", font=("Arial","15"),command=haut)
down_button = tk.Button(fenetre, text="↓", fg = "black", font=("Arial","15"),command=bas)

left_button.place(relx=0.80, rely=0.5, anchor="center")
right_button.place(relx=0.90, rely=0.5, anchor="center")
up_button.place(relx=0.85, rely=0.42, anchor="center")
down_button.place(relx=0.85, rely=0.58, anchor="center")

# Ajouter le canevas à la fenêtre
canvas.pack(expand=True)

#Initailisation du score
score = 0

#afficher label score 
score_label = tk.Label(fenetre, text="Score : " + str(score), font = ("helvetica", "20"))
score_label.pack()
start()

fenetre.mainloop()