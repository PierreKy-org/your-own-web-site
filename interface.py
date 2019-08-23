from tkinter import Tk, Button, Entry, Label, messagebox, Radiobutton, StringVar, Scrollbar, Text, Frame, Toplevel
from functools import partial
from threading import Thread
import os
import time
import index
import webview
import functionCss

global lienSansListe
global globalLien
globalLien = [list(), list()]
choix = ['p', 'h1', 'h2', 'li']
choixStr = ['Paragraphe', 'Titre principale', 'Titre', 'Puce liste']

choixB = ['nav','div','section','article']
choixBlock = ['Navigation', 'Balise basique', 'Section', 'Article']

if not os.path.isdir('web'):
    os.mkdir('web')
    index.base_html()
    functionCss.addCss()
else :
    if os.path.isfile("web/index.html"):
        if os.stat("web/index.html").st_size == 0:
            index.base_html()
            functionCss.addCss()
    else:
        index.base_html()
        functionCss.addCss()

def raise_frame(frame):
    frame.tkraise()
def letgo():
    Web = ViewHtml()
    Web.start()


class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
    def run(self):
        self.root = Tk()

        self.base = Frame(self.root)
        self.fenCiblage = Frame(self.root)
        self.fenAjoutElement = Frame(self.root)
        self.fenAjoutBlock = Frame(self.root)
        self.fenMenu = Frame(self.root)
        self.fenLien = Frame(self.root)
        self.fenCss = Frame(self.root)

        
        for frame in (self.base, self.fenCiblage, self.fenAjoutElement, self.fenAjoutBlock, self.fenMenu, self.fenLien, self.fenCss):
            frame.grid(row=0, column=0, sticky='news')

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.geometry("700x500+0+100")
        self.root.propagate(0)
        self.root.title('Your own web site')


                #MENU PRINCIPALE
        self.qb = Button(self.base, text='Quitter', command=partial(self.on_closing))
        self.qb.grid(column=0,row=0)

        self.ajoutElem = Button(self.base, text='Ajouter un élément', command=partial(raise_frame, self.fenAjoutElement))
        self.ajoutElem.grid(column=1,row=1, padx =20)

        self.ajoutBlock = Button(self.base, text='Ajouter un block', command=partial(raise_frame, self.fenAjoutBlock))
        self.ajoutBlock.grid(column=2,row=1, padx =20)

        self.ajoutMenu = Button(self.base, text='Ajouter un menu', command=partial(raise_frame, self.fenMenu))
        self.ajoutMenu.grid(column=3,row=1, padx =20)

        self.css = Button(self.base, text='Ajouter du CSS', command=partial(raise_frame, self.fenCss))
        self.css.grid(column=4,row=1, padx =20)













        #FENETRE CSS

        self.qbcss = Button(self.fenCss, text='Retour au menu', command=partial(raise_frame, self.base))
        self.qbcss.grid(column=0,row=0)

        self.textcss = Label(self.fenCss, text="Entrer l'élément à personnaliser (cela peut aussi être un block, un id ou une class !) :")
        self.textcss.grid(column=1,row=0, columnspan=5)

        self.cibleCss = Entry(self.fenCss)
        self.cibleCss.grid(column=1,row=1)

        self.validecss = Button(self.fenCss, text='Valider', command=partial(self.verif, 'css'))
        self.validecss.grid(column=5,row=4, pady=20)












        #FENETRE AJOUT MENU

        self.qbmenu = Button(self.fenMenu, text='Retour au menu', command=partial(raise_frame, self.base))
        self.qbmenu.grid(column=0,row=0)

        self.textPuce = Label(self.fenMenu, text="Entrer le nombre de lien que votre menu comporte :")
        self.textPuce.grid(column=1,row=0)

        self.nombre_puce = Entry(self.fenMenu)
        self.nombre_puce.grid(column=1,row=1)

        self.validePuce = Button(self.fenMenu, text='Valider', command=partial(self.verif, 'menu'))
        self.validePuce.grid(column=8,row=9, pady=20, padx=180)









        #FENETRE AJOUT LIEN



        self.textLien = Label(self.fenLien, text="Entrer le texte et son lien :")
        self.textLien.grid(column=1,row=0)

        self.textePuce = Entry(self.fenLien)
        self.textePuce.grid(column=1,row=1)

        self.adresse = Entry(self.fenLien)
        self.adresse.grid(column=2,row=1)

        self.validePuce = Button(self.fenLien, text='Valider', command=partial(self.ajoutListe, globalLien))
        self.validePuce.grid(column=4,row=4, pady=20, padx=180)


















        #FENETRE D'AJOUT D'ELEMENT
        self.qbelem = Button(self.fenAjoutElement, text='Retour au menu', command=partial(raise_frame, self.base))
        self.qbelem.grid(column=0,row=0)

        self.text = Label(self.fenAjoutElement, text="Choisisser l'élément à ajouter sur votre site : ")
        self.text.grid(column=0,row=1, columnspan=4, pady=50)

        self.varGr = StringVar()
        for i in range(len(choix)):
            self.b = Radiobutton(self.fenAjoutElement, variable=self.varGr,text=choixStr[i], value=choix[i], tristatevalue="x")
            self.b.grid(column=1,row=i+2)

        self.text1 = Label(self.fenAjoutElement, text="Entrer le texte que possèdera l'élément : ")
        self.text1.grid(column=5,row=1, columnspan=4)

        self.comment = Text(self.fenAjoutElement, height=7, width=30)
        self.comment.grid(column=5,row=2,columnspan=4, rowspan = 5)

        self.retourLigne = Button(self.fenAjoutElement, text='Retour à la ligne', command=partial(self.comment.insert, "end-1c", '</br>'))
        self.retourLigne.grid(column=1,row=9)

        self.ajoutLienElem = Button(self.fenAjoutElement, text='Ajoute un lien', command=partial(self.verif, 'lien'))
        self.ajoutLienElem.grid(column=2,row=9)


        self.valide = Button(self.fenAjoutElement, text='Valider', command=partial(self.verif, 'element'))
        self.valide.grid(column=8,row=9, pady=20, padx=180)













        #FENETRE AJOUT BLOCK
        self.qbblock = Button(self.fenAjoutBlock, text='Retour au menu', command=partial(raise_frame, self.base))
        self.qbblock.grid(column=0,row=0)

        self.textblock = Label(self.fenAjoutBlock, text="Choisisser l'élément à ajouter sur votre site : ")
        self.textblock.grid(column=0,row=1, columnspan=4, pady=50)

        self.varGr2 = StringVar()
        for i in range(len(choix)):
            self.c = Radiobutton(self.fenAjoutBlock, variable=self.varGr2,text=choixBlock[i], value=choixB[i], tristatevalue="x")
            self.c.grid(column=1,row=i+2)

        self.validee = Button(self.fenAjoutBlock, text='Valider', command=partial(self.verif, 'block'))
        self.validee.grid(column=8,row=9, pady=20, padx=180)









        #FENETRE DE CIBLAGE

        self.textCiblage = Label(self.fenCiblage, text="Entrer le texte d'un élément ou son id/class (votre texte sera juste en dessous) : ")
        self.textCiblage.grid(column=0,row=1, columnspan=4, pady = 20)

        self.ciblage = Text(self.fenCiblage, height=7, width=30)
        self.ciblage.grid(column=0,row=2,columnspan=4, rowspan = 5)

        self.textId = Label(self.fenCiblage, text="**Optionnel** Entrer un identifiant (cela permet de trouver votre élément plus facilement) : ")
        self.textId.grid(column=0,row=9)

        self.identifiant = Entry(self.fenCiblage)
        self.identifiant.grid(column=0,row=10)

        self.textClass = Label(self.fenCiblage, text="**Optionnel** Entrer une class (cela permet de trouver votre élément plus facilement) : ")
        self.textClass.grid(column=0,row=11)

        self.clas = Entry(self.fenCiblage)
        self.clas.grid(column=0,row=12)



        raise_frame(self.base)
        self.root.mainloop()

    def enter_click(self, provenance):
        raise_frame(self.base)
        if self.ciblage.get(1.0, "end-1c") == '':
            cible = 'body'
        else :
            cible = self.ciblage.get(1.0, "end-1c")
        if provenance == 'element':
            index.ajout_element(self.varGr.get(),self.comment.get(1.0, "end-1c"), cible, self.identifiant.get(), self.clas.get())
            self.ciblage.delete(1.0, "end-1c")
            cible = 'body'
        if provenance == 'lien':
            index.ajout_element(self.varGr.get(),lienSansListe, cible, self.identifiant.get(), self.clas.get())
            self.ciblage.delete(1.0, "end-1c")
            self.qblien.destroy()
            cible = 'body'
        if provenance == 'block':
            index.ajout_block(self.varGr2.get(), cible, self.identifiant.get(), self.clas.get())
            self.ciblage.delete(1.0, "end-1c")
            cible = 'body'
        if provenance == 'menu':
            self.qblien = Button(self.fenLien, text='Retour au menu', command=partial(self.endWithDestroy, self.fenMenu))
            self.qblien.grid(column=0,row=0)
            raise_frame(self.fenLien)
        if provenance == 'menu2':
            global globalLien
            index.ajout_menu(self.nombre_puce.get(), globalLien, cible)
            globalLien = [list(), list()]
            self.validePuce.destroy()
            self.validePuce = Button(self.fenLien, text='Valider', command=partial(self.ajoutListe, globalLien))
            self.validePuce.grid(column=4,row=4, pady=20, padx=180)
            self.ciblage.delete(1.0, "end-1c")
            self.qblien.destroy()
            cible = 'body'
        html_file = os.getcwd() + "//" + "web/index.html"
        window.load_url('file://' + html_file)
        self.comment.delete(1.0, "end-1c")

    def ajoutListe(self, liste):
        liste[0].append(self.textePuce.get())
        liste[1].append(self.adresse.get())
    
        self.textePuce.delete(0, 100)
        self.adresse.delete(0, 100)
        acc = len(liste[0])
        if acc >= int(self.nombre_puce.get()):
            self.validePuce.destroy()
            self.validePuce = Button(self.fenLien, text='Fini !', command=partial(self.enter_click, 'menu2'))
            self.validePuce.grid(column=4,row=4, pady=20, padx=180)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            window.destroy()

    def endWithDestroy(self, frame):
        self.qblien.destroy()
        raise_frame(frame)
    def linkWithoutList(self, link, texte):
        global lienSansListe
        raise_frame(self.fenCiblage)
        lienSansListe = '<a href="{}">{}</a>\n'.format(link.get(),texte.get())
    def verif(self,provenance):
        if provenance == 'lien':
            self.validePuce.destroy()
            self.validePuce = Button(self.fenLien, text='Valider', command=partial(self.linkWithoutList, self.adresse, self.textePuce))
            self.validePuce.grid(column=4,row=4, padx=20, pady=20)
            self.qblien = Button(self.fenLien, text='Retour', command=partial(self.endWithDestroy, self.fenAjoutElement))
            self.qblien.grid(column=0,row=0)
            raise_frame(self.fenLien)

        if provenance == 'block':
            if self.varGr2.get():
                raise_frame(self.fenCiblage)
                self.retour = Button(self.fenCiblage, text='Retour', command=partial(raise_frame, self.fenAjoutBlock))
                self.retour.grid(column=0,row=0)
            else:
                messagebox.showwarning("Champ vide", "Veuillez choisir un type d'élément et son contenu !")
        if provenance == 'menu':
            if self.nombre_puce.get() in '123456789' and self.nombre_puce.get() != '':
                raise_frame(self.fenCiblage)
                self.retour = Button(self.fenCiblage, text='Retour', command=partial(raise_frame, self.fenMenu))
                self.retour.grid(column=0,row=0)
            else:
                messagebox.showwarning("Champ incorrect", "Veuillez choisir un nombre !")
        if provenance == 'element':
            if self.varGr.get() and self.comment.get(1.0, "end-1c"):
                raise_frame(self.fenCiblage)
                self.retour = Button(self.fenCiblage, text='Retour', command=partial(raise_frame, self.fenAjoutElement))
                self.retour.grid(column=0,row=0)
            else:
                messagebox.showwarning("Champ vide", "Veuillez choisir un type d'élément et son contenu !")
        self.valider = Button(self.fenCiblage, text='Valider', command=partial(self.enter_click, provenance))
        self.valider.grid(column=1,row=13)

html_file = os.getcwd() + "//" + "web/index.html"
window = webview.create_window('Votre site !', 'file://' + html_file, width=500, height = 500)
webview.start(letgo())



