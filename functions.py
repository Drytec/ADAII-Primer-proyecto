def dissatisfaction(student, assignations):
    priorityCapacity = student.priorityCapacity
    requests = student.requests
    unassignedPrioritySum = sum(r.priority for r in requests if r not in assignations)

    return (1 - len(assignations) / len(requests)) * (
        unassignedPrioritySum / priorityCapacity
    )


def generalDissatisfaction(students, studentsAssignations):
    dissatisfactionSum = sum(
        dissatisfaction(s, a.requests) for s, a in zip(students, studentsAssignations)
    )

    return dissatisfactionSum / len(students)
