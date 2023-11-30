from tkinter import *
from time import *

current_time = None

def update():
    global current_time
    if current_time is not None:
        time_string = strftime("%I:%M:%S %p", current_time)
        time_label.config(text=time_string)
    time_label.after(1000, update)

def afficher_heure(heure):
    global current_time
    current_time = heure
    time_string = "{:02d}:{:02d}:{:02d}".format(heure[0], heure[1], heure[2])
    time_label.config(text=time_string)
    sleep(1000)

window = Tk()

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack()

update()

# Exemple d'utilisation de la fonction afficher_heure avec un tuple (heures, minutes, secondes)
heure_a_afficher = (12, 30, 47)
afficher_heure(heure_a_afficher)

window.mainloop()
