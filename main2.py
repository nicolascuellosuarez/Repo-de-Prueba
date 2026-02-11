from datetime import datetime
from rich.console import Console
from rich.table import Table
from typing import List, override

class Tarea:
    """
    Representa una tarea
    """

    def __init__(self, titulo: str, descripción: str, prioridad: str):
        self.titulo: str = titulo
        self.descripción: str = descripción
        self.__completado: bool = False
        self.fecha_creacion = datetime.now()
        self.prioridad: str = prioridad

    def marcar_completada(self) -> bool:
        """
        Cambio de estado de tarea
        """
        if not self.__completado:
            self.__completada = True
        return self.__completado
    
    def extras_tabla(self) -> dict:
        return {}

    @property
    def estado(self) -> str:
        """
        Getter temático para mostrar el estado de manera limpia
        """
        return "Completada" if self.__completado else "Pendiente"
    
    def revisar_prioridad(self) -> None:
        prioridades = ["Alta", "Media", "Baja"]
        if self.prioridad not in prioridades:
            raise ValueError("La prioridad no es válida")
        
class TareaAcademica(Tarea):
    def __init__(self, titulo: str, 
                 descripción: str, 
                 prioridad: str, 
                 materia: str, 
                 fecha_entrega: str):
        super().__init__(titulo, descripción, prioridad)
        self.__completado: bool = False
        self.fecha_creacion = datetime.now()
        self.materia: str = materia
        self.fecha_entrega: str = fecha_entrega

    def extras_tabla(self) -> dict[str, str]:
        return {"Materia": self.materia,
                "Fecha de Entrega": self.fecha_entrega}


class GestorTareas:
    """
    Clase controladora, para la gestión de tareas
    """
    def __init__(self):
        self.tareas: list[Tarea] = []
        self.console = Console()

    def agregar_tarea(self, tarea: Tarea) -> None:
        self.tareas.append(tarea)
        print(f"Tarea {tarea.titulo} agregada con éxito.")

    def mostrar_tablero(self) -> None:
        columnas_extra = set()
        for tarea in self.tareas:
            columnas_extra.update(tarea.extras_tabla().keys())

        table = Table(title = "Tablero de Tareas")
        table.add_column("Titulo", style="cyan")
        table.add_column("Estado", justify= "center")
        table.add_column("Creada el", style="magenta")
        table.add_column("Prioridad", style="magenta")
        columnas_extra = list(columnas_extra)
        for columna in columnas_extra:
            table.add_column(columna, style = "green")

        for tarea in self.tareas:
            fila = [
                tarea.titulo, 
                tarea.estado, 
                tarea.fecha_creacion.strftime("%Y-%m-%d %H:%M"),
                tarea.prioridad
            ]
            
            extras = tarea.extras_tabla()
            for col in columnas_extra:
                fila.append(extras.get(col, "—"))

            table.add_row(*fila)
        self.console.print(table)

    def eliminar_tarea(self, nombre: str) -> None:
        for tarea in self.tareas:
            if tarea.titulo == nombre:
                self.tareas.remove(tarea) 

def main():
    tarea_calculo = Tarea("Tarea 1", "Instalar Kernel de C", "Alta")
    tarea_fisica = Tarea("Tarea 2", "Uso de NumPy", "Alta")
    tarea_POO = TareaAcademica("Tarea 3", "Uso de Herencia", "Alta", "POO", "13/02/2025")
    tarea_EDD = TareaAcademica("Tarea 4", "Uso de memoria Heap y Stack", "Media", "EDD", "03/02/2025")
    mi_gestor = GestorTareas()
    mi_gestor.agregar_tarea(tarea_calculo)
    mi_gestor.agregar_tarea(tarea_fisica)
    mi_gestor.agregar_tarea(tarea_EDD)
    tarea_calculo.marcar_completada()
    mi_gestor.mostrar_tablero()
    mi_gestor.eliminar_tarea("Tarea 2")
    mi_gestor.mostrar_tablero()
    
if __name__ == "__main__":
    main()