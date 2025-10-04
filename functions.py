def dissatisfaction(student, studentAssignation):
    priorityCapacity = student.priorityCapacity
    requests = student.requests
    assignations = studentAssignation.requests
    unassignedPrioritySum = 0

    for request in requests:
        if request not in assignations:
            unassignedPrioritySum += request.prioriy

    return (1 - len(assignations) / len(requests)) * (
        unassignedPrioritySum / priorityCapacity
    )


def generalDissatisfaction(students, studentsAssignations):
    dissatisfactionSum = 0

    for student, studentAssignation in zip(students, studentsAssignations):
        dissatisfactionSum += dissatisfaction(student, studentAssignation)

    return dissatisfactionSum / len(students)
