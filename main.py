from classes import Subject, Student, Request
from functions import dissatisfaction, generalDissatisfaction
from itertools import combinations


def rocPD(j, quotas):
    key = (j, quotas)

    if key in store:
        return store[key]

    if j == len(E):
        return (0, [])

    student = E[j]
    best = float("inf")
    bestAssignation = []

    # Case 1
    noAssignDissatisfaction = dissatisfaction(student, [])
    dissatisfactionRest, assignationRest = rocPD(j + 1, quotas)
    best = noAssignDissatisfaction + dissatisfactionRest
    bestAssignation = [Student(student.code, [])] + assignationRest

    requests = student.requests

    for l in range(1, len(requests) + 1):
        for combination in combinations(requests, l):
            newQuotas = list(quotas)
            valid = True

            for request in combination:
                i = next(
                    (i for i, subject in enumerate(M) if subject.code == request.code)
                )

                if newQuotas[i] <= 0:
                    valid = False
                    break

                newQuotas[i] -= 1

            if not valid:
                continue

            combinationDissatisfaction = dissatisfaction(student, combination)
            dissatisfactionNext, assignationNext = rocPD(j + 1, tuple(newQuotas))
            totalDissatisfaction = combinationDissatisfaction + dissatisfactionNext

            if totalDissatisfaction < best:
                best = totalDissatisfaction
                bestAssignation = [Student(student.code, combination)] + assignationNext

    store[key] = (best, bestAssignation)

    return store[key]


M = [Subject("m1", 3), Subject("m2", 4), Subject("m3", 2)]
E = [
    Student("e1", [Request("m1", 5), Request("m2", 2), Request("m3", 1)]),
    Student("e2", [Request("m1", 4), Request("m2", 1), Request("m3", 3)]),
    Student("e3", [Request("m2", 3), Request("m3", 2)]),
    Student("e4", [Request("m1", 2), Request("m3", 3)]),
    Student("e5", [Request("m1", 3), Request("m2", 2), Request("m3", 3)]),
]

store = {}

initial_cupos = tuple(m.quota for m in M)

min_dissatisfaction, best_assignments = rocPD(0, initial_cupos)

print(f"\nInconformidad mínima total: {min_dissatisfaction:.4f}\n")
for student, assigned in zip(E, best_assignments):
    codes = [req.code for req in assigned.requests]
    print(f"{student.code}: {codes}")
