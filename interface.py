from tkinter import Tk, Button, Entry, Label, messagebox, Radiobutton, StringVar, Scrollbar, Text, Frame
from functools import partial
from threading import Thread
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import index

choix = ['p', 'h1', 'h2', 'nav', 'div', 'section', 'article']
choixStr = ['Paragraphe', 'Gros titre', 'Titre', 'Navigation', 'Balise basique', 'Section', 'Article']
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

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.oui = True
    def run(self):
        chrome_options = Options()
        html_file = os.getcwd() + "//" + "web/index.html"
        chrome_options.add_argument("--app=file:///" + html_file)
        chrome_options.add_argument("--window-size=600,539")
        chrome_options.add_argument("--window-position=701,100")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        assert "No results found." not in self.driver.page_source
        while self.oui:
            time.sleep(2)
            self.driver.refresh()
    def enter_click(self):
        raise_frame(base)
        index.ajout_element(varGr.get(),comment.get(1.0, "end-1c"), ciblage.get(1.0, "end-1c"), identifiant.get(), clas.get())
        self.driver.refresh()
        ciblage.delete(1.0, "end-1c")
        comment.delete(1.0, "end-1c")
    def fini(self):
        self.oui = False
        on_closing()


Web = ViewHtml()
root = Tk()

base = Frame(root)
fenCiblage = Frame(root)
f3 = Frame(root)
f4 = Frame(root)

for frame in (base, fenCiblage, f3, f4):
    frame.grid(row=0, column=0, sticky='news')


Web.start()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("700x500+0+100")
root.propagate(0)
root.title('Simple exemple')

#MENU PRINCIPALE
qb = Button(base, text='Quitter', command=partial(Web.fini))
qb.grid(column=0,row=0)
text = Label(base, text="Choisisser l'élément à ajouter sur votre site : ")
text.grid(column=0,row=1, columnspan=4, pady=50)

varGr = StringVar()
for i in range(len(choix)):
    b = Radiobutton(base, variable=varGr,text=choixStr[i], value=choix[i])
    b.grid(column=1,row=i+2)

text1 = Label(base, text="Entrer le texte que possèdera l'élément : ")
text1.grid(column=5,row=1, columnspan=4)

comment = Text(base, height=7, width=30)
comment.grid(column=5,row=2,columnspan=4, rowspan = 5)

retourLigne = Button(base, text='Retour à la ligne', command=partial(comment.insert, "end-1c", '</br>'))
retourLigne.grid(column=1,row=9)

valide = Button(base, text='Valider', command=partial(raise_frame, fenCiblage))
valide.grid(column=8,row=9, pady=20, padx=180)




#FENETRE DE CIBLAGE
textCiblage = Label(fenCiblage, text="Entrer le texte d'un élément ou son id/class (votre texte sera juste en dessous) : ")
textCiblage.grid(column=0,row=0, columnspan=4)

ciblage = Text(fenCiblage, height=7, width=30)
ciblage.grid(column=0,row=2,columnspan=4, rowspan = 5)

textId = Label(fenCiblage, text="**Optionnel** Entrer un identifiant (cela permet de trouver votre élément plus facilement) : ")
textId.grid(column=0,row=8)

identifiant = Entry(fenCiblage)
identifiant.grid(column=0,row=9)

textClass = Label(fenCiblage, text="**Optionnel** Entrer une class (cela permet de trouver votre élément plus facilement) : ")
textClass.grid(column=0,row=10)

clas = Entry(fenCiblage)
clas.grid(column=0,row=11)

valider = Button(fenCiblage, text='Valider', command=partial(Web.enter_click))
valider.grid(column=1,row=12)



raise_frame(base)
root.mainloop()


