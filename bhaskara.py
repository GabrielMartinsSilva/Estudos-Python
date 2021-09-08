import math
from decimal import *

def bhaskara():    
    entrada = input().split() 
    
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])    
    
    delta = ((b*b) - (4*a*c))    

    if a == 0 or delta <0: 
        print("Impossivel calcular")
    else:     
        R1 = (-b + math.sqrt(delta))/(2*a)               
        R2 = (-b - math.sqrt(delta))/(2*a)

        print("R1 = {:.5f}". format(R1))
        print("R2 = {:.5f}". format(R2))
        

bhaskara()            

            