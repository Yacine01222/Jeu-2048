## JEU 2048 ##

#Djessim Bouiche
#Gabriel Levy
#Yacine Boulachgour
#Namsai Souvanthong

#### MODULES / BIBLIOTHEQUES 

import tkinter as tk
import random as rd

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
    update_labels()
    return

def bas():
    update_labels()
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



fenetre.mainloop()
