"""
Script para ejecutar pruebas desde la línea de comandos.

Uso:
    python run_test.py <archivo_prueba>
    
Ejemplo:
    python run_test.py test_case_1.txt
"""

import sys
from parser import parse_test_file, print_parsed_data
from integration_example import run_roc_pd_algorithm, print_results


def main():
    if len(sys.argv) < 2:
        print("❌ Error: Debes proporcionar el archivo de prueba.")
        print("\nUso: python run_test.py <archivo_prueba>")
        print("Ejemplo: python run_test.py test_case_1.txt")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        print("="*60)
        print(f"CARGANDO PRUEBA: {filename}")
        print("="*60)
        
        # Parsear el archivo
        subjects, students = parse_test_file(filename)
        print_parsed_data(subjects, students)
        
        print("\n\n" + "="*60)
        print("EJECUTANDO ALGORITMO ROC-PD")
        print("="*60)
        print("⏳ Procesando... (esto puede tomar un momento)")
        
        # Ejecutar el algoritmo
        min_dissatisfaction, best_assignments = run_roc_pd_algorithm(subjects, students)
        
        # Mostrar resultados
        print_results(subjects, students, min_dissatisfaction, best_assignments)
        
        print("\n" + "="*60)
        print("✓ PROCESO COMPLETADO EXITOSAMENTE")
        print("="*60)
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo '{filename}'")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error durante la ejecución: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
