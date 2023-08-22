# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.input("radius") 

""" 
import numpy as np
f= [[1,1],
    [1,-1],
    [-1,1],
    [-1,-1],
    [-1.5,0.5],
    [-2,-2],
    [-1,0.5]
    
    ]

    
y=[1,1,1,-1,-1,-1,-1]


def perceptron(f,y):
    
    z= np.ones((len(f),1))
    x= np.append(f,z,axis=1)
    m , n  = np.array(f).shape
    w=np.ones(n+1)
    a=None 
    for j in range(10000) :
        a=0
        for i in range(len(y)):
            if np.dot(x[i],w)*y[i]<0:
                w +=np.multiply(x[i],y[i])
                a+=1
                
        if a==0 :
             break 
       
    return w
   
        
def predict(t):
    
    for a in t :
        if np.dot(perceptron(f, y),a ) <0 :
            print(-1)
        if np.dot(perceptron(f, y),a ) >0:
            print(1)
predict([ [2,2,1],
         [-4,-4,1]
    
    ])

        
        
      
   
