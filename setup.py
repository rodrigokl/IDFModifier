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

# DEF's

# --------------------------------------

def confirma_arqs():
	global fname, idd,idf, epw, box2,box3, nome_mat, materials
	if len(fname) == 0 and len(idd) == 0 and len(epw) == 0:
		popupmsg("Insira todos os arquivos na entrada!")
	else:
		IDF.setiddname(idd)
		idf = IDF(fname)
		NADA = tk.Label(frame2, text="", background='white')
		NADA.grid(column=3, row=1, sticky=S)
		pergunta = tk.Label(frame2, text="What you want to optimize?", background='white', font="arial 10")
		pergunta.grid(column=1, row=2, padx=10, sticky=S)
		NADA = tk.Label(frame2, text="", background='white')
		NADA.grid(column=3, row=3, sticky=S)
		isolamento = ttk.Button(frame2,text="  U and TC of the envelope  ",command=tabisolamento, style='TButton')
		isolamento.grid(column=1, row=4,padx=10, sticky=S)
		NADA = tk.Label(frame2, text="", background='white')
		NADA.grid(column=3, row=5, sticky=S)
		equip = ttk.Button(frame2,text="Equipment and systems", command=tabferramentas, style='TButton')
		equip.grid(column=1, row=6, sticky=S)
		NADA = tk.Label(frame2, text="", background='white')
		NADA.grid(column=3, row=7, sticky=S)
		usoocup = ttk.Button(frame2,text="          Use and occupancy          ", command=tabuso, style='TButton')
		usoocup.grid(column=1,row=8,sticky=S)
		tabop()

		# Combobox	
'''
		box_value2 = StringVar()
		box2 = ttk.Combobox(frame2, textvariable=box_value2)
		box2['values'] = nome_mat
		box2.bind("<<ComboboxSelected>>", materiais_combo)
		box2.current(0)
		box2.grid(column=2, row=2)
    	
'''

# --------------------------------------

def tab1():
    notebook.select(frame1)

    
def tabop():
    notebook.select(frame2)

def tabisolamento():

	global box2, constructions, materials, materials_air, u

def tabop():
    notebook.select(frame2)

def tabisolamento():

	global box2, constructions, materials, materials_air


	constructions = idf.idfobjects['CONSTRUCTION'] # selecionando todos os constructions
	nome_cons = [cons.Name for cons in constructions]

	materials = idf.idfobjects['MATERIAL'] # selecionando todos materials
	materials_air = idf.idfobjects['MATERIAL:AIRGAP']

	# Combobox

	NADA = tk.Label(frame3, text="", background='white')
	NADA.grid(column=1, row=0, sticky=S)

	chk_piso = ttk.Checkbutton(frame3, text="Want to keep TC?",style='TCheckbutton')
	chk_piso.grid(column=1, row=1, padx=10)

	NADA = tk.Label(frame3, text="", background='white')
	NADA.grid(column=1, row=2, sticky=S)
	pergunta = tk.Label(frame3, text="Building elements: ", font = "Arial 10", background='white')
	pergunta.grid(column=1, row=3,sticky=W,padx=10)
	box_value2 = StringVar()
	box2 = ttk.Combobox(frame3, textvariable=box_value2)
	box2['values'] = nome_cons
	box2.bind("<<ComboboxSelected>>", construction_combo)
	box2.current(0)
	box2.grid(column=2, row=3,sticky=S,padx=10)

	bt_ok = ttk.Button(frame3, text='Ok', command=transmitancia, style='TButton')
	bt_ok.grid(column=7,row=3,sticky=E,padx=10)

	notebook.select(frame3)

def tabferramentas():
	notebook.select(frame4)	 

def tabuso():
	notebook.select(frame5)

def confirma_thickness():
	mat = box2.get()
	for material in materials:
		if material.Name == mat:
			aux = float(thickness_ini.get())
			while aux < float(thickness_fim.get()):
				material.Thickness = aux
				nome = fname + str(aux) + '.idf'
				#print nome
				idf.saveas(nome)
				aux = aux + float(thickness_timestep.get())
			
def construction_combo(event):

	global rt, sum_res, lis_mat
	sum_res = cond = esp = 0 
	aux = 2
	atual = box2.get()
	for cons in constructions:
		if cons.Name == atual:
			if len(lis_mat) > 0:
				while len(lis_mat) > 0:
					lis_mat.pop()
	
			for material in materials:

				if cons.Outside_Layer == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:			
					
				if cons.Layer_2 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:			

				if cons.Layer_3 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:		

				if cons.Layer_4 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:		

				if cons.Layer_5 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:		

				if cons.Layer_6 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)
				
			for material in materials:	
				
				if cons.Layer_7 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond	
					lis_mat.insert(0,material.Name)

			for material in materials:		
					
				if cons.Layer_8 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond	
					lis_mat.insert(0,material.Name)

			for material in materials:		
	
				if cons.Layer_9 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond
					lis_mat.insert(0,material.Name)

			for material in materials:		

				if cons.Layer_10 == material.Name:
					cond = material.Conductivity
					esp = material.Thickness
					sum_res = sum_res + esp/cond	
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Outside_Layer == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:		
				if cons.Layer_2 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:		
				if cons.Layer_3 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_4 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_5 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance	
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_6 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)


			for material_air in materials_air:
				if cons.Layer_7 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_8 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_9 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

			for material_air in materials_air:
				if cons.Layer_10 == material_air.Name:
					sum_res = sum_res + material_air.Thermal_Resistance
					lis_mat.insert(0,material.Name)

def transmitancia():
	global inf, sup, delta_u_entry,u, box3, rt

	if chk_parede.instate(['selected']):
		rt = 0.04 + 0.13 + sum_res
		u = 1/rt
		trans = tk.Label(frame3, text="Transmittance (U) [W/(m²k)]: ",background='white', font='Arial 10')
		trans.grid(column=1, row=4, sticky=W,padx=10)
		trans_entry = tk.Entry(frame3,width=23)
		trans_entry.grid(column=2, row=4, sticky=W,padx=10)
		trans_entry.insert(0,"%.2f" % u)	

	if chk_piso.instate(['selected']):
		rt = 0.17 + 0.17 + sum_res
		u = 1/rt
		trans = tk.Label(frame3, text="Transmittance (U) [W/(m²k)]: ",background='white', font='Arial 10')
		trans.grid(column=1, row=4, sticky=W,padx=10)
		trans_entry = tk.Entry(frame3,width=23)
		trans_entry.grid(column=2, row=4, sticky=W,padx=10)
		trans_entry.insert(0,"%.2f" % u)

	if chk_cobertura.instate(['selected']):
		rt = 0.04 + 0.10 + sum_res
		u = 1/rt
		trans = tk.Label(frame3, text="Transmittance (U) [W/(m²k)]: ",background='white', font='Arial 10')
		trans.grid(column=1, row=4, sticky=W,padx=10)
		trans_entry = tk.Entry(frame3,width=23)
		trans_entry.grid(column=2, row=4, padx=10)
		trans_entry.insert(0,"%.2f" % u)

	materiais_da_lista = tk.Label(frame3, text="Which Material to change?",background='white', font='Arial 10')
	materiais_da_lista.grid(column=1, row=5, sticky=W,padx=10)	
	box_value2 = StringVar()
	box3 = ttk.Combobox(frame3, textvariable=box_value2)
	box3['values'] = lis_mat
	box3.current(0)
	box3.grid(column=2, row=5)

	lim_inf = tk.Label(frame3, text="Current TC Material:", background='white',font='Arial 10') 
	lim_inf.grid(column=1, row=6, sticky=W,padx=10)
	gg = tk.Entry(frame3,width=23)
	gg.grid(column=2, row=6, sticky=W,padx=10)
	#gg.insert(0,"%.2f" % ct/1000)
	lim_inf = tk.Label(frame3, text="U bottom (<):", background='white',font='Arial 10') 
	lim_inf.grid(column=1, row=7, sticky=W,padx=10)
	inf = tk.Entry(frame3,width=23)
	inf.grid(column=2, row=7, sticky=W,padx=10)


	lim_sup = tk.Label(frame3, text="U higher (>):",background='white', font='Arial 10') 
	lim_sup.grid(column=1, row=8, sticky=W,padx=10)
	sup = tk.Entry(frame3,width=23)
	sup.grid(column=2, row=8, sticky=W,padx=10)
	
	delta_u = tk.Label(frame3, text="Variation (ΔU):",background='white', font='Arial 10') 
	delta_u.grid(column=1, row=9, sticky=W,padx=10)
	delta_u_entry = tk.Entry(frame3,width=23)
	delta_u_entry.grid(column=2, row=9, sticky=W,padx=10)
	gerar_idfs = ttk.Button(frame3, text=" Generate ", command=gera_idf_u)
	gerar_idfs.grid(column=7, row=10, sticky=S)
	
def gera_idf_u():
	global u,ct,ct_nova, lis_mat, espessura_nova, densidade_nova, rt, sum_res
	
	res = sum_aux = 0.0
	superior = sup.get()
	inferior = inf.get()
	atual = box2.get()
	aux_superior = superior
	aux_inferior = inferior
	
	for cons in constructions:
		if cons.Name == atual:
			for material in materials:
				espessura_atual = material.Thickness
				condutividade_atual = material.Conductivity	
				if material.Name == box3.get():
					while(float(aux_inferior) <= float(aux_superior)):	
						rt_nova = 1/float(aux_inferior)
						u_nova = 1/rt_nova
						densidade_atual = material.Density
						ct = espessura_atual*material.Specific_Heat*material.Density
						#print ct
						res_atual = float(espessura_atual)/float(condutividade_atual)
						espessura_nova = (((rt - res_atual)*-1)+rt_nova)*condutividade_atual # Calcula qual a nova espessura da parede, mantendo a condutividade
						ct_nova = espessura_nova*material.Specific_Heat*material.Density
						#print ct_nova
						ct_nova = ct_nova/1000
						ct_nova = "%.2f" % ct_nova
						#densidade_nova =  ct_nova/(espessura_nova*material.Specific_Heat)
						#print densidade_nova
						material.Thickness = "%.2f" % espessura_nova
						#material.Density = "%.2f" % densidade_nova
						nome = "isolamento u " + str(u_nova) + " Capacidade termica "+ str(ct_nova) + '.idf'
						idf.saveas('%s' % nome)
						lista_idfs.append(nome)
						material.Thickness = espessura_atual
						#material.Density = densidade_atual
						aux_inferior = float(aux_inferior) + float(delta_u_entry.get())
	notebook.select(frame6)					

def simular_idfs():
	global epw
	for idf in lista_idfs:
		nome = idf.replace('idf','')
		saida = os.getcwd() + "\%s" % nome
		idf_run = IDF(idf, epw)
		idf_run.run(output_directory=saida)

def analisa_resultados():
	for nome in lista_idfs:
		nomedir = nome.replace('.idf','')
		saidaeso = os.getcwd() + '\%s' % nomedir +'\eplusout.eso'
		#print saidaeso
															




tkTop = Tk()
tkTop.title("IDF MODIFIER")
#tkTop.geometry('500x250')
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
notebook.add(frame1, text='In')
notebook.add(frame2, text='Options')
notebook.add(frame3, text='U and TC')
notebook.add(frame4, text='Equipaments')
notebook.add(frame5, text='Use and ocupancy')
notebook.add(frame6, text='Simulation')
notebook.add(frame7, text='Results')
notebook.grid()

# --------------------------------------
def load_file_IDF():
    global fname
    fname = askopenfilename(filetypes=(("Arquivos IDF", "*.idf"),
                                           ("All files", "*.*")))
    if fname:
      try:
        idftext.insert(INSERT, fname)

      except:                     
        showerror("Falha!", "Erro ao abrir o arquivo idf\n'%s'" % fname)
        return

def load_file_EPW():
    global epw
    epw = askopenfilename(filetypes=(("Arquivos EPW", "*.epw"),
                                           ("All files", "*.*")))
    if epw:
      try:
        epwtext.insert(INSERT, epw)
                
      except:                     
        showerror("Falha!", "Erro ao abrir o arquivo epw\n'%s'" % epw)
        return

def load_file_IDD():
    global idd
    idd = askopenfilename(filetypes=(("Arquivos IDD", "*.idd"),
                                           ("All files", "*.*")))
    if idd:
      try:
        iddtext.insert(INSERT, idd)
    
      except:                     
        showerror("Falha!", "Erro ao abrir o arquivo epw\n'%s'" % idd)
        return

# FRAME 1

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=1, sticky=W)

idflab = "IDF File:"
idflab = tk.Label(frame1, text=idflab, background='white',font='arial 10') 
idflab.grid(column=1, row=2, padx=10)

idftext = tk.Entry(frame1,width=50)
idftext.grid(column=2, row=2, padx=10)
procuraridf = ttk.Button(frame1,text="Search", command=load_file_IDF, style='TButton')
procuraridf.grid(column=3, row=2, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=3, sticky=W)
# --------------------------------------


iddlab = "IDD File:"
iddlab = tk.Label(frame1, text=iddlab, background='white',font='arial 10') 
iddlab.grid(column=1, row=4, padx=10)

iddtext = tk.Entry(frame1,width=50)
iddtext.grid(column=2, row=4, padx=10)
procuraridd = ttk.Button(frame1,text="Search",command=load_file_IDD, style='TButton')
procuraridd.grid(column=3, row=4, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=5, padx=10)

# --------------------------------------

epwlab = "EPW File:"
epwlab = tk.Label(frame1, text=epwlab, background='white', font='arial 10') 
epwlab.grid(column=1, row=6, padx=10)

epwtext = tk.Entry(frame1,width=50)
epwtext.grid(column=2, row=6, padx=10)
procurarepw = ttk.Button(frame1,text="Search",command=load_file_EPW, style='TButton')
procurarepw.grid(column=3, row=6, padx=10)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=7, padx=10)

tkButtonQuit = ttk.Button(frame1, text="   Exit    ",command=quit, style='TButton')
tkButtonQuit.grid(column=3, row=8, padx=10)
tkButtonConfirma = ttk.Button(frame1, text="  Confirm  ",command=confirma_arqs, style='TButton')
tkButtonConfirma.grid(column=2, row=8, sticky = E)

iddlab = ""
iddlab = tk.Label(frame1, text=iddlab, background='white') 
iddlab.grid(column=1, row=9, padx=10)

# --------------------------------------

# FRAME 3

# Informações dos constructions:
chk_piso = ttk.Checkbutton(frame3, text="Floor",style='TCheckbutton')
chk_piso.grid(column=4, row=3)

chk_cobertura = ttk.Checkbutton(frame3, text="Roof",style='TCheckbutton')
chk_cobertura.grid(column=5, row=3)

chk_parede = ttk.Checkbutton(frame3, text="Wall",style='TCheckbutton')
chk_parede.grid(column=6, row=3)

# FRAME 4

branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame4, text="Calculation method:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame4,width=15)
box4.grid(column=1, row=2, sticky=S, padx=130)
branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
valor_inicial = tk.Label(frame4, text="Start value:", background='white',font='Arial 10') 
valor_inicial.grid(column=1, row=4, sticky=W,padx=10)
valor_inicial_texto = tk.Entry(frame4,width=18)
valor_inicial_texto.grid(column=1, row=4)
valor_final = tk.Label(frame4, text="End value:", background='white',font='Arial 10') 
valor_final.grid(column=1, row=5, sticky=W,padx=10)
valor_final_texto = tk.Entry(frame4,width=18)
valor_final_texto.grid(column=1, row=5)
passo = tk.Label(frame4, text="Step:", background='white',font='Arial 10') 
passo.grid(column=1, row=6, sticky=W,padx=10)
passo_texto = tk.Entry(frame4,width=18)
passo_texto.grid(column=1, row=6, padx=10)
branco = tk.Label(frame4, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=7, sticky=W,padx=10)
gerar_idfs = ttk.Button(frame4, text=" Generate ",width=15, command=gera_idf_u)
gerar_idfs.grid(column=1, row=9, sticky=S)

# FRAME 5

branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame5, text="Calculation method:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame5,width=15)
box4.grid(column=1, row=2, sticky=S, padx=130)
branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
valor_inicial = tk.Label(frame5, text="Start value:", background='white',font='Arial 10') 
valor_inicial.grid(column=1, row=4, sticky=W,padx=10)
valor_inicial_texto = tk.Entry(frame5,width=18)
valor_inicial_texto.grid(column=1, row=4)
valor_final = tk.Label(frame5, text="End value:", background='white',font='Arial 10') 
valor_final.grid(column=1, row=5, sticky=W,padx=10)
valor_final_texto = tk.Entry(frame5,width=18)
valor_final_texto.grid(column=1, row=5)
passo = tk.Label(frame5, text="Step:", background='white',font='Arial 10') 
passo.grid(column=1, row=6, sticky=W,padx=10)
passo_texto = tk.Entry(frame5,width=18)
passo_texto.grid(column=1, row=6, padx=10)
branco = tk.Label(frame5, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=7, sticky=W,padx=10)
gerar_idfs = ttk.Button(frame5, text=" Generate ",width=15, command=gera_idf_u)
gerar_idfs.grid(column=1, row=9, sticky=S)

# FRAME 6

#Aba de simulação

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)

metodo_calc = tk.Label(frame6, text="simulation period:", background='white',font='Arial 10') 
metodo_calc.grid(column=1, row=2, sticky=W,padx=10)
box4 = ttk.Combobox(frame6,width=15)
box4.grid(column=2, row=2, sticky=W, padx=10)

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=3, sticky=W,padx=10)
saida = tk.Label(frame6, text="Ouutput variables:", background='white',font='Arial 10') 
saida.grid(column=1, row=4, sticky=W,padx=10)

chk_conforto80 = ttk.Checkbutton(frame6, text="Equipment - heat gains",style='TCheckbutton')
chk_conforto80.grid(column=1, row=5,sticky=W, padx=10)

chk_conforto90 = ttk.Checkbutton(frame6, text="Windows – heat gains",style='TCheckbutton')
chk_conforto90.grid(column=1, row=6,sticky=W,padx=10)

chk_consumo_aquecimento = ttk.Checkbutton(frame6, text="Windows – heat losses",style='TCheckbutton')
chk_consumo_aquecimento.grid(column=1, row=7,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Windows – solar radiation",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=1, row=8,sticky=W,padx=10)

chk_conforto80 = ttk.Checkbutton(frame6, text="Lights – heat gains",style='TCheckbutton')
chk_conforto80.grid(column=1, row=9,sticky=W, padx=10)

chk_conforto90 = ttk.Checkbutton(frame6, text="Opaque Surfaces – heat gains",style='TCheckbutton')
chk_conforto90.grid(column=2, row=5,sticky=W,padx=10)

chk_consumo_aquecimento = ttk.Checkbutton(frame6, text="Opaque Surfaces – heat losses",style='TCheckbutton')
chk_consumo_aquecimento.grid(column=2, row=6,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="People – heat gains",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=7,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Infiltration – sensitive and latent gains",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=8,sticky=W,padx=10)

chk_consumo_resfriamento = ttk.Checkbutton(frame6, text="Infiltration – sensitive and latent losses",style='TCheckbutton')
chk_consumo_resfriamento.grid(column=2, row=9,sticky=W,padx=10)

branco = tk.Label(frame6, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=10, sticky=W,padx=10)
botaosimular = ttk.Button(frame6, text="Simulate",command=simular_idfs, style='TButton')
botaosimular.grid(column=2,row=11,sticky = E,padx=160)


# FRAME 7

branco = tk.Label(frame7, text="", background='white',font='Arial 10') 
branco.grid(column=1, row=1, sticky=W,padx=10)
metodo_calc = tk.Label(frame7, text="Simulated Files:", background='white',font='Arial 10') 
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


tk.mainloop()