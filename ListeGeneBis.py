#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import os, sys
import javax.swing as swing
import java.awt as awt
from javax.swing import BorderFactory
from javax.swing.border import EtchedBorder, TitledBorder
from java.awt import Font

from java.awt import TextField, Panel, GridLayout, ComponentOrientation, Label, Checkbox, BorderLayout, Button, Color, FileDialog, Frame, Font

import sys
import os
import time
import glob
import os.path as path
import getpass
import shutil
import random
import math

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class ListeGeneBis(swing.JFrame):

				def __init__(self, listgenes):
					swing.JFrame.__init__(self, title="Genes")
					self.setDefaultCloseOperation(swing.JFrame.DISPOSE_ON_CLOSE)
					self.__listgenes = listgenes
					self.run()

				def run(self):
					self.size = (200,300)
					self.contentPane.layout = awt.BorderLayout()
					line = BorderFactory.createEtchedBorder(EtchedBorder.LOWERED)

					Panel1=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel1.setBorder(line)
					label=swing.JLabel("")
					label.setText("Liste des Genes")
					Panel1.add(label)
					menu = swing.JMenuBar()
					Panel1.add(menu)
					
					Panel2=swing.JPanel(awt.FlowLayout(awt.FlowLayout.CENTER))
					Panel2.setBorder(line)
					self.__displistgenes = swing.JList(self.__listgenes)
					self.__displistgenes.setVisibleRowCount(14)
					self.__displistgenes.setFixedCellWidth(75) 
					Panel2.add(self.__displistgenes)
					barre = swing.JScrollPane(self.__displistgenes)
					Panel2.add(barre)
					
					Panel3=swing.JPanel(awt.FlowLayout(awt.FlowLayout.RIGHT))
					Panel3.setBorder(line)
			


					self.contentPane.add(Panel1, awt.BorderLayout.NORTH)
					self.contentPane.add(Panel2, awt.BorderLayout.CENTER)
					self.contentPane.add(Panel3, awt.BorderLayout.SOUTH)


if __name__ == "__main__":

	listgenes=[]
	gene1 = ("A579")
	gene2 = ("A009")
	gene3 = ("A017")
	gene4 = ("A025")
	gene5 = ("A033")
	gene6 = ("A041")
	gene7 = ("A049")
	gene8 = ("A057")
	gene9 = ("A065")
	gene10 = ("A073")
	gene11 = ("A081")
	gene12 = ("A089")
	

	listgenes=[gene1,gene2,gene3,gene4,gene5,gene6,gene7,gene8,gene9,gene10,gene11,gene12]

	genes = ListeGeneBis(listgenes)
	genes.show()


						