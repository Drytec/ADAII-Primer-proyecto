# Guía de Uso del Parser - Ejemplos Prácticos

## 1. Uso Básico del Parser

### Ejemplo 1: Parsear desde archivo

```python
from parser import parse_test_file, print_parsed_data

# Cargar el archivo
subjects, students = parse_test_file('test_case_1.txt')

# Mostrar los datos parseados
print_parsed_data(subjects, students)
```

### Ejemplo 2: Parsear desde string

```python
from parser import parse_test_string

# Definir los datos directamente
test_data = """2
M1,3
M2,2
2
E1,2
M1,5
M2,3
E2,1
M1,4"""

subjects, students = parse_test_string(test_data)

# Acceder a los objetos
print(f"Primera materia: {subjects[0].code}, cupos: {subjects[0].quota}")
print(f"Primer estudiante: {students[0].code}")
print(f"Primera solicitud: {students[0].requests[0].code}, prioridad: {students[0].requests[0].priority}")
```

### Ejemplo 3: Crear objetos manualmente

```python
from classes import Subject, Student, Request

# Crear materias
m1 = Subject("MAT101", 5)
m2 = Subject("FIS201", 3)

# Crear solicitudes
req1 = Request("MAT101", 5)
req2 = Request("FIS201", 3)

# Crear estudiante
student = Student("EST001", [req1, req2])

print(f"Capacidad de prioridad: {student.priorityCapacity}")  # 3*2 - 1 = 5
```

## 2. Integración con Algoritmos

### Ejemplo 4: Ejecutar ROC-PD completo

```python
from parser import parse_test_file
from integration_example import run_roc_pd_algorithm, print_results

# 1. Parsear datos
subjects, students = parse_test_file('test_case_1.txt')

# 2. Ejecutar algoritmo
min_dissatisfaction, best_assignments = run_roc_pd_algorithm(subjects, students)

# 3. Mostrar resultados
print_results(subjects, students, min_dissatisfaction, best_assignments)
```

### Ejemplo 5: Calcular insatisfacción manual

```python
from parser import parse_test_string
from functions import dissatisfaction

test_data = """1
M1,1
1
E1,2
M1,3
M1,2"""

subjects, students = parse_test_string(test_data)
student = students[0]

# Calcular insatisfacción sin asignaciones
insatisfaction_no_assign = dissatisfaction(student, [])
print(f"Insatisfacción sin asignaciones: {insatisfaction_no_assign}")

# Calcular insatisfacción con una asignación
insatisfaction_with_assign = dissatisfaction(student, [student.requests[0]])
print(f"Insatisfacción con 1 asignación: {insatisfaction_with_assign}")
```

## 3. Casos de Prueba

### Caso 1: Ejemplo del enunciado
**Archivo:** `test_case_1.txt`

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

**Características:**
- 3 materias con cupos variados
- 5 estudiantes
- Cupos limitados (especialmente materia 1000 con solo 1 cupo)

**Ejecución:**
```bash
python run_test.py test_case_1.txt
```

### Caso 2: Caso pequeño
**Archivo:** `test_case_2.txt`

```
2
M1,2
M2,1
3
E1,2
M1,3
M2,2
E2,1
M1,4
E3,2
M1,1
M2,3
```

**Características:**
- 2 materias
- 3 estudiantes
- Más rápido de ejecutar (bueno para pruebas)

**Ejecución:**
```bash
python run_test.py test_case_2.txt
```

### Caso 3: Todos consiguen todo
**Crear archivo:** `test_case_3.txt`

```
2
M1,3
M2,3
3
E1,1
M1,5
E2,1
M2,5
E3,2
M1,3
M2,3
```

**Características:**
- Cupos suficientes para todos
- Insatisfacción mínima esperada: 0

### Caso 4: Nadie consigue nada
**Crear archivo:** `test_case_4.txt`

```
2
M1,0
M2,0
2
E1,2
M1,5
M2,5
E2,2
M1,3
M2,4
```

**Características:**
- Sin cupos disponibles
- Insatisfacción máxima

## 4. Validación y Debugging

### Ejemplo 6: Verificar formato de archivo

```python
def validate_file_format(filename):
    """Valida que el archivo tenga el formato correcto."""
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Verificar número de materias
        num_subjects = int(lines[0])
        print(f"✓ Número de materias: {num_subjects}")
        
        # Verificar materias
        for i in range(1, num_subjects + 1):
            code, quota = lines[i].split(',')
            print(f"  ✓ Materia {code}: {quota} cupos")
        
        # Verificar número de estudiantes
        index = num_subjects + 1
        num_students = int(lines[index])
        print(f"✓ Número de estudiantes: {num_students}")
        
        # Verificar estudiantes
        index += 1
        for _ in range(num_students):
            student_code, num_requests = lines[index].split(',')
            print(f"  ✓ Estudiante {student_code}: {num_requests} solicitudes")
            index += int(num_requests) + 1
        
        print("\n✓ Archivo válido")
        return True
        
    except Exception as e:
        print(f"✗ Error en el archivo: {str(e)}")
        return False

# Usar la función
validate_file_format('test_case_1.txt')
```

### Ejemplo 7: Comparar resultados

```python
from parser import parse_test_file
from integration_example import run_roc_pd_algorithm

# Ejecutar con diferentes casos
cases = ['test_case_1.txt', 'test_case_2.txt']

for case in cases:
    print(f"\n{'='*60}")
    print(f"CASO: {case}")
    print('='*60)
    
    subjects, students = parse_test_file(case)
    min_dis, assignments = run_roc_pd_algorithm(subjects, students)
    
    print(f"Insatisfacción total: {min_dis:.4f}")
    print(f"Insatisfacción promedio: {min_dis/len(students):.4f}")
```

## 5. Generación de Casos de Prueba

### Ejemplo 8: Generar caso aleatorio

```python
import random

def generate_random_test(num_subjects, num_students, max_quota=5, max_requests=3):
    """Genera un caso de prueba aleatorio."""
    
    # Generar materias
    lines = [str(num_subjects)]
    subject_codes = []
    for i in range(num_subjects):
        code = f"M{i+1}"
        quota = random.randint(1, max_quota)
        lines.append(f"{code},{quota}")
        subject_codes.append(code)
    
    # Generar estudiantes
    lines.append(str(num_students))
    for i in range(num_students):
        student_code = f"E{i+1}"
        num_requests = random.randint(1, min(max_requests, num_subjects))
        lines.append(f"{student_code},{num_requests}")
        
        # Seleccionar materias aleatorias sin repetir
        selected_subjects = random.sample(subject_codes, num_requests)
        for subject in selected_subjects:
            priority = random.randint(1, 5)
            lines.append(f"{subject},{priority}")
    
    # Guardar en archivo
    filename = f"test_random_{num_subjects}m_{num_students}e.txt"
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"✓ Generado: {filename}")
    return filename

# Generar caso aleatorio
test_file = generate_random_test(num_subjects=3, num_students=4)
```

## 6. Tips y Mejores Prácticas

1. **Siempre valida el formato** antes de parsear archivos grandes
2. **Usa casos pequeños** para debugging inicial
3. **Guarda los resultados** de casos importantes para comparación
4. **Verifica los cupos** antes de ejecutar el algoritmo
5. **Documenta casos especiales** que encuentres

## 7. Comandos Rápidos

```bash
# Ejecutar caso de prueba
python run_test.py test_case_1.txt

# Solo parsear (sin ejecutar algoritmo)
python parser.py

# Ejemplo completo integrado
python integration_example.py
```

## 8. Solución de Problemas

### Problema: "FileNotFoundError"
**Solución:** Verifica que el archivo esté en el directorio correcto

### Problema: "ValueError: not enough values to unpack"
**Solución:** Verifica que cada línea tenga el formato correcto (código,valor)

### Problema: El algoritmo tarda mucho
**Solución:** Usa casos de prueba más pequeños o el algoritmo voraz (ADA.py)

### Problema: Resultados inesperados
**Solución:** Usa `print_parsed_data()` para verificar que los datos se parsearon correctamente
