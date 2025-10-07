"""
Ejemplo de integración: Cómo usar el parser con los algoritmos existentes.
"""

from parser import parse_test_string, parse_test_file, print_parsed_data
from functions import dissatisfaction, generalDissatisfaction
from classes import Student
from itertools import combinations


def run_roc_pd_algorithm(subjects, students):
    """
    Ejecuta el algoritmo ROC con Programación Dinámica.
    
    Args:
        subjects: Lista de materias
        students: Lista de estudiantes
        
    Returns:
        tuple: (inconformidad_minima, mejor_asignacion)
    """
    
    store = {}
    
    def rocPD(j, quotas):
        key = (j, quotas)

        if key in store:
            return store[key]

        if j == len(students):
            return (0, [])

        student = students[j]
        best = float("inf")
        bestAssignation = []

        # Caso 1: No asignar ninguna materia al estudiante
        noAssignDissatisfaction = dissatisfaction(student, [])
        dissatisfactionRest, assignationRest = rocPD(j + 1, quotas)
        best = noAssignDissatisfaction + dissatisfactionRest
        bestAssignation = [Student(student.code, [])] + assignationRest

        requests = student.requests

        # Probar todas las combinaciones posibles de asignaciones
        for l in range(1, len(requests) + 1):
            for combination in combinations(requests, l):
                newQuotas = list(quotas)
                valid = True

                # Verificar si hay cupo disponible para esta combinación
                for request in combination:
                    i = next(
                        (i for i, subject in enumerate(subjects) if subject.code == request.code)
                    )

                    if newQuotas[i] <= 0:
                        valid = False
                        break

                    newQuotas[i] -= 1

                if not valid:
                    continue

                # Calcular insatisfacción de esta combinación
                combinationDissatisfaction = dissatisfaction(student, combination)
                dissatisfactionNext, assignationNext = rocPD(j + 1, tuple(newQuotas))
                totalDissatisfaction = combinationDissatisfaction + dissatisfactionNext

                if totalDissatisfaction < best:
                    best = totalDissatisfaction
                    bestAssignation = [Student(student.code, combination)] + assignationNext

        store[key] = (best, bestAssignation)
        return store[key]
    
    # Ejecutar el algoritmo
    initial_cupos = tuple(m.quota for m in subjects)
    min_dissatisfaction, best_assignments = rocPD(0, initial_cupos)
    
    return min_dissatisfaction, best_assignments


def print_results(subjects, students, min_dissatisfaction, best_assignments):
    """
    Imprime los resultados de la asignación.
    """
    print("\n" + "="*60)
    print("RESULTADOS DE LA ASIGNACIÓN")
    print("="*60)
    
    print(f"\n📊 Inconformidad mínima total: {min_dissatisfaction:.4f}")
    print(f"📊 Inconformidad promedio: {min_dissatisfaction/len(students):.4f}")
    
    print("\n📋 ASIGNACIONES:")
    print("-" * 60)
    for student_orig, assigned in zip(students, best_assignments):
        codes = [req.code for req in assigned.requests]
        if codes:
            print(f"Estudiante {student_orig.code}: {codes}")
        else:
            print(f"Estudiante {student_orig.code}: [Sin asignaciones]")
    
    print("\n📈 ESTADÍSTICAS:")
    print("-" * 60)
    total_requests = sum(len(s.requests) for s in students)
    total_assigned = sum(len(a.requests) for a in best_assignments)
    print(f"Total de solicitudes: {total_requests}")
    print(f"Total de asignaciones: {total_assigned}")
    print(f"Tasa de asignación: {(total_assigned/total_requests*100):.2f}%")
    
    print("\n📚 CUPOS UTILIZADOS:")
    print("-" * 60)
    for subject in subjects:
        assigned_count = sum(
            1 for assignment in best_assignments 
            for request in assignment.requests 
            if request.code == subject.code
        )
        print(f"Materia {subject.code}: {assigned_count}/{subject.quota} cupos utilizados")


# ============================================================================
# EJEMPLO DE USO
# ============================================================================

if __name__ == "__main__":
    # Datos de prueba
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
    
    print("="*60)
    print("PARSEANDO DATOS DE ENTRADA")
    print("="*60)
    
    # Parsear los datos
    subjects, students = parse_test_string(test_data)
    print_parsed_data(subjects, students)
    
    print("\n\n" + "="*60)
    print("EJECUTANDO ALGORITMO ROC-PD")
    print("="*60)
    print("(Esto puede tomar un momento para instancias grandes...)")
    
    # Ejecutar el algoritmo
    min_dissatisfaction, best_assignments = run_roc_pd_algorithm(subjects, students)
    
    # Mostrar resultados
    print_results(subjects, students, min_dissatisfaction, best_assignments)
    
    print("\n" + "="*60)
    print("✓ PROCESO COMPLETADO")
    print("="*60)
