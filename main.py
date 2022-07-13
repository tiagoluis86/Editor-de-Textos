from tkinter import Tk, Frame, Menu, Button
import time 

#root window

root = Tk() 
root.geometry('800x600')
root.resizable(height=True, width=True)
root.title('Bloco de Notas')

#criação da menubar

menubar = Menu(root) 
root.config(menu=menubar)

#criação do menu arquivo

arquivo_menu = Menu(   
    menubar,
    tearoff=0
)

#itens do menu arquivo
arquivo_menu.add_command(label="Novo")
arquivo_menu.add_command(label="Abrir")
arquivo_menu.add_command(label="Salvar")
arquivo_menu.add_command(label="Salvar Como...")
arquivo_menu.add_command(label="Imprimir")
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.destroy)

#adiciona o menu arquivo ao menubar
menubar.add_cascade(
    label="Arquivo",
    menu=arquivo_menu
)

#menu editar

editar_menu = Menu(
    menubar,
    tearoff=0
)

editar_menu.add_command(label="Localizar")
editar_menu.add_command(label="Substituir")
editar_menu.add_separator()
editar_menu.add_command(label="Recortar")
editar_menu.add_command(label="Copiar")
editar_menu.add_command(label="Colar")

menubar.add_cascade(
    label="Editar",
    menu=editar_menu
)

#menu ferramentas

ferramentas_menu = Menu(
    menubar,
    tearoff=0
)

ferramentas_menu.add_command(label="Fonte")
ferramentas_menu.add_command(label="Parágrafo")
ferramentas_menu.add_separator()
ferramentas_menu.add_command(label="Layout da Página")

menubar.add_cascade(
    label="Ferramentas",
    menu=ferramentas_menu
)

#menu ajuda

ajuda_menu = Menu(
    menubar,
    tearoff=0
)

ajuda_menu.add_command(label="Ajuda")
ajuda_menu.add_command(label="Sobre")

menubar.add_cascade(
    label="Ajuda",
    menu=ajuda_menu
)


root.mainloop()


