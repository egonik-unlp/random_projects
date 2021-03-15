#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import csv
import pandas as pd 
import matplotlib.pyplot as plt
from xyz import main as to_xyz
def generate_file_structure():
    dirs = ['csv', 'tsv', 'xyz', 'trial']
    dirs_created = []
    for dir in dirs:
        try:
            os.mkdir(dir)
            dirs_created.append(dir)
        except FileExistsError:
            pass
    if dirs_created:
        print(f'directorios creados: {", ".join(dirs_created)}')
    else:
        print('no hubo necesidad de crear carpetas adicionales')
def open_file(filename):
    if filename[-4:] == '.dat':
        f = open(filename, 'r', encoding= 'unicode_escape')
        lines = csv.reader(f)
        linea_aux = next(lines)
        l_arch = []
        done = False
        while not done:
            if linea_aux:
                if 'Int' in linea_aux[0]:
                    done = True
            else:
                pass
            linea_aux = next(lines)
        with open(f'tsv/{filename}_int_tsv', 'w') as f:
            while 'LT' not in linea_aux[0]:
                f.write(linea_aux[0])
                f.write('\n')
                linea_aux = next(lines)
            l_arch.append(f.name)
        print(filename)
        with open(f'tsv/{filename}_lt_tsv', 'w') as f:
            for line in lines:
                f.write(line[0])
                f.write('\n')
            l_arch.append(f.name)
        f.close()
    else:
        print(f'no corri con {filename} porque no termina en .dat')
    return l_arch
def to_csv(filename):
    pd.read_csv(filename, delim_whitespace= True, header= None).to_csv(f'csv/{filename[4:-4]}.csv')

def imshow():
    os.chdir('csv')

    try:
        for file in os.listdir():
            if file[-4:] == '.csv':
                dfn = pd.read_csv(file, header= None).to_numpy()
                plt.imshow(dfn)
                plt.savefig(f'{file}.png')
    except Exception:
        pass

def main(folder = '.'):
    os.chdir(folder)
    for file in os.listdir():
        if file[-4:] == '.dat':
            l_arch = open_file(file)
            for files in  l_arch:
                to_csv(files)
    imshow()
    for file in os.listdir():
        if file[-4:] == '.csv':
            print(file)
            to_xyz(file)

def walker(self_dirs):
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        print(dirs)
        for name in dirs:
            if name not in self_dirs + [root]:
                generate_file_structure()
                main(os.path.join(root, name))
if __name__ == '__main__':
    print(os.getcwd())
    walker(['csv', 'tsv', 'xyz', 'trial'])
