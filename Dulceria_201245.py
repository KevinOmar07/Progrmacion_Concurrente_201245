from random import random
import threading
import time
import random

cantidad_clientes = 0;

class Dulceria_Cine():
    def __init__(self, cliente = 0):
        self.locked = threading.Lock()
        self.cliente_num = cliente
        
    def realizar_venta(self, espera):
        self.locked.acquire()
        
        try:
            self.cliente_num += 1
            print("----------------------------------------------------------------------")
            print(f"Cliente num: {self.cliente_num}")
            if self.cliente_num < cantidad_clientes:
                print(f"Tiempo de espera estimado para el siguiente cliente: {espera}min") 
                ## la variable espera simula el tiempo de espera para que pase el siguiente cliente
            time.sleep(espera) ## La varible espera es un valor del 1 al 9 generado aleatoriamente para simular la espera con la libreria time
        finally:
            if self.cliente_num < cantidad_clientes:
                print("compra finalizada, siguiente cliente")
                print("----------------------------------------------------------------------\n")
            else :
                print("Compra finalizada, ya no hay más clientes")
                print("----------------------------------------------------------------------\n")
            self.locked.release()
            
def func_comprar(x):
    time_f = random.randint(1, 9)
    x.realizar_venta(time_f)
        
if __name__ == '__main__':
    dulceria = Dulceria_Cine()
    cantidad_clientes = int(input("Ingrese cantidad de personas en la cola para la compra de sus productos: "))
    for y in range(cantidad_clientes):
        tstart = threading.Thread(target=func_comprar, args=(dulceria,))
        tstart.start()