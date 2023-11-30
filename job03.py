import time

def regler_alarme(heure_alarme):
    while True:
        heure_actuelle = time.localtime(time.time())
        if heure_actuelle.tm_hour == heure_alarme[0] and heure_actuelle.tm_min == heure_alarme[1] and heure_actuelle.tm_sec == heure_alarme[2]:
            print("Alarme ! L'heure est arrivée.")
            break
        else:
            print(f"En attente de l'heure de l'alarme. Heure actuelle : {heure_actuelle.tm_hour}:{heure_actuelle.tm_min}:{heure_actuelle.tm_sec}")
            time.sleep(1)

heure_alarme = (10, 42, 0)
regler_alarme(heure_alarme)
