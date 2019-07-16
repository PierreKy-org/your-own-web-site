import eel
from tkinter import *
from functools import *
from threading import Thread
import os
import signal

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
        

    def run(self):
        eel.start('index.html')
        self.exit()
fenetre = ViewHtml()
eel.init('web')
root = Tk()
root.title('Simple exemple')
# Construction d'un simple bouton
qb = Button(root, text='Quitter', command=partial(fenetre._stop))
qb.pack()

start = Button(root, text='lancer chromium', command=partial(fenetre.start))
start.pack()
# Lancement de la «boucle principale»
root.mainloop()


