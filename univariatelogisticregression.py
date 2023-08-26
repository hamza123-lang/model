# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:39:00 2023

@author: hamza
"""
import numpy as np
x=[5,6,7,8,10]
y=[0,0,1,1,1] 
w=0
b=0
alpha = 0.01
def sigmoid(z):
    return 1/(1+np.exp(-z))
for j in range(50000):
    dw=0
    db=0
    for i in range(len(x)):
        dw=dw + (sigmoid(w*x[i]+b )-y[i])*x[i]
        db=db + (sigmoid(w*x[i]+b ) -y[i])
    w=w-alpha*dw
    b=b-alpha*db
print(w)
print(b)    
        
        