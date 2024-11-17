import crud
import core
import os
from datetime import datetime 

# Inicialización de variables
dirCreditos = {"data": []}
isMenuActivate = True
current_user = None  # Variable para almacenar el usuario actual
def mostrar_menu():
    os.system('clear')
    print("****************************************") 
    print("*        ¡Menu Principal Créditos      *")
    print("****************************************")
    print("1. Agregar Materia")
    print("2. Consulta de Materias y Créditos Pendientes")
    print("3. Planificación Personalizada de Asignaturas")
    print("4. Calendario Académico Integrado")
    print("5. Malla Curricular Interactiva")
    print("6. Sistema de Alertas para Inscripción de Materias")
    print("7. Acceso a Recursos Académicos")
    print("8. Red de Tutorías Académicas")
    print("9. Consultas a Profesores a través de Foros")
    print("10. Simulador de Exámenes de Biomedicina")
    print("11. Estadísticas de Desempeño Académico")
    print("12. Sistema de Recomendación de Cursos Electivos")
    print("13. Seguimiento del Avance de Tareas y Proyectos")
    print("14. Acceso a Noticias y Eventos Relevantes en Biomedicina")
    print("15. Conexión con Comunidades de Estudiantes de Biomedicina")
    print("16. Sistema de Feedback para la Mejora del Proceso de Aprendizaje")
    print("17. Mostrar creditos acumulados por mes y por año")
    print("18. Mostrar creditos faltantes para graduarse")
    print("19. Mostrar creditos Acumulados")
    print("20. Salir")

    def login():
        global current_user
        while True:
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            if core.login_user(username, password):
                current_user = username
                print(f"Bienvenido {current_user}!")
                break
            else:
                print("Usuario o contraseña incorrectos. Intente nuevamente.")

def register():
    while True:
        username = input("Ingrese un nuevo nombre de usuario: ")
        password = input("Ingrese una nueva contraseña: ")
        
        if core.register_user(username, password):
            print("Registro exitoso.")
            break
        else:
            print("El usuario ya existe. Intente con otro nombre.")

if __name__ == "__main__":
    print("****************************************") 
    print("*                                      *")
    print("* ¡Bienvenidos a Créditos a un Click!  *")
    print("*                                      *")
    print("****************************************")
    os.system("pause")

    if core.checkFile('creditos.json'):
        dirCreditos = core.LoadInfo('creditos.json')
    else:
        core.crearInfo('creditos.json', dirCreditos)
            # Preguntar al usuario si quiere iniciar sesión o registrarse
    action = input("¿Desea (L)ogin o (R)egistrar? (L/R): ").upper()
    
    if action == 'R':
        register()
    elif action == 'L':
        core.login()

    while isMenuActivate:
        mostrar_menu()
        op = int(input())
        
        if op == 1:
           crud.agregarMateria(dirCreditos)  # Ahora agrega materias como completadas
        elif op == 2:
            crud.consultaMaterias(dirCreditos)
        elif op == 3:
# Obtener los semestres del usuario
            semestres_a_planificar = crud.obtener_semestres()
            # Pasar los semestres a la función planificar_materias
            planificacion_final, creditos_totales = crud.planificar_materias(semestres_a_planificar)
            
            # Mostrar planificación final
            print("\nPlanificación final:")
            for semestre, materias in planificacion_final.items():
                print(f"Semestre {semestre}: {materias}")

            print(f"\nTotal de créditos seleccionados: {creditos_totales}")
        elif op == 4:
            crud.calendario_academico()
        elif op == 5:
            crud.malla_interactiva()
        elif op == 6:
            crud.alertasInscripcion()
        elif op == 7:
            crud.recursosAcademicos()
        elif op == 8:
            crud.redTutoria()
        elif op == 9:
            crud.consultasProfesores()
        elif op == 10:
            crud.simuladorExamenes()
        elif op == 11:
            crud.estadisticasDesempeno()
        elif op == 12:
            crud.recomendacionCursos()
        elif op == 13:
            crud.seguimientoTareas()
        elif op == 14:
            crud.noticiasEventos()
        elif op == 15:
            crud.conexionComunidad()
        elif op == 16:
            crud.feedbackMejora()
        elif op == 17:
            promedio_general, creditos_por_anio, creditos_por_mes = crud.calcular_promedios(dirCreditos)
            print(f"Promedio de créditos por materia: {promedio_general:.2f}")
            print(f"Créditos acumulados por año: {creditos_por_anio}")
            print(f"Créditos acumulados por mes: {creditos_por_mes}")
        elif op == 18: # Opción para mostrar créditos faltantes
            crud.mostrar_creditos_faltantes(dirCreditos)
        elif op == 19:  # Opción para mostrar créditos acumulados
            total_creditos = crud.calcular_creditos_acumulados(dirCreditos)
            print(f"Total de créditos cursados: {total_creditos}")
        elif op == 20:
            rta = input("¿Desea terminar el programa? (S/N): ")
            if rta.upper() == "S":
                isMenuActivate = False
