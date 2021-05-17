#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/rodrigokl/IDFModifier

# Rodrigo K. Leitzke, UFPEL - Laboratório de conforto e Eficiência energética; 
# Proposta de uma ferramenta que altere as caracteristicas do IDF utilizando a biblioteca EPPY

from Tkinter import *
from tkFileDialog import *
import ttk
import Tkinter as tk
from eppy import modeleditor
from eppy.modeleditor import IDF
try:
    # python 2
    from tkFont import Font
except ImportError:
    # python 3
    from tkinter.font import Font


import platform
import os
from definitions_modifier import *

#-----------------------------------------

tkTop = Tk()
tkTop.title("IDF MODIFIER")
#tkTop.geometry('670x250')
tkTop.resizable(0,0)
mainframe = ttk.Frame(tkTop, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

noteStyler = ttk.Style()
noteStyler.theme_use('vista')
noteStyler.configure("TFrame", background="white", foreground="green", borderwidth=0)
noteStyler.configure("TNotebook", background='white',darkcolor='#3A8FD7',lightcolor='#3A8FD7', borderwidth=0)
noteStyler.map("TNotebook.Tab", background=[("selected", 'gray')], foreground=[("selected", '#3A8FD7')]);
noteStyler.configure("TNotebook.Tab", background='#9e9e9e', foreground='#9e9e9e',bordercolor='#3A8FD7',  borderwidth=0,font='Arial 10 bold')
noteStyler.configure("TButton",background='gray',foreground='#3A8FD7', borderwidth=0,font='Arial 8 bold')
noteStyler.configure("TCheckbutton",background='white',foreground='#3A8FD7', borderwidth=0,font='Arial 8 bold')

 
notebook = ttk.Notebook(tkTop,style='TNotebook')
frame1 = ttk.Frame(notebook,style='TFrame')
frame2 = ttk.Frame(notebook,style='TFrame')
frame3 = ttk.Frame(notebook,style='TFrame')
frame4 = ttk.Frame(notebook,style='TFrame')
frame5 = ttk.Frame(notebook,style='TFrame')
frame6 = ttk.Frame(notebook,style='TFrame')
frame7 = ttk.Frame(notebook,style='TFrame')
notebook.add(frame1, text='Entrada')
notebook.add(frame2, text='Opções')
notebook.add(frame3, text='Isolamento')
notebook.add(frame4, text='Equipamentos')
notebook.add(frame5, text='Uso e ocupação')
notebook.add(frame6, text='Simular')
notebook.add(frame7, text='Resultados')
notebook.grid()


iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=1, sticky=W)

idflab = "Arquivo IDF:"
idflab = tk.Label(frame1, text=idflab, background='white',font='arial 10') 
idflab.grid(column=1, row=2, padx=10)

idftext = tk.Entry(frame1,width=50)
idftext.grid(column=2, row=2, padx=10)
procuraridf = ttk.Button(frame1,text="Procurar", command=load_file_IDF, style='TButton')
procuraridf.grid(column=3, row=2, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=3, sticky=W)

# --------------------------------------

iddlab = "Arquivo IDD:"
iddlab = tk.Label(frame1, text=iddlab, background='white',font='arial 10') 
iddlab.grid(column=1, row=4, padx=10)

iddtext = tk.Entry(frame1,width=50)
iddtext.grid(column=2, row=4, padx=10)
procuraridd = ttk.Button(frame1,text="Procurar",command=load_file_IDD, style='TButton')
procuraridd.grid(column=3, row=4, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=5, padx=10)

# --------------------------------------

epwlab = "Arquivo EPW:"
epwlab = tk.Label(frame1, text=epwlab, background='white', font='arial 10') 
epwlab.grid(column=1, row=6, padx=10)

epwtext = tk.Entry(frame1,width=50)
epwtext.grid(column=2, row=6, padx=10)
procurarepw = ttk.Button(frame1,text="Procurar",command=load_file_EPW, style='TButton')
procurarepw.grid(column=3, row=6, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=7, padx=10)

tkButtonQuit = ttk.Button(frame1, text="   Sair    ",command=quit, style='TButton')
tkButtonQuit.grid(column=3, row=8, padx=10)
tkButtonConfirma = ttk.Button(frame1, text="  Confirma  ",command=confirma_arqs, style='TButton')
tkButtonConfirma.grid(column=2, row=8, sticky = E)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=9, padx=10)

tk.mainloop()