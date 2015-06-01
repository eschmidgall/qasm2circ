# qasmAutoDoAll.py - An Automated Script for qasm2circ-v1.4
# ========================
# Author: E. R. Schmidgall
# Date: 01-Jun-2015
# Version: 1.0.0
# License: GNU Public v2.0
# Software may be modified and redistributed. It is distributed without
# any warranty, without even the implied warranty of mechantiblity or
# fitness for a particular purpose.
#
# ==========================

import os
import glob
import fileinput
import sys
import qasm2texLib as qlib


def main(pathName):

    fileList = []

    if os.path.isdir(pathName):
        fileList = glob.glob(pathName+'\\*.qasm')

    if os.path.isfile(pathName) and pathName.endswith('.qasm'):
        fileList = [pathName]
        pathName = os.path.dirname(pathName)

    if not fileList:
        print("Provide a directory or a .qasm file path")
        return
    
    for f in fileList:

        tmp = os.path.splitext(f)
        saveFname = tmp[0]+'.tex'
        
        qp = qlib.qasm_parser(fileinput.input(f))
        qc = qlib.qcircuit(qp.nametab,qp.typetab)
        for g in qp.gatetab:
            qc.add_op(g)

        if os.path.exists(saveFname):   #Don't overwrite files automatically. Skip the file. 
            print("File name "+saveFname+" already exists.")
            continue
        
        qc.output_sequence(saveFname)
        qc.output_matrix(saveFname)
        qc.output_latex(saveFname)

        os.system('pdflatex '+saveFname +' -output-directory='+pathName) 
        


if __name__ == "__main__":
    main(sys.argv[1])
    
                     
