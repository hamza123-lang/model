# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.input("radius") 

""" 
import numpy as np 
from scipy.stats import poisson

alpha=[]
beta=[]



"""  transpose  """

y=[1,1,0]  
x = [
     [1,2,3],
     [4,5,6],
     [7,8,9]
     ] 

for i in range(len(x)) :
    if y[i]==0:
        alpha.append(x[i])
    if y[i]==1:
        beta.append(x[i])
        
        
"""  transpose i to iterate over the features so i can get the means   """
def meanof(matr):      
    p= np.transpose(matr)
    z = [] 
    for o in p:
        z.append(o.mean())
    return z
meanof(alpha)
meanof(beta)

"""l is data  """
l=[[1,4,4],
   [1,2,3],
   [10,11,12]
   ]
def getproba(l,moyenne):
    sa = []
    for a in l :
        
        result = poisson.pmf(k=a, mu=moyenne )
        sa.append(result)
    
        
     
    """get the product of every set of probabilities pr(x1x2x3/y=!!) """
    zabi=[]
    for a in sa:
        np.prod(a)
        zabi.append( np.prod(a))
    
    return zabi    
""" all i have to do now is to repeat this process for y=0 and calculate the priors for 1 and 0 then the retio y=1/y=0 """         
likelihoodzero= getproba(l,meanof(alpha))       
likelihoodone= getproba(l,meanof(beta))
priorzero = 0
priorone  =0
for a in y:
    if a==0:
        priorzero +=1
        
    if a==1:
         priorone +=1
priorzero =priorzero/len(y) 
priorone =priorone/len(y)  
beyesfectorzero = np.multiply(priorzero,likelihoodzero)
beyesfactorone= np.multiply(priorone,likelihoodone) 
prediction = []
for i in range(len(beyesfactorone)) :
    if beyesfactorone[i]>beyesfectorzero[i]:
        prediction.append('1') 
    if beyesfactorone[i]<beyesfectorzero[i]:
         prediction.append('0')    


print(prediction)


        
        
   

        
        
      
   
