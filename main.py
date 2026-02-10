class Pizza:
    def __init__(self, ingredientes: list[str]):
        self.ingredientes: list[str] = ingredientes

    """
    Factor g
    """

    @classmethod
    def crear_hawaiana(cls) -> 'Pizza':
        return cls(["Queso", "Piña, Jamón"])
    
def main():
    pizza_1 = Pizza(["Chicharrón", "Queso", "Pepperoni"])
    pizza_hawaiana = Pizza.crear_hawaiana()

    print(pizza_1.ingredientes)
    print(pizza_hawaiana.ingredientes)

if __name__ == "__main__":
    main()