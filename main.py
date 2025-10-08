from itertools import combinations
from pathlib import Path

from classes import Student
from functions import dissatisfaction, generalDissatisfaction
from parser import parse_test_file


RESULTS_DIR = Path("results")


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
    bestAssignation = []

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

            combination_list = list(combination)
            combinationDissatisfaction = dissatisfaction(student, combination_list)
            dissatisfactionNext, assignationNext = rocPD(j + 1, tuple(newQuotas))
            totalDissatisfaction = combinationDissatisfaction + dissatisfactionNext

            if totalDissatisfaction < best:
                best = totalDissatisfaction
                bestAssignation = [Student(student.code, combination_list)] + assignationNext

    store[key] = (best, bestAssignation)

    return store[key]


def solve_roc_pd(subjects, students):
    global M, E, store

    M = subjects
    E = students
    store = {}
    quotas = tuple(subject.quota for subject in M)

    return rocPD(0, quotas)


def write_result_file(test_number, students, assignments, total_cost):
    RESULTS_DIR.mkdir(exist_ok=True)

    if students:
        general_cost = generalDissatisfaction(students, assignments)
    else:
        general_cost = 0.0

    lines = [f"{general_cost:.4f}"]

    for student, assigned in zip(students, assignments):
        assigned_requests = list(getattr(assigned, "requests", []))
        lines.append(f"{student.code},{len(assigned_requests)}")
        for request in assigned_requests:
            lines.append(request.code)

    output_path = RESULTS_DIR / f"Result{test_number}.txt"
    output_path.write_text("\n".join(lines), encoding="utf-8")

    return output_path


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

    subjects, students = parse_test_file(f"tests/Prueba{test}.txt")
    cost, assignments = solve_roc_pd(subjects, students)
    output_path = write_result_file(test, students, assignments, cost)
    print(f"Resultado generado en: {output_path}")
