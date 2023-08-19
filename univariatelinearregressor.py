import numpy as np 
x= np.array([1,2,3,6,8,6,5])
y=np.array([1,2,4,7,7,8,8])
def univariatelinearregression(x,y):
    w=0
    b=0
    for i in range(100):
        da=0
        db=0
        for j in range(len(x)):
           da=da+ (w*x[j]+b-y[j])*x[j]
           db=db+(w*x[j]+b-y[j] )   
        w=w-0.01*da
        b=b-0.01*db
        print(w)
        print(b)
univariatelinearregression(x, y)    
