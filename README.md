# Proyecto I - Asignación Óptima de Cursos (ROC)

## Descripción del Proyecto

Sistema de asignación óptima de materias a estudiantes, minimizando la insatisfacción general. El proyecto implementa tres algoritmos de solución:
- **rocFB**: Fuerza Bruta - Solución óptima exhaustiva
- **rocV**: Voraz (Greedy) - Solución heurística rápida
- **rocPD**: Programación Dinámica - Solución óptima con memoización

## Estructura del Proyecto

```
ADAII-Primer-proyecto/
├── main.py                    # ⭐ Menú principal y orquestador
├── brute_force.py             # Algoritmo rocFB (Fuerza Bruta)
├── voraz.py                   # Algoritmo rocV (Voraz)
├── programacion_dinamica.py   # Algoritmo rocPD (Programación Dinámica)
├── parser.py                  # Parser para leer archivos de prueba
├── classes.py                 # Clases: Subject, Student, Request
├── functions.py               # Funciones de cálculo de insatisfacción
├── tests/                     # Batería de pruebas (Prueba1.txt - Prueba46.txt)
└── results/                   # Archivos de salida generados
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

## 🚀 Ejecución del Programa

### Comando Principal
```bash
python main.py
```

### Menú Interactivo
```
1. rocFB 
2. rocV 
3. rocPD

Dígite una opción: [1, 2 o 3]
Digite el número del test a ejecutar: [1-46]
```

### Ejemplos de Uso
```bash
# Ejecutar Fuerza Bruta con Prueba 1
python main.py
> 1
> 1

# Ejecutar Voraz con Prueba 5
python main.py
> 2
> 5

# Ejecutar Programación Dinámica con Prueba 10
python main.py
> 3
> 10
```

## 📄 Formato de Archivos

### Formato de Entrada (tests/PruebaX.txt)

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
```

#### Ejemplo (Prueba1.txt):
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

### Formato de Salida (results/ResultXYZ.txt)

Los archivos de salida siguen el formato especificado en la sección 3.4.2 del documento del proyecto:

```
<costo_insatisfacción_general>
<código_estudiante>,<cantidad_materias_asignadas>
<código_materia_1>
<código_materia_2>
...
<código_estudiante>,<cantidad_materias_asignadas>
<código_materia_1>
...
```

**Nomenclatura de archivos:**
- `ResultXFB.txt` - Resultado de Fuerza Bruta para test X
- `ResultXV.txt` - Resultado de Voraz para test X
- `ResultXPD.txt` - Resultado de Programación Dinámica para test X

#### Ejemplo (Result1PD.txt):
```
0.2500
100,2
1001
1002
101,1
1002
102,0
103,2
1001
1000
104,1
1000
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

## 🧮 Algoritmos Implementados

### 1. rocFB - Fuerza Bruta
- **Archivo**: `brute_force.py`
- **Método**: Genera todas las combinaciones posibles de asignaciones
- **Complejidad**: Exponencial O(2^n)
- **Ventaja**: Garantiza encontrar la solución óptima
- **Desventaja**: Muy lento para instancias grandes
- **Uso**: Ideal para verificar correctitud en tests pequeños

### 2. rocV - Voraz (Greedy)
- **Archivo**: `voraz.py`
- **Método**: Asignación por ponderación de prioridades
- **Complejidad**: O(k × r) donde k=materias, r=estudiantes
- **Ventaja**: Muy rápido, escalable
- **Desventaja**: No garantiza solución óptima
- **Uso**: Ideal para instancias grandes donde se necesita rapidez

### 3. rocPD - Programación Dinámica
- **Archivo**: `programacion_dinamica.py`
- **Método**: Recursión con memoización
- **Complejidad**: Exponencial, pero optimizado con cache
- **Ventaja**: Solución óptima más rápida que Fuerza Bruta
- **Desventaja**: Alto uso de memoria para instancias grandes
- **Uso**: Balance entre optimalidad y rendimiento

## 📊 Función de Insatisfacción

La insatisfacción de un estudiante se calcula como:

```
I(e, A_e) = (1 - |A_e|/|S_e|) × (1 - Σ(prioridades_asignadas) / capacidad_total)
```

Donde:
- `|A_e|`: Número de materias asignadas al estudiante
- `|S_e|`: Número de solicitudes del estudiante
- `capacidad_total`: Suma de todas las prioridades del estudiante

**Insatisfacción General**: Promedio de las insatisfacciones individuales de todos los estudiantes.

## 🔧 Uso Programático

### Importar y usar el parser
```python
from parser import parse_test_file

subjects, students = parse_test_file("tests/Prueba1.txt")
```

### Ejecutar un algoritmo específico
```python
from brute_force import rocFB
from voraz import rocV
from programacion_dinamica import rocPD
from parser import parse_test_file
from main import write_result_file

# Parsear test
subjects, students = parse_test_file("tests/Prueba1.txt")

# Ejecutar algoritmo deseado
cost, assignments = rocPD(subjects, students)

# Guardar resultado
write_result_file(1, students, assignments, "PD")
```

## 📝 Notas Técnicas

- Los archivos de test están en la carpeta `tests/` (Prueba1.txt a Prueba46.txt)
- Los resultados se guardan automáticamente en la carpeta `results/`
- El parser valida automáticamente el formato de entrada
- Las líneas vacías y espacios en blanco son ignorados
- Todos los algoritmos reciben parámetros en el mismo orden: `(subjects, students)`

## 👥 Equipo

- Parser e integración: Jose Armando Martínez Hernández - 2325365
- Algoritmo rocFB: Nicolás Salazar Castillo 2328060-3743
- Algoritmo rocV: Dylan Fernando Morales Rojas
- Algoritmo rocPD: Jhorman Gomez 2326867-3743
