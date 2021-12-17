# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import requests as r
import pandas as pd
os.chdir('/home/gonik/Documents/test_recon')

#url = 'http://worksiweb.com.ar:8083/?url_data=https://raw.githubusercontent.com/egonik-unlp/random_projects/master/imagenes_prueba_gv/{}.jpg'
#url = 
dataframes =[]
for i in range(32):
    url_img = 'https://raw.githubusercontent.com/egonik-unlp/random_projects/master/imagenes_prueba_gv/{}.jpg'.format(i)
    url_data = 'url'
    resp = r.post('http://0.0.0.0:80/', json = {
        'url_img' : url_img,
        'url_data' : url_data
    })
    d = resp.json()
    df = pd.DataFrame(d['ingredientes'], columns = ['ingredientes de imagen_{}'.format(i), 'puntaje'])
    with open('reconocidos_imagen_{}.txt'.format(i), 'w') as file:
        file.write(' '.join(d['reconocimiento_crudo']['reconocimiento_ocr']))
    dataframes.append(df)
    
df = pd.concat(dataframes, axis=1)
df.to_excel('reconocimiento_imagenes_demo.xlsx')