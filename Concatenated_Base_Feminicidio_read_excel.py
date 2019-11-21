# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 02:11:02 2019

@author: carlo
"""



import os
import pandas as pd
#import numpy as np
import glob

def concatenate(indir="E:\\datasets\\seg_publica\\base_teste",outfile="E:\\datasets\\seg_publica\\base_teste\\Base_Feminicidio_2019.xlsx"):
#def concatenate(indir="C:\\in\\Extracted",outfile="C:\\out\\Concatenated.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.xlsx")
    #criação do dataframe 
    dfList=[]
    #colnames=["nome","idade"]
    for filename in fileList:
        print(filename)
        df=pd.read_excel(filename)
        dfList.append(df)
    concatDf=pd.concat(dfList,axis=0) 
    #concatDf.columns=colnames
    concatDf.to_excel(outfile,index=None)