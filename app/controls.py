
from app.models import TiketsGroup,MayorQue100Exception,NegativeNumber
from simple_screen import Screen_manager,cls,DIMENSIONS,Print,locate,Input
from app.views import VistaGrupo, Entry



class Zoo:
  def __init__(self):
    
   self.grupo=TiketsGroup()
   self.x=(DIMENSIONS.w-37)//2
   self.y=1
   self.vedad=Entry("Por favor ingrese su edad: ",self.x,12)
   self.vseguir=Entry("Pulsa (s) para salir, (n) para añadir otra entrada: ",self.x,14)
   

  def run(self):
     self.vg=VistaGrupo(self.grupo,self.x,self.y)
     with Screen_manager:  
      while True:  
       cls()
       self.vg.paint()
       inp=self.vedad.paint()
       if inp=="":
          seguir=self.vseguir.paint()
          if seguir.upper()=="N":
            self.grupo=TiketsGroup()
            self.vg=VistaGrupo(self.grupo,self.x,self.y)
            continue
        
       
          if seguir.upper()=="S":
           break
       else:
        try:
         self.grupo.add_ticket(int(inp))
        except MayorQue100Exception:
          locate(self.x,14,"Las edades no pueden ser superiores a 100")
          Input()
        except NegativeNumber:
          locate(self.x,14,"Las edades no pueden ser negativas")
          Input()
        except ValueError:
          locate(self.x,14,"Por favor ingrese una edad valida")
          Input()       
    
  
     
     
    