#!/usr/bin/python
# -*- coding: iso-8859-15 -*-


import sys
import os

import os.path as path
import getpass
import shutil

username=getpass.getuser()

mypath=os.path.expanduser(os.path.join("~","Dropbox","Macros_Lisa","Code_VRD"))
sys.path.append(mypath)

from Fenetre import Fenetre


from org.python.core import codecs
codecs.setDefaultEncoding('utf-8')


class VRD_Tools(object):
	fenetre = Fenetre()
	fenetre.dossier = "/Users/lisalamasse/Desktop/Metasensors HCS/Bacillus_Ibidi_96well_angio1"
	fenetre.nomb = "20130410_162617_825"
	fenetre.show()

if __name__ == "__main__":
	vrd = VRD_Tools()

