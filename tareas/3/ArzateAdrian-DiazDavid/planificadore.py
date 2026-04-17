import random 
from collections import deque 
import copy
from dataclasses import dataclass

@dataclass
class Proceso:
    nombre: str
    tiempo_llegada: int
    tiempo_servicio: int 

    tiempo_restante: int = 0
    tiempo_retorno: int = 0
    tiempo_espera: int = 0

    def __pos_init__(self):
        if self.tiempo_restante == 0:
            self.tiempo_restante = self.tiempo_servicio

print( Proceso('A', 0, 5))
