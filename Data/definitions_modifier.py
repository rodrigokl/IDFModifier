# --------------------------------------

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

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("ERRO")
    popup.resizable(0,0)
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.mainloop()		

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
 

def confirma_arqs():
    global fname, idd,idf, epw, box2,box3, nome_mat, materials
    if len(fname) == 0 and len(idd) == 0 and len(epw) == 0:
      popupmsg("Insira todos os arquivos na entrada!")
    else:
      notebook.select(frame2)

def quit():
    global tkTop
    tkTop.destroy()
