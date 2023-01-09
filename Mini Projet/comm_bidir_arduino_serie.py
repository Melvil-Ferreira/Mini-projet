 #!/usr/bin/env python3

import time

def read_mode():
    with open("mode.txt") as f:
        mode = f.read()
    return mode

def read_old_etat_lampadaire():
    with open("old_mode.txt") as f:
        old_mode = f.read()
    return old_mode

def read_forcage_lampadaire():
    with open("lampadaire.txt") as l:
        lampadaire = l.read()
    return lampadaire

numero_lampadaire_1 = read_forcage_lampadaire().split(".")[0]
numero_lampadaire_2 = read_forcage_lampadaire().split(".")[2]
numero_lampadaire_3 = read_forcage_lampadaire().split(".")[4]
numero_lampadaire_4 = read_forcage_lampadaire().split(".")[6]

etat_lampadaire_1 = read_forcage_lampadaire().split(".")[1]
etat_lampadaire_2 = read_forcage_lampadaire().split(".")[3]
etat_lampadaire_3 = read_forcage_lampadaire().split(".")[5]
etat_lampadaire_4 = read_forcage_lampadaire().split(".")[7]

#def write_etat_lampadaire(etat):
 #   with open("lampadaire.txt", "w") as l:
  #      l.write(read_numero_lampadaire() + "," + 'test')


while True:

    if read_forcage_lampadaire != read_old_etat_lampadaire():
        print("Lampadaire {} est {}" .format(numero_lampadaire_1,etat_lampadaire_1))
        # envoyer numero_lampadaire_1 et etat_lampadaire_1 à l'arduino
        # envoyer numero_lampadaire_2 et etat_lampadaire_2 à l'arduino
        # envoyer numero_lampadaire_3 et etat_lampadaire_3 à l'arduino
        # envoyer numero_lampadaire_4 et etat_lampadaire_4 à l'arduino
        # sur l'arduino faire en sorte que le microcontrôleur change l'état de chaque lampadaire inivduellement

    read_mode()
    read_forcage_lampadaire()

    mode = read_mode()

    print("Lampadaire {} est {}" .format(numero_lampadaire_1,etat_lampadaire_1))
    print("Lampadaire {} est {}" .format(numero_lampadaire_2,etat_lampadaire_2))
    print("Lampadaire {} est {}" .format(numero_lampadaire_3,etat_lampadaire_3))
    print("Lampadaire {} est {}" .format(numero_lampadaire_4,etat_lampadaire_4))

    if mode == "Standard":
        print("Mode standard")
        #envoyer l'instruction à l'arduino de changer le mode d'éclairage

    elif mode == "eco-securite":
        print("Mode éco-sécurité")
        #envoyer l'instruction à l'arduino de changer le mode d'éclairage

    elif mode == "extreme":
        print("Mode extrême")
        #envoyer l'instruction à l'arduino de changer le mode d'éclairage

    elif mode == "Mode alerte":
        print("Mode alerte")
        #envoyer l'instruction à l'arduino de changer le mode d'éclairage

    else:
        print("Mode inconnu" + mode)

    time.sleep(1)