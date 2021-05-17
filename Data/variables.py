fname = ""
idd = ""
#!/usr/bin/env python
# -*- encoding: utf-8 -*-


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

idf = ""
epw = "" 
box2 = ""
box3 = ""
nome_mat = ""
materials = []
materials_air = []
buildings = []
constructions = []
espessura = []
condutividade = []
lis_mat = []
sup = ""
inf = ""
espessura_nova = 0.0
condutividade_atual = 0.0
espessura_atual = 0.0
delta_u_entry = ""
trans_entry = ""
rt = 0.0
u = 0.0
sum_res = 0.0
rt = 0.0
tkTop = Tk()
tkTop.title("IDF MODIFIER")
tkTop.geometry('670x250')
tkTop.resizable(0,0)
mainframe = ttk.Frame(tkTop, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
 
notebook = ttk.Notebook(tkTop)
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
frame4 = ttk.Frame(notebook)
frame5 = ttk.Frame(notebook)
notebook.add(frame1, text='Entrada')
notebook.add(frame2, text='Opções')
notebook.add(frame3, text='Isolamento')
notebook.add(frame4, text='Equipamentos')
notebook.add(frame5, text='Uso e ocupação')
notebook.grid()
