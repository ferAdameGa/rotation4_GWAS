# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:09:21 2024

@author: madamega

manhattan plot
"""
import pandas as pd
import glob
import numpy as np
from matplotlib import pyplot as plt
import random
import os
import math
import seaborn as sns

#read file
path='C:/Users/madamega/Downloads/class.assoc.txt'
name="trial"
th=5e-8


full=np.loadtxt(path,delimiter='\t',dtype="U") #complete
#pssed threshold
ind=np.where(full[1:len(full),12].astype(float)<th)[0]
ind=[x+1 for x in ind]
importance=full[ind]
np.savetxt("imp_"+name+'.txt',importance,fmt='%s',delimiter='\t')

#get important columns, chr, pos, pvalue
data=np.loadtxt(path,delimiter='\t',skiprows=1,usecols=[0,2,12])

#negative logarithm of pvalues
manhattan=[-math.log10(data[x,2]) for x in range(0,len(data))]
data=np.c_[data,manhattan]
data2=data.copy()
data2[:,0]=2
data=np.concatenate((data,data2))

#plot
font={'size':40}
chr=np.unique(data[:,0])

for i in range(0,len(chr)):
    data_c=data[np.where(data[:,0]==chr[i])]
    
    fig=plt.figure()
    
    ax=sns.scatterplot(x=data_c[:,1],y=data_c[:,3]) #hue=data[:,0]
    #importance
    # plt.scatter(importance[:,2],
    #              [-math.log10(importance[x,12].astype(float)) for x in range(0,len(importance))],
    #              color='red')
    
    #threshold 
    plt.axhline(y=-math.log10(th), color='r', linestyle='--')
    
    ax.set(xlabel='Position', ylabel='-log10(pvalues)')
    #ax.legend(title='chromosomes')
    plt.title("Manhattan plot "+name+" chr "+str(int(chr[i])))
    plt.rc('font', **font)
    plt.show()
    
    #save full screen
    fig.set_size_inches(32,18)
    plt.savefig(name+str(int(chr[i]))+'.png')
