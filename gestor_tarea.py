# Definimos la clase Tarea para representar una tarea individual
class Tarea:
    def __init__(self, id, titulo, descripcion="", completada=False, prioridad="normal"):
        # Asignamos los valores básicos de la tarea
        self.id = id  # Identificador único para la tarea
        self.titulo = titulo  # Título de la tarea
        self.descripcion = descripcion  # Descripción opcional de la tarea
        self.completada = completada  # Estado de la tarea (True si está completada, False si no)

        # Definimos las prioridades válidas para la validación
        prioridades_validas = ['baja', 'normal', 'alta']

        # Verificamos que la prioridad proporcionada sea válida
        if prioridad not in prioridades_validas:
            raise ValueError(f"Prioridad no válida. Debe ser una de: {prioridades_validas}")

        # Asignamos la prioridad si pasó la validación
        self.prioridad = prioridad

    # Método para comparar dos objetos Tarea por su ID
    def __eq__(self, other):
        if not isinstance(other, Tarea):  # Si el otro objeto no es de tipo Tarea, retornamos False
            return False
        return self.id == other.id  # Compara si ambos objetos Tarea tienen el mismo ID


# La clase GestorTarea maneja una colección de objetos Tarea
class GestorTarea:
    def __init__(self):
        # Lista para almacenar todas las tareas creadas
        self.tareas = []

        # Contador para asignar IDs únicos a las tareas de manera incremental
        self.contador_id = 0

    # Método para agregar una nueva tarea al gestor
    def agregar_tarea(self, titulo, descripcion="", prioridad="normal"):
        # Incrementamos el contador para obtener un nuevo ID único
        self.contador_id += 1

        # Creamos la nueva tarea con los parámetros proporcionados
        nueva_tarea = Tarea(self.contador_id, titulo, descripcion, False, prioridad)

        # Añadimos la tarea a nuestra lista de tareas
        self.tareas.append(nueva_tarea)
        
        # Retornamos la tarea creada para que pueda ser utilizada por otras funciones
        return nueva_tarea
    
    # Método para eliminar una tarea por su ID
    def eliminar_tarea(self, id_tarea):
        # Buscamos la tarea dentro de la lista de tareas
        for tarea in self.tareas:
            # Si encontramos la tarea con el ID especificado, la eliminamos de la lista
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True  # Indicamos que la tarea fue eliminada con éxito
        
        # Si no encontramos ninguna tarea con ese ID, retornamos False
        return False
    
    # Método para buscar una tarea específica por su ID
    def buscar_tarea(self, id_tarea):
        # Recorremos la lista de tareas para buscar la tarea que coincida con el ID proporcionado
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                return tarea  # Retornamos la tarea encontrada
        
        # Si no se encuentra ninguna tarea con ese ID, retornamos None
        return None

    # Método para marcar una tarea como completada
    def completar_tarea(self, id_tarea):
        # Buscamos la tarea en la lista de tareas
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                tarea.completada = True  # Marcamos la tarea como completada
                return True  # Indicamos que la operación fue exitosa
        
        # Si no se encuentra la tarea, retornamos False
        return False
    

    # Método para enlistar todas las tareas
    def enlistar_tareas(self):
        # Retornamos la lista completa de tareas almacenadas en el gestor
        return self.tareas
    

    # Método para enlistar tareas pendientes
    def enlistar_tareas_pendientes(self):
        # Generamos una lista que contiene solo las tareas que no están completadas
        tareas_pendientes = [tarea for tarea in self.tareas if not tarea.completada]
        
        # Retornamos la lista de tareas pendientes
        return tareas_pendientes
    

    # Método para filtrar tareas por prioridad
    def filtrar_prioridad(self, prioridad):
        # Generamos una lista que contiene solo las tareas con la prioridad que se busca
        tareas_filtradas = [tarea for tarea in self.tareas if tarea.prioridad == prioridad]
        
        # Retornamos la lista de tareas filtradas por prioridad
        return tareas_filtradas
