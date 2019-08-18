from tkinter import Tk, Button, Entry, Label, messagebox, Radiobutton, IntVar
from functools import partial
from threading import Thread
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import index

try:
    if os.stat("web/index.html").st_size == 0:
        index.base_html()
except:
    index.base_html()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        Web.driver.close()
def test():
    if Web.isAlive():
        print('Il existe')
    else:
        print('Non')

class ViewHtml(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.oui = True
    def run(self):
        chrome_options = Options()
        html_file = os.getcwd() + "//" + "web/index.html"
        chrome_options.add_argument("--app=file:///" + html_file)
        chrome_options.add_argument("--window-size=600,539")
        chrome_options.add_argument("--window-position=601,100")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        assert "No results found." not in self.driver.page_source
        while self.oui:
            time.sleep(2)
            self.driver.refresh()
    def enter_click(self):
        index.ajout_element(qb2.get(),comment.get())
        self.driver.refresh()
    def fini(self):
        self.oui = False
        on_closing()


Web = ViewHtml()
root = Tk()
Web.start()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("500x500+100+100")
root.propagate(0)
root.title('Simple exemple')

qb = Button(root, text='Quitter', command=partial(Web.fini))
qb.pack()
text = Label(root, text="Entrer l'élément à ajouter sur votre site : ")
text.pack()
qb2 = Entry(root, width=10)
qb2.pack()
comment = Entry(root, width=10)
comment.pack()
valide = Button(root, text='Valider', command=partial(Web.enter_click))
valide.pack()

test = Button(root, text='TEST THREAD', command=partial(test))
test.pack()
b = Radiobutton(root, text='slt', value='p')
b.pack()

root.mainloop()


