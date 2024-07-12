from enum import Enum,auto
class TipoEntrada(Enum):
    BEBE=0
    NIÑO=14
    ADULTO=23
    JUBILADO=18

class Entrada:
    def __init__(self,edad:int):
        if edad<0:
            raise ValueError("Las edades no pueden ser negativas")
        
        elif edad>=0 and edad <=3:
            self.tipo=TipoEntrada.BEBE
        
        elif edad<=13:
            self.tipo=TipoEntrada.NIÑO
            
        elif edad<=63:
            self.tipo=TipoEntrada.ADULTO
            
        elif edad>=64:
            self.tipo=TipoEntrada.JUBILADO



        self.edad=edad
        self.precio=self.tipo.value
        
class TiketsGroup():
    def __init__(self):
        self.total=0
        self.num_entradas=0
        self.type_tickets={TipoEntrada.BEBE:0,
                           TipoEntrada.NIÑO:0,
                           TipoEntrada.ADULTO:0,
                           TipoEntrada.JUBILADO:0}
        

    def add_ticket(self,n):
        tiket=Entrada(n)
        self.total+=tiket.precio
        self.num_entradas+=1
        self.type_tickets[tiket.tipo]+=1

    def count_type_tickets(self,tipo):
        return self.type_tickets[tipo]
    
    def subtotal_for_type(self,tipo):
        return self.type_tickets[tipo]*tipo.value
    


group=TiketsGroup()
group.add_ticket(12)
print(group.subtotal_for_type(TipoEntrada.NIÑO))





        




        
        
