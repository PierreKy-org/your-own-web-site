from tkinter import Tk, Button, Entry, Label, messagebox, Radiobutton, StringVar, Scrollbar, Text, Frame, Toplevel
from functools import partial
from threading import Thread
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import index

choix = ['p', 'h1', 'h2']
choixStr = ['Paragraphe', 'Titre principale', 'Titre']

choixB = ['nav','div','section','article']
choixBlock = ['Navigation', 'Balise basique', 'Section', 'Article']
if not os.path.isdir('web'):
    os.mkdir('web')
    index.base_html()
else :
    if os.path.isfile("web/index.html"):
        if os.stat("web/index.html").st_size == 0:
            index.base_html()
    else:
        index.base_html()
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        Web.driver.close()

def raise_frame(frame):
    frame.tkraise()

def verif(provenance):
    if provenance == 'block':
        if varGr2.get():
            raise_frame(fenCiblage)
            retour = Button(fenCiblage, text='Retour', command=partial(raise_frame, fenAjoutBlock))
            retour.grid(column=0,row=0)
        else:
            messagebox.showwarning("Champ vide", "Veuillez choisir un type d'élément et son contenu !")
    if provenance == 'menu':
        if nombre_puce.get() in '123456789' and nombre_puce.get() != '':
            raise_frame(fenCiblage)
            retour = Button(fenCiblage, text='Retour', command=partial(raise_frame, fenMenu))
            retour.grid(column=0,row=0)
        else:
            messagebox.showwarning("Champ incorrect", "Veuillez choisir un nombre !")
    if provenance == 'element':
        if varGr.get() and comment.get(1.0, "end-1c"):
            raise_frame(fenCiblage)
            retour = Button(fenCiblage, text='Retour', command=partial(raise_frame, fenAjoutElement))
            retour.grid(column=0,row=0)
        else:
            messagebox.showwarning("Champ vide", "Veuillez choisir un type d'élément et son contenu !")
    valider = Button(fenCiblage, text='Valider', command=partial(Web.enter_click, provenance))
    valider.grid(column=1,row=13)

def ajoutListe(liste):
    liste[0].append(textePuce.get())
    liste[1].append(adresse.get())
    
    textePuce.delete(0, 100)
    adresse.delete(0, 100)
    acc = len(liste[0])
    if acc >= int(nombre_puce.get()):
        validePuce = Button(fenLien, text='Fini !', command=partial(Web.enter_click, 'menu2'))
        validePuce.grid(column=4,row=4, pady=20, padx=180)
        fenLien.update()

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
    def run(self):
        chrome_options = Options()
        html_file = os.getcwd() + "//" + "web/index.html"
        chrome_options.add_argument("--app=file:///" + html_file)
        chrome_options.add_argument("--window-size=600,539")
        chrome_options.add_argument("--window-position=701,100")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        assert "No results found." not in self.driver.page_source
        
    def enter_click(self, provenance):
        raise_frame(base)
        if ciblage.get(1.0, "end-1c") == '':
            cible = 'body'
        else :
            cible = ciblage.get(1.0, "end-1c")
        if provenance == 'element':
            index.ajout_element(varGr.get(),comment.get(1.0, "end-1c"), cible, identifiant.get(), clas.get())
            ciblage.delete(1.0, "end-1c")
            cible = 'body'
        if provenance == 'block':
            index.ajout_block(varGr2.get(), cible, identifiant.get(), clas.get())
            ciblage.delete(1.0, "end-1c")
            cible = 'body'
        if provenance == 'menu':
            raise_frame(fenLien)
        if provenance == 'menu2':
            global globalLien
            index.ajout_menu(nombre_puce.get(), globalLien, cible)
            globalLien = [list(), list()]
            validePuce = Button(fenLien, text='Valider', command=partial(ajoutListe, globalLien))
            validePuce.grid(column=4,row=4, pady=20, padx=180)
            ciblage.delete(1.0, "end-1c")
            cible = 'body'
        self.driver.refresh()
        comment.delete(1.0, "end-1c")


Web = ViewHtml()
global globalLien
globalLien = [list(), list()]
root = Tk()

base = Frame(root)
fenCiblage = Frame(root)
fenAjoutElement = Frame(root)
fenAjoutBlock = Frame(root)
fenMenu = Frame(root)
fenLien = Frame(root)

for frame in (base, fenCiblage, fenAjoutElement, fenAjoutBlock, fenMenu, fenLien):
    frame.grid(row=0, column=0, sticky='news')


Web.start()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("700x500+0+100")
root.propagate(0)
root.title('Your own web site')

#MENU PRINCIPALE
qb = Button(base, text='Quitter', command=partial(on_closing))
qb.grid(column=0,row=0)

ajoutElem = Button(base, text='Ajouter un élément', command=partial(raise_frame, fenAjoutElement))
ajoutElem.grid(column=1,row=1, padx =20)

ajoutBlock = Button(base, text='Ajouter un block', command=partial(raise_frame, fenAjoutBlock))
ajoutBlock.grid(column=2,row=1, padx =20)

ajoutMenu = Button(base, text='Ajouter un menu', command=partial(raise_frame, fenMenu))
ajoutMenu.grid(column=3,row=1, padx =20)

















#FENETRE AJOUT MENU

qb = Button(fenMenu, text='Retour au menu', command=partial(raise_frame, base))
qb.grid(column=0,row=0)

textPuce = Label(fenMenu, text="Entrer le nombre de lien que votre menu comporte :")
textPuce.grid(column=1,row=0)

nombre_puce = Entry(fenMenu)
nombre_puce.grid(column=1,row=1)

validePuce = Button(fenMenu, text='Valider', command=partial(verif, 'menu'))
validePuce.grid(column=8,row=9, pady=20, padx=180)









#FENETRE AJOUT LIEN

qb = Button(fenLien, text='Retour au menu', command=partial(raise_frame, fenMenu))
qb.grid(column=0,row=0)


textLien = Label(fenLien, text="Entrer le texte et son lien :")
textLien.grid(column=1,row=0)

textePuce = Entry(fenLien)
textePuce.grid(column=1,row=1)

adresse = Entry(fenLien)
adresse.grid(column=2,row=1)

validePuce = Button(fenLien, text='Valider', command=partial(ajoutListe, globalLien))
validePuce.grid(column=4,row=4, pady=20, padx=180)


















#FENETRE D'AJOUT D'ELEMENT
qb = Button(fenAjoutElement, text='Retour au menu', command=partial(raise_frame, base))
qb.grid(column=0,row=0)

text = Label(fenAjoutElement, text="Choisisser l'élément à ajouter sur votre site : ")
text.grid(column=0,row=1, columnspan=4, pady=50)

varGr = StringVar()
for i in range(len(choix)):
    b = Radiobutton(fenAjoutElement, variable=varGr,text=choixStr[i], value=choix[i], tristatevalue="x")
    b.grid(column=1,row=i+2)

text1 = Label(fenAjoutElement, text="Entrer le texte que possèdera l'élément : ")
text1.grid(column=5,row=1, columnspan=4)

comment = Text(fenAjoutElement, height=7, width=30)
comment.grid(column=5,row=2,columnspan=4, rowspan = 5)

retourLigne = Button(fenAjoutElement, text='Retour à la ligne', command=partial(comment.insert, "end-1c", '</br>'))
retourLigne.grid(column=1,row=9)


valide = Button(fenAjoutElement, text='Valider', command=partial(verif, 'element'))
valide.grid(column=8,row=9, pady=20, padx=180)













#FENETRE AJOUT BLOCK
qb = Button(fenAjoutBlock, text='Retour au menu', command=partial(raise_frame, base))
qb.grid(column=0,row=0)

text = Label(fenAjoutBlock, text="Choisisser l'élément à ajouter sur votre site : ")
text.grid(column=0,row=1, columnspan=4, pady=50)

varGr2 = StringVar()
for i in range(len(choix)):
    b = Radiobutton(fenAjoutBlock, variable=varGr2,text=choixBlock[i], value=choixB[i], tristatevalue="x")
    b.grid(column=1,row=i+2)

valide = Button(fenAjoutBlock, text='Valider', command=partial(verif, 'block'))
valide.grid(column=8,row=9, pady=20, padx=180)









#FENETRE DE CIBLAGE

textCiblage = Label(fenCiblage, text="Entrer le texte d'un élément ou son id/class (votre texte sera juste en dessous) : ")
textCiblage.grid(column=0,row=1, columnspan=4, pady = 20)

ciblage = Text(fenCiblage, height=7, width=30)
ciblage.grid(column=0,row=2,columnspan=4, rowspan = 5)

textId = Label(fenCiblage, text="**Optionnel** Entrer un identifiant (cela permet de trouver votre élément plus facilement) : ")
textId.grid(column=0,row=9)

identifiant = Entry(fenCiblage)
identifiant.grid(column=0,row=10)

textClass = Label(fenCiblage, text="**Optionnel** Entrer une class (cela permet de trouver votre élément plus facilement) : ")
textClass.grid(column=0,row=11)

clas = Entry(fenCiblage)
clas.grid(column=0,row=12)



raise_frame(base)
root.mainloop()


