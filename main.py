from classes import Subject, Student, Request
from functions import dissatisfaction, generalDissatisfaction
from itertools import combinations
from parser import parse_test_file


# j: student iter
# l: request iter
# i: subject iter
def rocPD(j, quotas):
    key = (j, quotas)

    if key in store:
        return store[key]

    if j == len(E):
        return (0, [])

    student = E[j]
    best = float("inf")
    bestAssignation = None

    # Case 1
    noAssignDissatisfaction = dissatisfaction(student, [])
    dissatisfactionRest, assignationRest = rocPD(j + 1, quotas)
    best = noAssignDissatisfaction + dissatisfactionRest
    bestAssignation = [Student(student.code, [])] + assignationRest

    requests = student.requests

    # Case 2
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


if __name__ == "__main__":
    print("1. rocFB \n2. rocV \n3. rocPD")
    option = int(input("\nDígite una opción: "))

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        test = int(
            input(
                "\nDigite el número del test a ejecutar (acorde a la batería de pruebas): "
            )
        )

        M, E = parse_test_file(f"tests/Prueba{test}.txt")
        store = {}
        quotas = tuple(subject.quota for subject in M)
        cost, A = rocPD(0, quotas)
        print(cost / len(A))
