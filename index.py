import os

def ajout_element(element,texte): #PERMET L'AJOUT DE PARAGRAPHE (le reste nécessite une autre fonction car pas adapter)
    choix = input("Ou voulez-vous ajouter votre élément ?")
    fd = open('index.html', 'r')
    oui = fd.readlines()
    fd.close()
    for i in range(len(oui)):
        if choix in oui[i]:
            print( oui[i])
            choix = input("Voulez vous ajouter un id à l'élément (cela permettra de le cibler plus facilement) ?")
            if choix == 'oui':
                identifiant = input("Entrez son identifiant :")
                oui.insert(i+1, '<{} id="{}">{}</{}>\n'.format(element,identifiant,texte,element))
            else:
                choix_classe = input("Voulez vous ajouter une class à l'élément (cela permettra de le cibler plus facilement) ?")
                if choix_classe == 'oui':
                    identifiant = input("Entrez sa classe :")
                    oui.insert(i+1, '<{} class="{}">{}</{}>\n'.format(element,identifiant, texte,element))
                else :
                    oui.insert(i+1, "<{}>{}</{}>\n".format(element,texte,element))
    fd = open('index.html', 'w')
    oui = "".join(oui)
    fd.write(oui)
    fd.close()

def ajout_menu(): #AJOUTE UN MENU MAIS SANS LES HYPERLIENS POUR L'INSTANT (nécessite une fonction pour créer les hyperliens)
    choix = input("Ou voulez-vous ajouter votre menu ? (préféré dans l'entete du site)")
    fd = open('index.html', 'r')
    oui = fd.readlines()
    fd.close()
    for i in range(len(oui)):
        if choix in oui[i]:
            print( oui[i])
            oui.insert(i+1, '<ul>\n')
            nombre = int(input("Combien voulez-vous de lien ? :"))
            for j in range(1,nombre+1):
                texte = input("Le nom de votre lien :")
                oui.insert(i+1+j, '<li>{}</li>\n'.format(texte))
            oui.insert(i+2+nombre, '</ul>\n')
    fd = open('index.html', 'w')
    oui = "".join(oui)
    fd.write(oui)
    fd.close()

    
def base_html(): #CREER LA STRUCTURE HTML DE BASE
    fd = open('index.html', 'w')
    fd.write("<!doctype html>\n\t<html lang='fr'>\n\t\t<head>\n\t\t\t<meta charset='utf-8'>\n\t\t\t<title>Titre de la page</title>\n\t\t\t<link rel='stylesheet' href='style.css'>\n\t\t\t<script src='script.js'></script>\n\t\t</head>\n\t\t<body>")
    fd.write("\n\t\t</body>\n\t</html>")
    fd.close()

if __name__ == '__main__':
    try:
        if os.stat("index.html").st_size == 0:
            base_html()
    except:
        base_html()