import os


def ajout_element(element,texte, ciblage='body', identifiant=None, clas=None): #PERMET L'AJOUT DE <p> <span> <div> (nécessite l'intégration du <li>) (le reste nécessite une autre fonction car pas adapter)
    fd = open('web/index.html', 'r')
    dom = fd.readlines()
    fd.close()
    for i in range(len(dom)):
        if ciblage in dom[i]:
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

def ajout_menu(nb_puce, varLien, ciblage='body'): #AJOUTE UN MENU MAIS SANS LES HYPERLIENS POUR L'INSTANT (nécessite une fonction pour créer les hyperliens)
    fd = open('web/index.html', 'r')
    dom = fd.readlines()
    fd.close()
    nb_puce = int(nb_puce)
    for i in range(len(dom)):
        if ciblage in dom[i]:
            dom.insert(i+1, '<ul>\n')
            for j in range(1,nb_puce+1):
                texte = '<a href="{}">{}</a>'.format(varLien[1][j-1], varLien[0][j-1])
                dom.insert(i+1+j, '<li>{}</li>\n'.format(texte))
            dom.insert(i+2+nb_puce, '</ul>\n')
            break
    fd = open('web/index.html', 'w')
    dom = "".join(dom)
    fd.write(dom)
    fd.close()

def ajout_block(element, ciblage='body', identifiant=None, clas=None):
    fd = open('web/index.html', 'r')
    dom = fd.readlines()
    fd.close()
    for i in range(len(dom)):
        if ciblage in dom[i]:
            if identifiant and clas:
                dom.insert(i+1, '<{} id="{}" class="{}">\n'.format(element,identifiant,clas))
                break
            if identifiant:
                dom.insert(i+1, '<{} id="{}">\n'.format(element,identifiant))
                break
            else:
                if clas:
                    dom.insert(i+1, '<{} class="{}">\n'.format(element,clas))
                    break
                else:
                    dom.insert(i+1, '<{}>\n'.format(element))
                    break
    dom.insert(i+2, '\n</{}>\n'.format(element))
    fd = open('web/index.html', 'w')
    dom = "".join(dom)
    fd.write(dom)
    fd.close()
    
def base_html(): #CREER LA STRUCTURE HTML DE BASE
    fd = open('web/index.html', 'w')
    fd.write("<!doctype html>\n\t<html lang='fr'>\n\t\t<head>\n\t\t\t<meta charset='utf-8'>\n\t\t\t<title>Titre de la page</title>\n\t\t\t<link rel='stylesheet' href='style.css'>\n\t\t\t<script src='script.js'></script>\n\t\t</head>\n\t\t<body>")
    fd.write("\n\t\t</body>\n\t</html>")
    fd.close()

