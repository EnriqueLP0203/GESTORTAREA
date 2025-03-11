# importamos el modulo unittest para realizar las pruebas
import unittest

# importamos las clases a testear
from gestor_tarea import Tarea, GestorTarea

# definir la clase de pruebas de GestorTarea
class TextGestorTareas(unittest.TestCase):
    def setUp(self):
        # Creamos una nueva instancia para GestorTarea para cada prueba
        self.gestor = GestorTarea()

        # Agregamos algunas tareas de prueba para que las pruebas puedan interactuar con ellas
        self.tarea1 = self.gestor.agregar_tarea("Realizar tarea", "Elaborar tarea de testing", "normal")
        self.tarea2 = self.gestor.agregar_tarea("Estudiar python", "Pruebas unitarias", "baja")
        self.tarea3 = self.gestor.agregar_tarea("Proyecto integradora", "Avanzar con la pagina TimeFit", "alta")

    # Prueba para agregar tareas
    def test_agregar_tarea(self):
        # Agregamos una tarea nueva
        tarea = self.gestor.agregar_tarea("Prueba", "Descripcion de prueba")
        # Verificamos que la tarea se haya agregado correctamente
        self.assertIn(tarea, self.gestor.tareas)
        self.assertEqual(tarea.titulo, "Prueba")
        self.assertEqual(tarea.descripcion, "Descripcion de prueba")
        self.assertEqual(tarea.prioridad, "normal")
        self.assertFalse(tarea.completada)
        self.assertEqual(tarea.id, 4)

    # Prueba para eliminar una tarea existente
    def test_eliminar_tarea(self):
        resultado = self.gestor.eliminar_tarea(self.tarea1.id)
        self.assertTrue(resultado)
        self.assertNotIn(self.tarea1, self.gestor.tareas)

    # Prueba para intentar eliminar una tarea que no existe
    def test_eliminar_tarea_inexistente(self):
        resultado = self.gestor.eliminar_tarea(1010)
        self.assertFalse(resultado)

    # Prueba para buscar una tarea existente
    def test_buscar_tarea(self):
        busqueda = self.gestor.buscar_tarea(1)
        self.assertEqual(busqueda, self.tarea1)

    # Prueba para buscar una tarea inexistente
    def test_buscar_tarea_inexistente(self):
        busqueda = self.gestor.buscar_tarea(20)
        self.assertIsNone(busqueda)

    # Prueba para marcar una tarea como completada
    def test_marcar_tarea(self):
        marcada = self.gestor.completar_tarea(1)
        self.assertTrue(marcada)

    # Prueba para intentar marcar una tarea inexistente como completada
    def test_marcar_tarea_inexistente(self):
        marcada = self.gestor.completar_tarea(45)
        self.assertFalse(marcada)

    # Prueba para enlistar todas las tareas
    def test_enlistar_tareas(self):
        resultado = self.gestor.enlistar_tareas()
        self.assertEqual(len(resultado), 3)
        self.assertIn(self.tarea1, resultado)
        self.assertIn(self.tarea2, resultado)
        self.assertIn(self.tarea3, resultado)

    # Prueba para enlistar solo tareas pendientes
    def test_enlistar_tareas_pendientes(self):
        self.gestor.completar_tarea(1)
        tareasPendientes = self.gestor.enlistar_tareas_pendientes()
        self.assertEqual(len(tareasPendientes), 2)
        self.assertNotIn(self.tarea1, tareasPendientes)
        self.assertIn(self.tarea2, tareasPendientes)
        self.assertIn(self.tarea3, tareasPendientes)

    # Prueba para filtrar tareas por prioridad
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

    # Prueba para verificar la prioridad invalida
    def test_prioridad_invalida(self):
        with self.assertRaises(ValueError) as context:
            Tarea(1, "Tarea inválida", "Descripción", False, "urgente")
        self.assertEqual(str(context.exception), "Prioridad no válida. Debe ser una de: ['baja', 'normal', 'alta']")

    # Prueba para comparar tareas iguales
    def test_comparar_tareas_iguales(self):
        tarea1 = Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        tarea2 = Tarea(1, "Tarea de español", "Hacer un diccionario", True, "normal")
        self.assertEqual(tarea1, tarea2)

    # Prueba para comparar tareas diferentes
    def test_comparar_tareas_diferentes(self):
        tarea1 = Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        tarea2 = Tarea(2, "Tarea de español", "Hacer un diccionario", True, "normal")
        self.assertNotEqual(tarea1, tarea2)

    # Prueba para comparar un objeto tarea con algo que no es tarea
    def test_comparar_con_otra_cosa(self):
        tarea1 = Tarea(1, "Tarea de metricas", "Hacer el reporte de los codigos de prueba", False, "normal")
        cosa1 = 1234
        self.assertNotEqual(tarea1, cosa1)

if __name__ == '__main__':
    unittest.main()
