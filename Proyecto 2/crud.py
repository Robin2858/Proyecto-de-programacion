import json
import core
from datetime import datetime, timedelta


# Definición del pensum
pensum = {
    1: [("Álgebra Lineal", 3), ("Biología Estructural", 2), ("Cálculo Diferencial", 4), ("Expresión", 4),
        ("Fundamentos de Programación", 3), ("Laboratorio Biología Estructural", 0), ("Seminario de Ingeniería I", 2)],
    2: [("Biología Celular y Molecular", 2), ("Cálculo Integral", 4), ("Dibujo de Ingeniería", 2), ("Identidad", 3),
        ("Laboratorio Biología Celular y Molecular", 0), ("Laboratorio de Mecánica", 0), ("Mecánica y Laboratorio", 3),
        ("Programación de Computadores", 3)],
    3: [("Bioquímica", 2), ("Cálculo en Varias Variables", 3), ("Creatividad", 3), ("Dibujo Asistido por Computador", 2),
        ("Electromagnetismo y Laboratorio", 3), ("Estadística General", 3), ("Laboratorio Bioquímica", 0),
        ("Laboratorio de Electromagnetismo", 0), ("Seminario de Ingeniería II", 2)],
    4: [("Circuitos Eléctricos", 3), ("Ecuaciones Diferenciales", 3), ("Electiva Sociohumanística", 3),
        ("Laboratorio Circuitos Eléctricos", 0), ("Laboratorio Morfofisiología Biomédica I", 0),
        ("Laboratorio Termofluidos", 0), ("Morfofisiología Biomédica I", 3),
        ("Taller de Deportes, Recreación y Cultura", 1), ("Taller de Desarrollo Humano", 1), ("Termofluidos", 3)],
    5:[("Actividades Libres de Recreación, Deporte y Cultura y de Desarrollo Humano", 2), ("Biomateriales", 3),
        ("Electiva Sociohumanística", 3), ("Electrónica Análoga", 3), ("Inteligencia Artificial y Ciencia de Datos", 2),
        ("Laboratorio Biomateriales", 0), ("Laboratorio de Electrónica Análoga", 0),
        ("Laboratorio Morfofisiología Biomédica II", 0), ("Laboratorio Sistemas Embebidos", 0),
        ("Morfofisiología Biomédica II", 3), ("Sistemas Embebidos", 2)],
    6: [("Biomecánica Deportiva", 2), ("Electiva de Contexto", 3), ("Electrónica de Potencia", 2),
        ("Equipos Médicos Básicos", 2), ("Imágenes Biomédicas", 2), ("Ingeniería Clínica", 3),
        ("Laboratorio Biomecánica Deportiva", 0), ("Laboratorio Electrónica de Potencia", 0),
        ("Laboratorio Equipos Médicos Básicos", 0), ("Laboratorio Ingeniería Clínica", 0),
        ("Procesamiento de Señales Biomédicas", 2), ("Tissue Engineering", 2),
        ("Tissue Engineering Laboratory", 0)],
    7: [("Biomecánica Clínica", 2), ("Electiva Profundización", 3), ("Equipos de Monitoreo y Diagnóstico Médico", 2),
        ("Ingeniería Hospitalaria", 3), ("Instrumentación Biomédica", 3), ("Laboratorio Biomecánica Clínica", 0),
        ("Laboratorio Equipos de Monitoreo y Diagnóstico Médico", 0), ("Laboratorio Ingeniería Hospitalaria", 0),
        ("Laboratorio Instrumentación Biomédica", 0), ("Tele-Robótica Médica", 3)],
    8: [("Diseño en Medicina Personalizada", 3), ("Electiva de Contexto", 3), ("Electiva Profundización", 9),
        ("Equipos Médicos Avanzados", 2), ("Laboratorio Equipos Médicos Avanzados", 0)],
    9: [("Práctica Académica", 12), ("Proyecto de Diseño en Medicina Personalizada", 2)],
}


def agregarMateria(dirCreditos):
    nombre = input("\nIngrese el nombre de la materia: ")
    while True:
        try:
            creditos = int(input("Ingrese los créditos: "))
            break
        except ValueError:
            print("Por favor, ingrese un número válido para los créditos.")
    
    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    
    # Crear la materia con estado como completada
    materia = {
        "nombre": nombre,
        "creditos": creditos,
        "pendiente": False,  # Cambiar a False para indicar que está completada
        "fecha": fecha_actual  # Agregar la fecha aquí
    }
    
    dirCreditos['data'].append(materia)
    
    # Guardar cambios en el archivo
    core.crearInfo('creditos.json', dirCreditos)
    print("\nMateria agregada con éxito.")

def consultaMaterias(dirCreditos):
   if not dirCreditos['data']:
       print("\nNo hay datos disponibles.")
       return
    # Mostrar materias completadas
    

   # Mostrar materias pendientes
   print("\nMaterias y Créditos Pendientes:")
   for materia in dirCreditos['data']:
       estado = 'Pendiente' if materia['pendiente'] else 'Completado'
       print(f"Materia: {materia['nombre']}, Créditos: {materia['creditos']}, Estado: {estado}")
       print("----------------------------------------")


def planificar_materias(semestres_seleccionados):
    planificacion = {}
    total_creditos = 0
    
    for semestre in semestres_seleccionados:
        if semestre in pensum:
            print(f"\nMaterias disponibles para el semestre {semestre}:")
            for materia, creditos in pensum[semestre]:
                print(f"- {materia} ({creditos} créditos)")

                # Validar si la materia ya fue seleccionada
                if materia in planificacion[semestre]:
                    print(f"La materia {materia} ya ha sido seleccionada.")
                    continue
                
                # Validar si se cumplen los créditos
                if total_creditos + creditos > 24:
                    print(f"No se puede seleccionar la materia {materia} porque el total de créditos excede los 24.")
                    continue
                
                # Marcar la materia como seleccionada
                planificacion[semestre].append(materia)
                total_creditos += creditos
                print(f"La materia {materia} ha sido seleccionada.")
                break
                
            seleccionadas = input("Ingrese las materias que desea cursar (separadas por comas): ")
            materias_elegidas = [materia.strip() for materia in seleccionadas.split(",")]
            
            # Validar selección
            materias_validas = []
            for materia in materias_elegidas:
                for mat, creditos in pensum[semestre]:
                    if mat.lower() == materia.lower():
                        materias_validas.append((mat, creditos))
                        total_creditos += creditos
            
            planificacion[semestre] = materias_validas
        else:
            print(f"El semestre {semestre} no es válido.")
    
    return planificacion, total_creditos

def obtener_semestres():
    semestres_input = input("Ingrese los semestres que desea planificar (separados por comas): ")
    semestres_seleccionados = [int(semestre.strip()) for semestre in semestres_input.split(",")]
    return semestres_seleccionados

def calendario_academico():
    # Definir las fechas de inicio y fin del semestre
    semestre_inicio_febrero = datetime(year=datetime.now().year, month=2, day=1)
    semestre_fin_junio = datetime(year=datetime.now().year, month=6, day=30)

    semestre_inicio_agosto = datetime(year=datetime.now().year, month=8, day=1)
    semestre_fin_noviembre = datetime(year=datetime.now().year, month=11, day=30)

    # Solicitar al usuario que ingrese la fecha actual
    fecha_actual_input = input("Ingrese la fecha actual (formato: YYYY-MM-DD): ")
    try:
        fecha_actual = datetime.strptime(fecha_actual_input, "%Y-%m-%d")
    except ValueError:
        print("Fecha no válida. Asegúrese de usar el formato YYYY-MM-DD.")
        return

    # Determinar en qué semestre se encuentra
    if semestre_inicio_febrero <= fecha_actual <= semestre_fin_junio:
        semestre = "Febrero - Junio"
        fin_semestre = semestre_fin_junio
        parciales = [
            semestre_inicio_febrero + timedelta(weeks=4),
            semestre_inicio_febrero + timedelta(weeks=8),
            semestre_inicio_febrero + timedelta(weeks=12),
            semestre_inicio_febrero + timedelta(weeks=16)
        ]
    elif semestre_inicio_agosto <= fecha_actual <= semestre_fin_noviembre:
        semestre = "Agosto - Noviembre"
        fin_semestre = semestre_fin_noviembre
        parciales = [
            semestre_inicio_agosto + timedelta(weeks=4),
            semestre_inicio_agosto + timedelta(weeks=8),
            semestre_inicio_agosto + timedelta(weeks=12),
            semestre_inicio_agosto + timedelta(weeks=16)
        ]
    else:
        print("La fecha ingresada no corresponde a ningún semestre académico.")
        return

    # Mostrar resultados
    print(f"\nSemestre actual: {semestre}")
    print(f"Fin del semestre: {fin_semestre.strftime('%Y-%m-%d')}")
    print("Fechas de parciales:")
    for i, parcial in enumerate(parciales):
        print(f"Parcial {i + 1}: {parcial.strftime('%Y-%m-%d')}")

def mostrar_malla():
    print("\nMalla Curricular:")
    for semestre, materias in pensum.items():
        print(f"Semestre {semestre}:")
        for materia, creditos in materias:
            print(f"  - {materia} - Créditos: {creditos}")
           
# Función para marcar una materia como aprobada
def marcar_aprobada(materia):
    for semestre, materias in pensum.items():
        for mat, creditos in materias:
            if mat.lower() == materia.lower():
                print(f"{materia} ha sido marcada como aprobada.")
                # Opcional: eliminarla de la malla si se desea
                materias.remove((mat, creditos))
                return
    print(f"La materia {materia} no existe en la malla.")

# Función principal para interactuar con el usuario
def malla_interactiva():
    while True:
        mostrar_malla()
        opcion = input("\n¿Desea marcar una materia como aprobada? (S/N): ").strip().upper()
        if opcion == 'S':
            materia_a_aprobar = input("Ingrese el nombre de la materia a aprobar: ")
            marcar_aprobada(materia_a_aprobar)
        elif opcion == 'N':
            print("Saliendo del sistema de malla curricular.")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

def alertasInscripcion():
    alertas = [
        "Inscripción abierta hasta el *20/02/2024*.",
        "Último día para agregar materias: *10/03/2024*."
    ]
    
    while True:
        print("\n=== Alertas para Inscripción ===")
        for alerta in alertas:
            print(alerta)
        
        opcion = input("\n¿Desea recibir más información sobre las inscripciones? (S/N): ").strip().upper()
        if opcion == 'S':
            print("Más información sobre el proceso de inscripción...")
            print("Consulte la página de inscripción o contacte al administrador.")

            print("Recuerde revisar los requisitos y fechas importantes.")
        elif opcion == 'N':
            print("Saliendo del sistema de alertas de inscripción.")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")


def recursosAcademicos():
    recursos = [
        "Libro 'Biomedicina Básica'",
        "Artículos en línea sobre Biología Molecular",
        "Guías de Estudio de Anatomía",
        "Videos Educativos sobre Fisiología"
    ]
    
    while True:
        print("\n=== Recursos Académicos ===")
        for i, recurso in enumerate(recursos, start=1):
            print(f"{i}. {recurso}")
        
        opcion = input("\n¿Desea ver más información sobre algún recurso? (Ingrese el número o N para salir): ").strip().upper()
        
        if opcion == 'N':
            print("Saliendo del sistema de recursos académicos.")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(recursos):
            recurso_seleccionado = recursos[int(opcion) - 1]
            print(f"\nInformación sobre el recurso seleccionado: {recurso_seleccionado}")
        
            print("Puedes encontrar más información en la biblioteca o en línea.")
        else:
            print("Opción no válida. Por favor intente nuevamente.")


def redTutoria():
    tutores = [
        "Dr. Juan Pérez - Biología",
        "Prof. Ana Gómez - Química",
        "Mrs. Laura Martínez - Matemáticas",
        "Dr. Carlos López - Fisiología",
        "GOAT Julian Santoyo - Programación"	
    ]
    
    while True:
        print("\n=== Red de Tutorías Académicas ===")
        for i, tutor in enumerate(tutores, start=1):
            print(f"{i}. {tutor}")
        
        opcion = input("\n¿Desea obtener más información sobre algún tutor? (Ingrese el número o N para salir): ").strip().upper()
        
        if opcion == 'N':
            print("Saliendo del sistema de red de tutorías académicas.")
            break
        elif opcion.isdigit() and 1 <= int(opcion) <= len(tutores):
            tutor_seleccionado = tutores[int(opcion) - 1]
            print(f"\nInformación sobre el tutor seleccionado: {tutor_seleccionado}")
           
            print("Puedes contactarlo a través del correo institucional proyectop@unab.edu.co para más detalles.")
        else:
            print("Opción no válida. Por favor intente nuevamente.")


def consultasProfesores():
    # Lista para almacenar las consultas enviadas
    consultas_enviadas = []
    
    print("\n=== Consultas a Profesores ===")

    
    while True:
        consulta = input("\nIngrese su consulta para el profesor (o escriba 'salir' para terminar): ")
        
        if consulta.strip().lower() == 'salir':
            print("Saliendo del sistema de consultas a profesores.")
            break
        
        # Agregar la consulta a la lista de consultas enviadas
        consultas_enviadas.append(consulta)
        
        print(f"Consulta enviada: {consulta}")
        
        # Simulación de respuesta del profesor
        respuesta_profesor = input(f"\nProfesor: ¿Cuál es la respuesta a su consulta? ")
        
        print(f"Respuesta del profesor: {respuesta_profesor}")
        
        # Simulación de confirmación de respuesta
        print("Su consulta ha sido respondida exitosamente.")
        # Simulación de confirmación de envío
        print("Su consulta ha sido enviada exitosamente. Espere la respuesta del profesor.")
    
    # Opcional: Mostrar todas las consultas enviadas al final
    print("\nConsultas enviadas:")
    for c in consultas_enviadas:
        print(f"- {c}")



def simuladorExamenes():
     # Lógica para simular exámenes (placeholder)
    
    # Lista de preguntas y respuestas
    preguntas = [
        {"pregunta": "¿Cuál es la función del ADN?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 0},
        {"pregunta": "¿Cuál es la función del DNA?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 0},
        {"pregunta": "¿Qué es el RNA?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 1},
        {"pregunta": "¿Qué es la proteína?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 0},
        {"pregunta": "¿Qué es la molécula?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 0},
        {"pregunta": "¿Qué es el ácido nucleico?", "respuestas": ["Almacenar información genética", "Producir energía"], "respuesta_correcta": 0},
        {"pregunta": "¿Qué es la mitosis?", "respuestas": ["División celular", "Fusión celular"], "respuesta_correcta": 0}
        ]
    
    print("\n=== Simulador de Exámenes ===")
    puntaje = 0
    
    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        
        for j, respuesta in enumerate(pregunta["respuestas"]):
            print(f"{j + 1}. {respuesta}")
        
        # Solicitar respuesta del usuario
        while True:
            try:
                respuesta_usuario = int(input("Seleccione el número de su respuesta: ")) - 1
                if respuesta_usuario < 0 or respuesta_usuario >= len(pregunta["respuestas"]):
                    raise ValueError("Número fuera de rango.")
                break
            except ValueError as e:
                print("Entrada no válida. Por favor ingrese un número correspondiente a su respuesta.")
        
        # Evaluar la respuesta
        if respuesta_usuario == pregunta["respuesta_correcta"]:
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Incorrecto.")
    
    # Mostrar el resultado final
    print(f"\nSu puntaje final es: {puntaje}/{len(preguntas)}")



def estadisticasDesempeno():
      # Lógica para mostrar estadísticas académicas 
    
    # Estadísticas de desempeño académico
    estadisticas = {
        'promedio': 85,
        'materias_aprobadas': 5,
        'materias_reprobadas': 1,
        
    }
    
    print("\n=== Estadísticas de Desempeño Académico ===")
    for key, value in estadisticas.items():
        print(f"{key}: {value}")
    
   
    
    # 1. Calcular estadísticas más detalladas
    def calcular_promedio_por_materia(materias):
        # Ejemplo de cálculo de promedio por materia
        if len(materias) == 0:
            return 0
        return sum(materias) / len(materias)
# Sistema recomendacion de cursos electivos
def recomendacionCursos():
    # Lógica para recomendar cursos electivos (placeholder)
    # Este ejemplo muestra cómo se podría agregar la lógica para recomendar cursos
    print("\nRecomendación de Cursos Electivos:")
    print("Los cursos electivos recomendados para ti son:")
    print("1. Biología Computacional")
    print("2. Bioinformática")
    print("3. Genética")


def seguimientoTareas():
   # Lógica para seguimiento del avance en tareas (placeholder)
   tareas = [
       {"tarea":"Proyecto final de Biología","estado":"En progreso"},
       {"tarea":"Informe sobre genética","estado":"Completado"}
   ]
   
   print("\nSeguimiento del Avance en Tareas:")
   for tarea in tareas:
       print(f"Tarea: {tarea['tarea']}, Estado: {tarea['estado']}")

def noticiasEventos():
   # Lógica para acceder a noticias relevantes (placeholder)
   noticias = [
       {"titulo":"Conferencia sobre Biomedicina","fecha":"15/04/2025"},
       {"titulo":"Taller sobre Investigación Biomédica","fecha":"25/05/2025"}
       ]
   
   print("\nNoticias y Eventos Relevantes:")
   for noticia in noticias:
       print(f"{noticia['titulo']} - Fecha: {noticia['fecha']}")

def conexionComunidad():
   # Lógica para conectar con comunidades estudiantiles (placeholder)
   comunidades = ["Grupo de Estudiantes en Facebook","Foro sobre Investigación Biomédica"]

   
   print("\nComunidades Estudiantiles:")
   for comunidad in comunidades:
       print(comunidad)
       print("\nConectarse a la comunidad:", comunidad)
       print("Nuestras redes sociales:")
       print("Facebook: https://www.facebook.com/grupodeestudiantesenbiomedicaunab")
       print("Instagram: https://www.instagram.com/biomedicaunab/")



def feedbackMejora():
   # Lógica para recoger feedback sobre el proceso educativo 
   feedback = input("\nIngrese su feedback sobre el proceso educativo: ")
   print(f"Feedback recibido: {feedback}")
   
   # Lógica para procesar y guardar el feedback 
   print("\nGracias por su feedback. Nos ayudamos a mejorar.")
   

def calcular_promedios(dirCreditos):
    total_creditos = sum(materia['creditos'] for materia in dirCreditos['data'])
    total_materias = len(dirCreditos['data'])
    
    if total_materias == 0:
        return 0, {}, {}  # Evitar división por cero
    
    promedio_general = total_creditos / total_materias
    
    # Calcular créditos por año y mes
    creditos_por_anio = {}
    creditos_por_mes = {}
    
    for materia in dirCreditos['data']:
        fecha = datetime.strptime(materia['fecha'], "%Y-%m-%d")
        anio = fecha.year
        mes = fecha.month
        
        if anio not in creditos_por_anio:
            creditos_por_anio[anio] = 0
        creditos_por_anio[anio] += materia['creditos']
        
        if mes not in creditos_por_mes:
            creditos_por_mes[mes] = 0
        creditos_por_mes[mes] += materia['creditos']
    
    return promedio_general, creditos_por_anio, creditos_por_mes

def mostrar_creditos_faltantes(dirCreditos):
    CREDITOS_REQUERIDOS_GRADUACION = 153  # Cambia este valor según sea necesario
    total_creditos_acumulados = sum(materia['creditos'] for materia in dirCreditos['data'])
    creditos_faltantes = CREDITOS_REQUERIDOS_GRADUACION - total_creditos_acumulados
    
    if creditos_faltantes > 0:
        print(f"Créditos faltantes para graduación: {creditos_faltantes}")
    else:
        print("¡Felicidades! Has cumplido con los créditos requeridos para graduación.")

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

def calcular_creditos_acumulados(dirCreditos):
    total_creditos = sum(materia['creditos'] for materia in dirCreditos['data'] if not materia.get('pendiente', True))
    return total_creditos
