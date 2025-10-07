"""
Parser para leer archivos de prueba y crear objetos del sistema de asignación de materias.

Formato esperado del archivo:
- Primera línea: número de materias (n)
- Siguientes n líneas: código_materia,cupo
- Siguiente línea: número de estudiantes (m)
- Para cada estudiante:
    - código_estudiante,cantidad_solicitudes
    - Siguientes cantidad_solicitudes líneas: código_materia,prioridad
"""

from classes import Subject, Student, Request


def parse_test_file(filename):
    """
    Lee un archivo de prueba y crea los objetos necesarios (materias y estudiantes).
    
    Args:
        filename (str): Ruta al archivo de prueba
        
    Returns:
        tuple: (list[Subject], list[Student]) - Lista de materias y lista de estudiantes
    """
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]
    
    return parse_test_data(lines)


def parse_test_data(lines):
    """
    Parsea los datos de prueba desde una lista de líneas.
    
    Args:
        lines (list[str]): Lista de líneas del archivo de prueba
        
    Returns:
        tuple: (list[Subject], list[Student]) - Lista de materias y lista de estudiantes
    """
    index = 0
    
    # Leer número de materias
    num_subjects = int(lines[index])
    index += 1
    
    # Leer materias
    subjects = []
    for _ in range(num_subjects):
        code, quota = lines[index].split(',')
        subjects.append(Subject(code.strip(), int(quota.strip())))
        index += 1
    
    # Leer número de estudiantes
    num_students = int(lines[index])
    index += 1
    
    # Leer estudiantes
    students = []
    for _ in range(num_students):
        # Leer código del estudiante y número de solicitudes
        student_code, num_requests = lines[index].split(',')
        student_code = student_code.strip()
        num_requests = int(num_requests.strip())
        index += 1
        
        # Leer solicitudes del estudiante
        requests = []
        for _ in range(num_requests):
            subject_code, priority = lines[index].split(',')
            requests.append(Request(subject_code.strip(), int(priority.strip())))
            index += 1
        
        students.append(Student(student_code, requests))
    
    return subjects, students


def parse_test_string(test_string):
    """
    Parsea los datos de prueba desde un string.
    
    Args:
        test_string (str): String con los datos de prueba
        
    Returns:
        tuple: (list[Subject], list[Student]) - Lista de materias y lista de estudiantes
    """
    lines = [line.strip() for line in test_string.strip().split('\n') if line.strip()]
    return parse_test_data(lines)


def print_parsed_data(subjects, students):
    """
    Imprime los datos parseados de forma legible.
    
    Args:
        subjects (list[Subject]): Lista de materias
        students (list[Student]): Lista de estudiantes
    """
    print("\n=== MATERIAS ===")
    for subject in subjects:
        print(f"Materia {subject.code}: {subject.quota} cupos")
    
    print("\n=== ESTUDIANTES ===")
    for student in students:
        print(f"\nEstudiante {student.code} (Capacidad de prioridad: {student.priorityCapacity}):")
        for request in student.requests:
            print(f"  - Materia {request.code}: prioridad {request.priority}")


# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo con string
    test_data = """3
1000,1
1001,4
1002,3
5
100,3
1002,2
1000,3
1001,2
101,1
1002,1
102,2
1002,1
1000,2
103,3
1001,2
1002,2
1000,4
104,2
1000,4
1002,1"""
    
    print("Parseando datos de prueba...\n")
    subjects, students = parse_test_string(test_data)
    print_parsed_data(subjects, students)
    
    # Ejemplo guardando en archivo y leyendo
    print("\n\n=== Guardando en archivo de prueba ===")
    with open('test_input.txt', 'w') as f:
        f.write(test_data)
    
    print("Leyendo desde archivo...")
    subjects_from_file, students_from_file = parse_test_file('test_input.txt')
    print("\nVerificando que los datos son iguales...")
    assert len(subjects) == len(subjects_from_file)
    assert len(students) == len(students_from_file)
    print("✓ Los datos se leyeron correctamente del archivo")
