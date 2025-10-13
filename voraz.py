from classes import Subject, Student, Request

def priority_total(student):
    return sum(request.priority for request in student.requests)


def weighting(students, subjects, i):

    results = []
    
    for student in students:
        for request in student.requests:
            if request.code == subjects[i].code:
                subject_code = request.code
                value = request.priority / priority_total(student)
                results.append((student.code, subject_code, value))
    
    return sorted(results, key=lambda x: x[2], reverse=True)


def dissatisfaction(assignments, students, i):

    student = students[i]
    assigned = set()
    accumulated_dissatisfaction = 0

    
    for student_code, (subject_code, weight) in assignments:
        if student_code == student.code:
            assigned.add((student_code, (subject_code, weight)))

    
    for _, (_, weight) in assigned:
        accumulated_dissatisfaction += weight

    subject_diff = 1 - (len(assigned) / len(student.requests))
    avg_dissatisfaction = 1 - accumulated_dissatisfaction

    return subject_diff * avg_dissatisfaction


def rocV(subjects, students):
    """
    Implementación del algoritmo voraz ROCV.
    Devuelve:
      - costo promedio de insatisfacción (float)
      - lista de estudiantes con sus asignaciones actualizadas
    """
    A = []
    i = 0
    total_dissatisfaction = 0
    r = len(students)
    k = len(subjects)
    
    # Asignación greedy
    while i < k:
        if subjects[i].quota > 0:
            weightings = weighting(students, subjects, i)
            while weightings and subjects[i].quota > 0:
                best = weightings.pop(0)
                A.append((best[0], (best[1], best[2])))
                subjects[i].quota -= 1
        i += 1


    for h in range(r):
        total_dissatisfaction += dissatisfaction(A, students, h)
    avg_dissatisfaction = total_dissatisfaction / r

    
    assignments = []
    for student in students:
        assigned_reqs = []
        for student_code, (subject_code, weight) in A:
            if student_code == student.code:
                assigned_reqs.append(Request(subject_code, weight))
        
        assigned_student = Student(student.code, assigned_reqs)
        assignments.append(assigned_student)
    print(avg_dissatisfaction)
    return avg_dissatisfaction, assignments
