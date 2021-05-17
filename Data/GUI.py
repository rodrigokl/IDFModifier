#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
from modifier import *

# GLOBAL VARIABLES

fname = ""
idd = ""
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
lista_idfs = []
ct = 0.0
densidade_nova = 0.0
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
ct_nova = 0.0
rt = 0.0
tkTop = Tk()
tkTop.title("IDF MODIFIER")
tkTop.geometry('640x270')
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

# --------------------------------------

# FRAME 1

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
# --------------------------------------

# FRAME 3

# Informações dos constructions:
chk_piso = ttk.Checkbutton(frame3, text="Piso",style='TCheckbutton')
chk_piso.grid(column=4, row=3)

chk_cobertura = ttk.Checkbutton(frame3, text="Cobertura",style='TCheckbutton')
chk_cobertura.grid(column=5, row=3)

chk_parede = ttk.Checkbutton(frame3, text="Parede",style='TCheckbutton')
chk_parede.grid(column=6, row=3)

# FRAME 4

branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame4, text="Método de Cálculo:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame4,width=15)
box4.grid(column=1, row=2, sticky=S, padx=130)
branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
valor_inicial = tk.Label(frame4, text="Valor inicial:", background='white',font='Arial 10') 
valor_inicial.grid(column=1, row=4, sticky=W,padx=10)
valor_inicial_texto = tk.Entry(frame4,width=18)
valor_inicial_texto.grid(column=1, row=4)
valor_final = tk.Label(frame4, text="Valor final:", background='white',font='Arial 10') 
valor_final.grid(column=1, row=5, sticky=W,padx=10)
valor_final_texto = tk.Entry(frame4,width=18)
valor_final_texto.grid(column=1, row=5)
passo = tk.Label(frame4, text="Passo:", background='white',font='Arial 10') 
passo.grid(column=1, row=6, sticky=W,padx=10)
passo_texto = tk.Entry(frame4,width=18)
passo_texto.grid(column=1, row=6, padx=10)
branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=7, sticky=W,padx=10)
gerar_idfs = ttk.Button(frame4, text=" Gerar ",width=15, command=gera_idf_u)
gerar_idfs.grid(column=1, row=9, sticky=S)

# FRAME 5

branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame5, text="Método de Cálculo:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame5,width=15)
box4.grid(column=1, row=2, sticky=S, padx=130)
branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
valor_inicial = tk.Label(frame5, text="Valor inicial:", background='white',font='Arial 10') 
valor_inicial.grid(column=1, row=4, sticky=W,padx=10)
valor_inicial_texto = tk.Entry(frame5,width=18)
valor_inicial_texto.grid(column=1, row=4)
valor_final = tk.Label(frame5, text="Valor final:", background='white',font='Arial 10') 
valor_final.grid(column=1, row=5, sticky=W,padx=10)
valor_final_texto = tk.Entry(frame5,width=18)
valor_final_texto.grid(column=1, row=5)
passo = tk.Label(frame5, text="Passo:", background='white',font='Arial 10') 
passo.grid(column=1, row=6, sticky=W,padx=10)
passo_texto = tk.Entry(frame5,width=18)
passo_texto.grid(column=1, row=6, padx=10)
branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=7, sticky=W,padx=10)
gerar_idfs = ttk.Button(frame5, text=" Gerar ",width=15, command=gera_idf_u)
gerar_idfs.grid(column=1, row=9, sticky=S)

# FRAME 6

#Aba de simulação

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)

metodo_calc = tk.Label(frame6, text="Período de simulação:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame6,width=15)
box4.grid(column=2, row=2, sticky=W, padx=10)

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
saida = tk.Label(frame6, text="Variáveis de saída:", background='white',font='Arial 10') 
saida.grid(column=1, row=4, sticky=W,padx=10)

chk_conforto80 = ttk.Checkbutton(frame6, text="Equipamentos – ganhos de calor",style='TCheckbutton')
chk_conforto80.grid(column=1, row=5,sticky=W, padx=10)

chk_conforto90 = ttk.Checkbutton(frame6, text="Esquadrias – ganhos de calor",style='TCheckbutton')
chk_conforto90.grid(column=1, row=6,sticky=W,padx=10)

chk_consumo_aquecimento = ttk.Checkbutton(frame6, text="Esquadrias – perdas de calor",style='TCheckbutton')
chk_consumo_aquecimento.grid(column=1, row=7,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Esquadrias – radiação solar",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=1, row=8,sticky=W,padx=10)

chk_conforto80 = ttk.Checkbutton(frame6, text="Iluminação – ganhos de calor",style='TCheckbutton')
chk_conforto80.grid(column=1, row=9,sticky=W, padx=10)

chk_conforto90 = ttk.Checkbutton(frame6, text="Superficies opacas – ganhos de calor",style='TCheckbutton')
chk_conforto90.grid(column=2, row=5,sticky=W,padx=10)

chk_consumo_aquecimento = ttk.Checkbutton(frame6, text="Superficies opacas – perdas de calor",style='TCheckbutton')
chk_consumo_aquecimento.grid(column=2, row=6,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Pessoas – ganhos totais de calor",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=7,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Infiltração – ganho sensível e latente",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=8,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Infiltração – perda sensível e latente",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=9,sticky=W,padx=10)

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=10, sticky=W,padx=10)
botaosimular = ttk.Button(frame6, text="Simular",command=simular_idfs, style='TButton')
botaosimular.grid(column=2,row=11,sticky = E,padx=160)


# FRAME 7

branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame7, text="Arquivos simulados:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame7,width=15)
box4.grid(column=1, row=2, sticky=S, padx=135)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=4, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=5, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=6, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=7, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=8, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=9, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=10, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=11, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=12, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=13, sticky=W,padx=10)
branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=14, sticky=W,padx=10)