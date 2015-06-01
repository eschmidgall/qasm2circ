# qasm2circ
This library is Issac Chuang's qasm2circ library with the following modifications: 

1. qasm2tex.py has been replaced by a library version, qasm2texLib.py that functions as a python library. 
2. qasm2texLib.py writes to tex files directly from the library instead of via stdout. 
3. qasmAutoDoAll.py is a Windows-compatible multifile script that can convert all the .qasm files in a directory to .pdf directly. 

==============================
Requirements: 
-Python 2.7 (should also be compatible with Python 3, though I have not tested it on this python version). 
-Latex2e with xypic (included)
-pdflatex 

For more information about the qasm2circ file format, see the original readme (included). 

=============================
Syntax: 

python qasmAutoDoAll.py <directory>   : Converts all .qasm files in the directory to pdf. 
python qasmAutoDoAll.py <file.qasm>   : Converts a specific .qasm file to pdf. 

Example: 
python qasmAutoDoAll.py C:\users\foo\qasmfiles\   : Converts all .qasm files in C:\users\foo\qasmfiles to .pdf
python qasmAutoDoAll.py .   : Converts all .qasm files in the python script directory to .pdf
python qasmAutoDoAll.py C:\users\foo\qasmfiles\test1.qasm : Converts only test1.qasm to .pdf

In all cases, the pdf file is saved in the same directory as the .qasm file, and the .tex and .pdf file names match the .qasm file name. 
