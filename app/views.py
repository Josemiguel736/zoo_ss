from simple_screen import locate, Print,Screen_manager,cls,Input
from app.models import TiketsGroup,TipoEntrada
"""
 123456789012345678901234567890123456789
 TIPO             PU     Q        TOTAL
 =======================================
 BEBE <2          0.00   99       9999.99
 NIÑO <2          0.00   99       9999.99
 ADULTO <2        0.00   99       9999.99
 JUBILADO <2      0.00   99       9999.99
---------------------------------------------
                         999      9999.99

 EDAD:
 CONF
"""

class VistaGrupo:
    def __init__(self,grupo: TiketsGroup,x=1,y=0):
        self.grupo=grupo
        self.x=x
        self.y=y

    def paint(self):
        locate(self.x,self.y,"TIPO                  Pv     Q       TOTAL")
        locate(self.x,self.y+2,"============================================")
        
        for indice,tipo in enumerate(TipoEntrada):
           
         locate(self.x,self.y+3+indice,f" {tipo.name: <20s}{tipo.value.precio:5.2f}   {self.grupo.count_type_tickets(tipo)}      {self.grupo.subtotal_for_type(tipo):5.2f}")
         locate(self.x,self.y+8,"---------------------------------------------")

         locate(self.x,self.y+9,f"                    ENTRADAS {self.grupo.num_entradas}     {self.grupo.total:6.2f}")

class Entry:
   def __init__(self,label:str,x,y):
      self.label=label
      self.x=x
      self.y=y
      
   
   def paint(self):
      locate(self.x,self.y,self.label)
      value=Input()
      return value

   



  
  
  



