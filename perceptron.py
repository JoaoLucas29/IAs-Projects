import os
import numpy as np

os.system("cls")
from random import uniform

dados = np.array([
    [-1, 0, 0, 0],
    [-1, 0, 1, 0],
    [-1, 1, 0, 0],
    [-1, 1, 1, 1]
])

n = 0.6
ne = 3
w=[]
na = len(dados)

i = 0
while i != ne:
    rand = uniform(0,1)
    w.append(rand)
    i+=1

w = np.array(w)

flag = 1
while(flag == 1):
    flag = 0
    cont = 0

    for am in range(na):
        x=dados[am,0:ne]
        tg=dados[am][3] 
        E=np.dot(x,w) #ou X@W
    
        if E >= 0:
            net = 1
        else:
            net = 0
        D = tg - net
        if D == 0:
            cont +=1
        dw = n*D*x
        w = w+dw
        
        print(f"Tg:{tg}, net:{net}")
    if cont<4:
        flag=1
    print("-----------------------------------------------------------------")