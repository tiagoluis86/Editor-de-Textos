from tkinter import *
from tkinter.ttk import *


def openAbout():
    about = Tk() 
    about.title("Sobre esse programa")
    about.geometry("400x100")
    Label(about, text ="Programa desenvolvido por Tiago Luis Custódio\nTodos os direitos reservados \n2022\ntiagoluis86@outlook.com").pack()