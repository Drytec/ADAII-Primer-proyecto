# Proyecto ADA - Sistema de Asignación de Materias

## Descripción del Proyecto

Sistema de asignación óptima de materias a estudiantes, minimizando la insatisfacción general. El proyecto implementa dos algoritmos:
- **ROC-PD**: Algoritmo óptimo usando Programación Dinámica
- **ROC-V**: Algoritmo voraz (heurístico)

## Estructura del Proyecto

```
ADAII-Primer-proyecto/
├── classes.py              # Clases principales: Subject, Student, Request
├── functions.py            # Funciones de cálculo de insatisfacción
├── main.py                 # Implementación ROC-PD (Programación Dinámica)
├── ADA.py                  # Implementación ROC-V (Voraz)
├── ADA_class.py            # Clases alternativas para ROC-V
├── parser.py               # ⭐ Parser para leer archivos de prueba
├── integration_example.py  # Ejemplo completo de uso
└── test_input.txt          # Archivo de prueba generado
```

## Clases Principales

### `Subject` (Materia)
- `code`: Código de la materia
- `quota`: Número de cupos disponibles

### `Student` (Estudiante)
- `code`: Código del estudiante
- `requests`: Lista de solicitudes (Request)
- `priorityCapacity`: Capacidad total de prioridad (3 * num_solicitudes - 1)

### `Request` (Solicitud)
- `code`: Código de la materia solicitada
- `priority`: Prioridad (1-5, mayor = más importante)

## Formato de Entrada

El parser acepta archivos con el siguiente formato:

```
<número_de_materias>
<código_materia>,<cupo>
<código_materia>,<cupo>
...
<número_de_estudiantes>
<código_estudiante>,<número_solicitudes>
<código_materia>,<prioridad>
<código_materia>,<prioridad>
...
<código_estudiante>,<número_solicitudes>
<código_materia>,<prioridad>
...
```

### Ejemplo:
```
3
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
1002,1
```

## Uso del Parser

### Opción 1: Parsear desde archivo

```python
from parser import parse_test_file, print_parsed_data

subjects, students = parse_test_file('test_input.txt')
print_parsed_data(subjects, students)
```

### Opción 2: Parsear desde string

```python
from parser import parse_test_string

test_data = """3
1000,1
1001,4
1002,3
2
100,2
1000,1
1001,2
101,1
1002,1"""

subjects, students = parse_test_string(test_data)
```

### Opción 3: Ejemplo completo con algoritmo

```python
from parser import parse_test_file
from integration_example import run_roc_pd_algorithm, print_results

# Parsear datos
subjects, students = parse_test_file('test_input.txt')

# Ejecutar algoritmo
min_dissatisfaction, best_assignments = run_roc_pd_algorithm(subjects, students)

# Mostrar resultados
print_results(subjects, students, min_dissatisfaction, best_assignments)
```

## Función de Insatisfacción

La insatisfacción de un estudiante se calcula como:

```
I(e, A_e) = (1 - |A_e|/|S_e|) × (Σ prioridades no asignadas / capacidad_total)
```

Donde:
- `|A_e|`: Número de materias asignadas al estudiante
- `|S_e|`: Número de solicitudes del estudiante
- `capacidad_total`: 3 × |S_e| - 1

La insatisfacción general es el promedio de las insatisfacciones individuales.

## Algoritmos

### ROC-PD (Programación Dinámica)
- **Archivo**: `main.py` o `integration_example.py`
- **Complejidad**: Exponencial, pero con memoización
- **Ventaja**: Encuentra la solución óptima
- **Desventaja**: Puede ser lento para instancias grandes

### ROC-V (Voraz)
- **Archivo**: `ADA.py`
- **Complejidad**: O(n²)
- **Ventaja**: Rápido
- **Desventaja**: No garantiza solución óptima

## Ejecución

### Ejecutar el parser solo:
```bash
python parser.py
```

### Ejecutar ejemplo completo:
```bash
python integration_example.py
```

### Ejecutar algoritmo ROC-PD original:
```bash
python main.py
```

### Ejecutar algoritmo ROC-V:
```bash
python ADA.py
```

## Funciones del Parser

### `parse_test_file(filename)`
Lee un archivo y retorna tupla `(subjects, students)`.

### `parse_test_string(test_string)`
Parsea un string con los datos y retorna tupla `(subjects, students)`.

### `parse_test_data(lines)`
Parsea una lista de líneas y retorna tupla `(subjects, students)`.

### `print_parsed_data(subjects, students)`
Imprime los datos parseados de forma legible.

## Ejemplo de Salida

```
============================================================
RESULTADOS DE LA ASIGNACIÓN
============================================================

📊 Inconformidad mínima total: 0.8833
📊 Inconformidad promedio: 0.1767

📋 ASIGNACIONES:
------------------------------------------------------------
Estudiante 100: ['1001']
Estudiante 101: ['1002']
Estudiante 102: ['1002']
Estudiante 103: ['1001', '1002']
Estudiante 104: ['1000']

📈 ESTADÍSTICAS:
------------------------------------------------------------
Total de solicitudes: 11
Total de asignaciones: 6
Tasa de asignación: 54.55%

📚 CUPOS UTILIZADOS:
------------------------------------------------------------
Materia 1000: 1/1 cupos utilizados
Materia 1001: 2/4 cupos utilizados
Materia 1002: 3/3 cupos utilizados
```

## Autores

- Algoritmo ROC-PD: [Compañero 1]
- Algoritmo ROC-V: [Compañero 2]
- Parser: [Tu nombre]
- Funciones base: [Equipo]

## Notas

- El parser valida automáticamente el formato de entrada
- Las líneas vacías son ignoradas
- Los espacios en blanco se eliminan automáticamente
- El parser es compatible con ambos algoritmos (ROC-PD y ROC-V)
