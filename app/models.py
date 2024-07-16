from enum import Enum,auto
from collections import namedtuple

Datos_Entrada=namedtuple("datos_entrada",("precio","edad_maxima"))
class TipoEntrada(Enum):
    BEBE=Datos_Entrada(0,3)
    NIÑO=Datos_Entrada(14,13)
    ADULTO=Datos_Entrada(23,63)
    JUBILADO=Datos_Entrada(18,100)
  

class Entrada:
    def __init__(self,edad:int):
        if edad<0 or edad>=100:
            validate_entrada(edad)
        
        for tipo in TipoEntrada:
            if edad<=tipo.value.edad_maxima:
                self.tipo=tipo
                break

        self.edad=edad
        self.precio=self.tipo.value.precio
        
def validate_entrada(edad):
    if edad<0:
     raise NegativeNumber("Las edades no pueden ser negativas")
    elif  edad>=100:
     raise MayorQue100Exception("Las edades no pueden ser superiores a 100")
    
class TiketsGroup():
    def __init__(self):
        self.total=0
        self.num_entradas=0
        self.type_tickets={x:0 for x in TipoEntrada }

    def type_tickets(self):
        result={}
        for x in TipoEntrada:  
            result.update({x:0} )       
            
        return result
            
        

    def add_ticket(self,n):
        tiket=Entrada(n)
        self.total+=tiket.precio
        self.num_entradas+=1
        self.type_tickets[tiket.tipo]+=1

    def count_type_tickets(self,tipo):
        return self.type_tickets[tipo]
    
    def subtotal_for_type(self,tipo):
        return self.type_tickets[tipo]*tipo.value.precio
    

class MayorQue100Exception(Exception):
    pass
class NegativeNumber(Exception):
    pass













        
        
