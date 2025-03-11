# importamos el modulo unittest para realizar las pruebas
import unittest

# importamos las clases a testear
from gestor_tarea import Tarea, GestorTarea

# definir la clase de pruebas de GestorTarea
class TextGestorTareas(unittest.TestCase):
    def setUp(self):
        # creamos una nueva instancia para GestorTarea para cada prueba
        self.gestor = GestorTarea()

        # Agregamos algunas tareas de prueba para que las pruebas puedan interactuar con ellas
        self.tarea1 = self.gestor.agregar_tarea("Realizar tarea", "Elaborar tarea de testing", "normal")
        self.tarea2 = self.gestor.agregar_tarea("Estudiar python", "Pruebas unitarias", "baja")
        self.tarea3 = self.gestor.agregar_tarea("Proyecto integradora", "Avanzar con la pagina TimeFit", "alta")

    def test_agregar_tarea(self):
        # agregamos una tarea nueva con valores de prueba
        tarea = self.gestor.agregar_tarea("Prueba", "Descripcion de prueba")

        # Comprobamos que la tarea se haya agregado a la lista de tareas del gestor
        self.assertIn(tarea, self.gestor.tareas)

        # Verificamos que los valores de la tarea coincidan con los que se especificaron al agregarla
        self.assertEqual(tarea.titulo, "Prueba")
        self.assertEqual(tarea.descripcion, "Descripcion de prueba")
        self.assertEqual(tarea.prioridad, "normal")  # Valor por defecto si no se especifica otro
        self.assertFalse(tarea.completada)  # Por defecto, la tarea no debe estar completada

        # verificar que el ID sea el siguiente en la secuencia (4), ya que hay 3 tareas previamente agregadas
        self.assertEqual(tarea.id, 4)

    # creamos la prueba para eliminar una tarea, en este caso la tarea 1
    def test_eliminar_tarea(self):
        # Eliminamos la tarea usando su ID y guardamos el resultado (debe ser True si se elimina correctamente)
        resultado = self.gestor.eliminar_tarea(self.tarea1.id)

        # Comprobamos que el resultado de la eliminación es True
        self.assertTrue(resultado)
        
        # Comprobamos que la tarea eliminada no está presente en la lista de tareas
        self.assertNotIn(self.tarea1, self.gestor.tareas)

    # creamos la prueba para eliminar una tarea que no existe
    def test_eliminar_tarea_inexistente(self):
        # Intentamos eliminar una tarea con un ID que no existe
        resultado = self.gestor.eliminar_tarea(1010)

        # Verificamos que el método retorne False, ya que no se puede eliminar una tarea inexistente
        self.assertFalse(resultado)

    # creamos la prueba para buscar una tarea que existe
    def test_buscar_tarea(self):
        # Buscamos una tarea por su ID (1) y guardamos el resultado
        busqueda = self.gestor.buscar_tarea(1)

        # Comparamos el resultado de la búsqueda con la tarea que agregamos en setUp, debe ser la misma
        self.assertEqual(busqueda, self.tarea1)

    # creamos la prueba para una tarea inexistente
    def test_buscar_tarea_inexistente(self):
        # Intentamos buscar una tarea con un ID que no existe (20)
        busqueda = self.gestor.buscar_tarea(20)

        # Como la tarea no existe, debe devolver None
        self.assertIsNone(busqueda)

    # creamos la prueba para marcar una tarea como completada
    def test_marcar_tarea(self):
        # Intentamos marcar la tarea con ID 1 como completada
        marcada = self.gestor.completar_tarea(1)

        # Comprobamos que la función devuelva True, indicando que la tarea fue marcada exitosamente
        self.assertTrue(marcada)

    # creamos la prueba para marcar una tarea inexistente como completada
    def test_marcar_tarea_inexistente(self):
        # Intentamos marcar como completada una tarea con ID que no existe (45)
        marcada = self.gestor.completar_tarea(45)

        # Comprobamos que la función devuelva False, indicando que no se pudo marcar como completada
        self.assertFalse(marcada)


    def test_enlistar_tareas(self):
        resultado = self.gestor.enlistar_tareas()
        self.assertEqual(len(resultado), 3)

        self.assertIn(self.tarea1, resultado)
        self.assertIn(self.tarea2, resultado)
        self.assertIn(self.tarea3, resultado)


    def test_enlistar_tareas_pendientes(self):

        self.gestor.completar_tarea(1)

        tareasPendientes= self.gestor.enlistar_tareas_pendientes()

        self.assertEqual(len(tareasPendientes), 2)
        self.assertNotIn(self.tarea1, tareasPendientes)
        self.assertIn(self.tarea2, tareasPendientes)
        self.assertIn(self.tarea3, tareasPendientes)

    
    def test_filtro_por_prioridad(self):

        tareaNormal = self.gestor.filtrar_prioridad("normal")

        self.assertEqual(len(tareaNormal), 1)
        self.assertIn(self.tarea1, tareaNormal)


        tareaBaja = self.gestor.filtrar_prioridad("baja")

        self.assertEqual(len(tareaBaja), 1)
        self.assertIn(self.tarea2, tareaBaja)
        

        tareaAlta = self.gestor.filtrar_prioridad("alta")

        self.assertEqual(len(tareaAlta), 1)
        self.assertIn(self.tarea3, tareaAlta)


    def test_prioridad_invalida(self):
        # Intentamos crear una tarea con una prioridad no válida
        with self.assertRaises(ValueError) as context:
            Tarea(1, "Tarea inválida", "Descripción", False, "urgente")  # La prioridad "urgente" no esta implementada dentro del gestor

        # Verificamos que el mensaje de la excepción sea el correcto
        self.assertEqual(str(context.exception), "Prioridad no válida. Debe ser una de: ['baja', 'normal', 'alta']")


    def test_comparar_tareas_iguales(self):
        tarea1= Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        tarea2= Tarea(1, "Tarea de español", "Hacer un diccionario ", True, "normal")

        self.assertEqual(tarea1, tarea2)

    def test_comparar_tareas_diferentes(self):
        tarea1= Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        tarea2= Tarea(2, "Tarea de español", "Hacer un diccionario ", True, "normal")

        self.assertNotEqual(tarea1, tarea2)

    def test_comparar_con_otra_cosa(self):
        tarea1= Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        cosa1= 1234

        self.assertNotEqual(tarea1, cosa1)









if __name__ == '__main__':
    unittest.main()
