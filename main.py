from itertools import combinations
from pathlib import Path

from classes import Student
from functions import dissatisfaction, generalDissatisfaction
from parser import parse_test_file
from brute_force import rocFB
from voraz import rocV
from programacion_dinamica import rocPD

RESULTS_DIR = Path("results")

def write_result_file(test_number, students, assignments, algorithm_suffix):
    """
    Escribe el archivo de resultados con el formato especificado.
    
    Args:
        test_number: Número del test
        students: Lista de estudiantes originales
        assignments: Lista de asignaciones resultado del algoritmo
        algorithm_suffix: Sufijo del algoritmo ('FB', 'V', o 'PD')
    
    Returns:
        Path: Ruta del archivo generado
    """
    RESULTS_DIR.mkdir(exist_ok=True)

    general_cost = generalDissatisfaction(students, assignments) if students else 0.0

    lines = [f"{general_cost:.4f}"]

    for student, assigned in zip(students, assignments):
        assigned_requests = list(getattr(assigned, "requests", []))
        lines.append(f"{student.code},{len(assigned_requests)}")
        for request in assigned_requests:
            lines.append(request.code)

    output_path = RESULTS_DIR / f"Result{test_number}{algorithm_suffix}.txt"
    output_path.write_text("\n".join(lines), encoding="utf-8")

    return output_path


if __name__ == "__main__":
    print("1. rocFB \n2. rocV \n3. rocPD")
    option = int(input("\nDígite una opción: "))

    if option == 1:
        test = int(
            input(
                "\nDigite el número del test a ejecutar (acorde a la batería de pruebas): "
            )
        )

        subjects, students = parse_test_file(f"tests/Prueba{test}.txt")
        cost, assignments = rocFB(subjects, students)
        write_result_file(test, students, assignments, "FB")
    elif option == 2:
        test = int(
            input(
                "\nDigite el número del test a ejecutar (acorde a la batería de pruebas): "
            )
        )

        subjects, students = parse_test_file(f"tests/Prueba{test}.txt")
        cost, assignments = rocV(subjects, students)
        write_result_file(test, students, assignments, "V")
    elif option == 3:
        test = int(
            input(
                "\nDigite el número del test a ejecutar (acorde a la batería de pruebas): "
            )
        )

        subjects, students = parse_test_file(f"tests/Prueba{test}.txt")
        cost, assignments = rocPD(subjects, students)
        write_result_file(test, students, assignments, "PD")
