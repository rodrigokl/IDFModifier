#!/usr/bin/env python
# -*- coding: utf-8 -*-

from javax.swing import *
from java.awt import BorderLayout
from java.lang import *
from javax.swing.filechooser import *

frame = JFrame('IDF MODIFIER')
frame.setSize(600, 600)
frame.setResizable(0)
frame.setLayout(BorderLayout())
pnl = JPanel()
frame.add(pnl)

class Modifier:



    def idf_choose(self, e):
        chooseFile = JFileChooser()
        filter = FileNameExtensionFilter("Arquivos IDF", ["idf"])
        chooseFile.addChoosableFileFilter(filter)
        ret = chooseFile.showDialog(self.textidf, "Selecionar")
        f = chooseFile.getSelectedFile()
        self.textidf.setText(str(f))

    def idd_choose(self, e):
        chooseFile = JFileChooser()
        filter = FileNameExtensionFilter("Arquivos IDD", ["idd"])
        chooseFile.addChoosableFileFilter(filter)
        ret = chooseFile.showDialog(self.textidf, "Selecionar")
        f = chooseFile.getSelectedFile()
        self.textidd.setText(str(f))

    def epw_choose(self, e):
        chooseFile = JFileChooser()
        filter = FileNameExtensionFilter("Arquivos EPW", ["epw"])
        chooseFile.addChoosableFileFilter(filter)
        ret = chooseFile.showDialog(self.textepw, "Selecionar")
        f = chooseFile.getSelectedFile()
        self.textepw.setText(str(f))        


    """def cbSelect(self, event):
		selected = self.cb1.selectedIndex
		if selected >= 0:
			materiais = self.materiais[selected]
			self.label5.text = materiais + " selected"     
"""
    def __init__(self):

        # LEITURA DOS ARQUIVOS 
        self.label = JLabel('Arquivo IDF:  ')
        pnl.add(self.label, BorderLayout.NORTH)
        self.textidf = JTextField('',30)
        pnl.add(self.textidf, BorderLayout.NORTH)
        button = JButton('Procurar', actionPerformed = self.idf_choose)
        pnl.add(button)

        self.label2 = JLabel('Arquivo IDD:  ')
        pnl.add(self.label2, BorderLayout.NORTH)
        self.textidd = JTextField('',30)
        pnl.add(self.textidd, BorderLayout.NORTH)
        button2 = JButton('Procurar', actionPerformed = self.idd_choose)
        pnl.add(button2)

        self.label3 = JLabel('Arquivo EPW:')
        pnl.add(self.label3, BorderLayout.NORTH)
        self.textepw = JTextField('',30)
        pnl.add(self.textepw, BorderLayout.NORTH)
        button3 = JButton('Procurar', actionPerformed = self.epw_choose)
        pnl.add(button3)


        # COMBO BOX DAS INFORMAÇÕES
        	
        self.label4 = JLabel('Materiais:')
        pnl.add(self.label4, BorderLayout.SOUTH)

        self.materiais = ('GG','GG1')
        self.cb1 = JComboBox(self.materiais)
        pnl.add(self.cb1)
        """
        btn = JButton('click me', actionPerformed = self.cbSelect)
    	pnl.add(btn,BorderLayout.SOUTH)
        self.label5 = JLabel('Select a city then click button')
        pnl.add(self.label5,BorderLayout.CENTER)
        """
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)
        frame.setVisible(True) 
if __name__ == '__main__':
	Modifier()