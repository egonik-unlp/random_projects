#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Este programa recorre la carpeta indicada y parsea archivos con la extensión `.fa` conteniendo secuencias en formato FASTA, exportando la metadata en
otro archivo. Dado un archivo `algo.fa`, se guardará en un archivo `algo.fa_out`.
----------
This short script reads all FASTA-formatted files with the `.fa` extension, and returns files containing sequence metadata. Given
a file named `foo.fa`, a filed named `foo.fa_out` will be generated. A path can be provided as an argument.

'''

import re
import os
import sys



def process_file(contig_file):
    with open(contig_file) as file:
        write_file=open("{}_out".format(file.name), 'w')
        print("\t Procesando archivo {} guardando output en {} ".format(file.name, write_file.name))
        for line in file.readlines():
            pattern=re.match(r"^>.*\n$", line)
            if pattern:
                write_file.write(pattern.string)
        write_file.close()
def parse_folder(path):
    for file in os.listdir(path):
        if file[-3:]=='.fa':
            process_file(os.path.join(path, file) )

if __name__=='__main__':
    if len(sys.argv) > 1:
        parse_folder(sys.argv[1])
        print("Procesando archivos de la carpeta {} ".format(sys.argv[1]))
    elif len(sys.argv)==1:
        print("Procesando carpeta actual")
        parse_folder('.')
    else:
        print("Uso incorrecto, uso correcto \n {}, `archivo a procesar`".format(sys.argv[0]))
