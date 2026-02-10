from abc import ABC, abstractmethod
from typing import final

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self): ... 
    @final
    def mensaje_transaccion(self) -> None:
        print("Transacción Completada")

class PagoPaypal(MetodoPago):
    def __init__(self, email: str) -> None:
        self.email: str = email

    def procesar_pago(self, monto: float) -> None:
        print(f"Pago con correo {self.email} hecho por ${monto}")

class PagoTarjeta(MetodoPago):
    def __init__(self, numero_tarjeta: str) -> None:
        self.numero_tarjeta: str = numero_tarjeta
    
    def procesar_pago(self, monto: float) -> None:
        print(f"Pago con Tarjeta {self.tarjeta} hecho por ${monto}")

class Procesador:
    def __init__(self, pagos: list[MetodoPago]) -> None:
        self.pagos: list[MetodoPago] = pagos
    
    def procesar_pagos(self):
        for pago in self.pagos:
            pago.mensaje_transaccion()

class Pizza:
    def __init__(self, ingredientes: list[str]):
        self.ingredientes: list[str] = ingredientes

    """
    Factory o Fábrica, Patrón de diseño
    """

    @classmethod
    def crear_hawaiana(cls) -> 'Pizza':
        return cls(["Queso", "Piña, Jamón"])
    

    
def main():
    pizza_1 = Pizza(["Chicharrón", "Queso", "Pepperoni"])
    pizza_hawaiana = Pizza.crear_hawaiana()
    print(pizza_1.ingredientes)
    print(pizza_hawaiana.ingredientes)

    paypal_1 = PagoPaypal("jaimecuellosuarez@gmail.com")
    tarjeta_1 = PagoTarjeta("1234 4567 1235")

    paypal_1.procesar_pago(300)
    paypal_1.mensaje_transaccion()
    procesador = Procesador([paypal_1, tarjeta_1])
    procesador.procesar_pagos()

if __name__ == "__main__":
    main()