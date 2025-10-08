from classes import Subject, Student, Request
from functions import dissatisfaction, generalDissatisfaction
from itertools import combinations
from parser import parse_test_file


# j: student iter
# l: request iter
# i: subject iter
def rocPD2(M, E):
    store = {}
    quotas = tuple(subject.quota for subject in M)

    def F(j, quotas):
        key = (j, quotas)

        if j == len(E):
            return 0, []

        if key in store:
            return store[key]

        student = E[j]
        bestCost = float("inf")
        bestAssignments = []

        for l in range(0, len(student.requests) + 1):
            for combination in combinations(student.requests, l):
                newQuotas = list(quotas)
                valid = True

                for request in combination:
                    i = next(
                        (
                            i
                            for i, subject in enumerate(M)
                            if subject.code == request.code
                        )
                    )
                    if newQuotas[i] <= 0:
                        valid = False
                        break
                    newQuotas[i] -= 1

                if not valid:
                    continue

                dissat = dissatisfaction(student, combination)
                restCost, restAssignments = F(j + 1, tuple(newQuotas))
                totalCost = dissat + restCost

                if totalCost < bestCost:
                    bestCost = totalCost
                    bestAssignments = [
                        Student(student.code, list(combination))
                    ] + restAssignments

        store[key] = (bestCost, bestAssignments)
        return store[key]

    return F(0, quotas)


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
        cost, A = rocPD(M, E)
        print(cost / len(A))
