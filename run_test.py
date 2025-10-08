"""Utilidad ligera para ejecutar el algoritmo ROC-PD desde la línea de comandos."""

import sys

from parser import parse_test_file
from main import solve_roc_pd, write_result_file


def run_test_case(input_path: str, test_number: int):
    """Ejecuta el algoritmo sobre un archivo de prueba y genera la salida."""

    subjects, students = parse_test_file(input_path)
    cost, assignments = solve_roc_pd(subjects, students)
    return write_result_file(test_number, students, assignments, cost)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("Uso: python run_test.py <ruta_archivo_prueba> <numero_test>")

    output_path = run_test_case(sys.argv[1], int(sys.argv[2]))
    print(output_path)
