
from tkinter import Tk, Button, Entry, Label
from functools import partial
from threading import Thread
import os
import signal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.chrome.options import Options
import index
try:
    if os.stat("web/index.html").st_size == 0:
        index.base_html()
except:
    index.base_html()

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
        

    def run(self):
        chrome_options = Options()
        html_file = os.getcwd() + "//" + "web/index.html"
        chrome_options.add_argument("--app=file:///" + html_file)
        chrome_options.add_argument("--window-size=600,539")
        chrome_options.add_argument("--window-position=601,100")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        assert "No results found." not in driver.page_source


Web = ViewHtml()
root = Tk()
Web.start()
root.geometry("500x500+100+100")
root.propagate(0)
root.title('Simple exemple')
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=partial(root.destroy))
qb.pack()
text = Label(root, text="Entrer l'élément à ajouter sur votre site : ")
text.pack()
qb = Entry(root, width=10)
qb.pack()
comment = Entry(root, width=10)
comment.pack()
valide = Button(root, text='Valider', command=partial(index.ajout_element, qb.get(), comment.get()))
valide.pack()
# Lancement de la «boucle principale»
root.mainloop()


