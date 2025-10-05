from classes import Subject, Student, Request
from functions import dissatisfaction, generalDissatisfaction


# Materias
s1 = Subject("m1", 3)
s2 = Subject("m2", 4)
s3 = Subject("m3", 2)
M = [s1, s2, s3]

# Estudiantes
# Estudiante 1
r1 = Request("m1", 5)
r2 = Request("m2", 2)
r3 = Request("m3", 1)
st1 = Student("e1", [r1, r2, r3])

# Estudiante 2
r4 = Request("m1", 4)
r5 = Request("m2", 1)
r6 = Request("m3", 3)
st2 = Student("e2", [r4, r5, r6])

# Estudiante 3
r7 = Request("m2", 3)
r8 = Request("m3", 2)
st3 = Student("e3", [r7, r8])

# Estudiante 4
r9 = Request("m1", 2)
r10 = Request("m3", 3)
st4 = Student("e4", [r9, r10])

# Estudiante 5
r11 = Request("m1", 3)
r12 = Request("m2", 2)
r13 = Request("m3", 3)
st5 = Student("e5", [r11, r12, r13])

# Lista de estudiantes
E = [st1, st2, st3, st4, st5]


# Estudiante 1
a1 = Request("m1", 5)
a2 = Request("m2", 2)
sta1 = Student("e1", [a1, a2])

# Estudiante 2
a3 = Request("m1", 4)
a4 = Request("m2", 1)
a5 = Request("m3", 3)
sta2 = Student("e2", [a3, a4, a5])

# Estudiante 3
a6 = Request("m2", 3)
sta3 = Student("e3", [a6])

# Estudiante 4
a7 = Request("m3", 3)
sta4 = Student("e4", [a7])

# Estudiante 5
a8 = Request("m1", 3)
a9 = Request("m2", 2)
sta5 = Student("e5", [a8, a9])

# Lista de asignaciones
A = [sta1, sta2, sta3, sta4, sta5]
