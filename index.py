import os
from tkinter import messagebox

def ajout_hyperlien(texte):
    choix = input('donnez votre URL')
    texte = '<a href="{}">{}</a>'.format(choix, texte)
    return texte

def ajout_element(element,texte, ciblage, identifiant=None, clas=None): #PERMET L'AJOUT DE <p> <span> <div> (nécessite l'intégration du <li>) (le reste nécessite une autre fonction car pas adapter)
    fd = open('web/index.html', 'r')
    dom = fd.readlines()
    fd.close()
    for i in range(len(dom)):
        if ciblage in dom[i]:
            print( dom[i])
            if identifiant and clas:
                dom.insert(i+1, '<{} id="{}" class="{}">{}</{}>\n'.format(element,identifiant,clas,texte,element))
                break
            if identifiant:
                dom.insert(i+1, '<{} id="{}">{}</{}>\n'.format(element,identifiant,texte,element))
                break
            else:
                if clas:
                    dom.insert(i+1, '<{} class="{}">{}</{}>\n'.format(element,clas, texte,element))
                    break
                else :
                    dom.insert(i+1, "<{}>{}</{}>\n".format(element,texte,element))
                    break
    fd = open('web/index.html', 'w')
    dom = "".join(dom)
    fd.write(dom)
    fd.close()

def ajout_menu(): #AJOUTE UN MENU MAIS SANS LES HYPERLIENS POUR L'INSTANT (nécessite une fonction pour créer les hyperliens)
    choix = print_where()
    fd = open('web/index.html', 'r')
    oui = fd.readlines()
    fd.close()
    for i in range(len(oui)):
        if choix in oui[i]:
            print( oui[i])
            oui.insert(i+1, '<ul>\n')
            nombre = int(input("Combien voulez-vous de lien ? :"))
            for j in range(1,nombre+1):
                texte = input("Le nom de votre lien :")
                texte = ajout_hyperlien(texte)
                oui.insert(i+1+j, '<li>{}</li>\n'.format(texte))
            oui.insert(i+2+nombre, '</ul>\n')
            break
    fd = open('web/index.html', 'w')
    oui = "".join(oui)
    fd.write(oui)
    fd.close()

def ajout_block(element):
    choix = print_where()
    fd = open('web/index.html', 'r')
    oui = fd.readlines()
    fd.close()
    for i in range(len(oui)):
        if choix in oui[i]:
            print(oui[i])
            choix2 = input("Voulez vous ajouter un id à l'élément (cela permettra de le cibler plus facilement) ?")
            if choix2 == 'oui':
                identifiant = input("Entrez son identifiant :")
                oui.insert(i+1, '<{} id="{}">\n'.format(element, identifiant))
            else:
                choix_classe = input("Voulez vous ajouter une class à l'élément (cela permettra de le cibler plus facilement) ?")
                if choix_classe == 'oui':
                    identifiant = input("Entrez sa classe :")
                    oui.insert(i+1, '<{} class="{}">\n'.format(element,identifiant))
                else:
                    oui.insert(i+1, '<{}>\n'.format(element))
            oui.insert(i+2, '</{}>\n'.format(element))
            break
    fd = open('web/index.html', 'w')
    oui = "".join(oui)
    fd.write(oui)
    fd.close()
    
def base_html(): #CREER LA STRUCTURE HTML DE BASE
    fd = open('web/index.html', 'w')
    fd.write("<!doctype html>\n\t<html lang='fr'>\n\t\t<head>\n\t\t\t<meta charset='utf-8'>\n\t\t\t<title>Titre de la page</title>\n\t\t\t<link rel='stylesheet' href='style.css'>\n\t\t\t<script src='script.js'></script>\n\t\t</head>\n\t\t<body>")
    fd.write("\n\t\t</body>\n\t</html>")
    fd.close()

