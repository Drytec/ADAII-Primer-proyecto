from itertools import combinations
from pathlib import Path

from classes import Student
from functions import dissatisfaction, generalDissatisfaction
from parser import parse_test_file


RESULTS_DIR = Path("results")


def rocPD(subjects, students):
    store = {}
    initial_quotas = tuple(subject.quota for subject in subjects)

    def solve(j, quotas):
        key = (j, quotas)

        if j == len(students):
            return 0, []

        if key in store:
            return store[key]

        student = students[j]
        best_cost = float("inf")
        best_assignments = []

        no_assign_cost = dissatisfaction(student, [])
        rest_cost, rest_assignments = solve(j + 1, quotas)
        best_cost = no_assign_cost + rest_cost
        best_assignments = [Student(student.code, [])] + rest_assignments

        for l in range(1, len(student.requests) + 1):
            for combination in combinations(student.requests, l):
                new_quotas = list(quotas)
                valid = True

                for request in combination:
                    idx = next(
                        (
                            idx
                            for idx, subject in enumerate(subjects)
                            if subject.code == request.code
                        ),
                        None,
                    )

                    if idx is None or new_quotas[idx] <= 0:
                        valid = False
                        break

                    new_quotas[idx] -= 1

                if not valid:
                    continue

                combination_list = list(combination)
                dissat_cost = dissatisfaction(student, combination_list)
                rest_cost, rest_assignments = solve(j + 1, tuple(new_quotas))
                total_cost = dissat_cost + rest_cost

                if total_cost < best_cost:
                    best_cost = total_cost
                    best_assignments = [
                        Student(student.code, combination_list)
                    ] + rest_assignments

        store[key] = (best_cost, best_assignments)
        return store[key]

    return solve(0, initial_quotas)


def write_result_file(test_number, students, assignments):
    RESULTS_DIR.mkdir(exist_ok=True)

    general_cost = generalDissatisfaction(students, assignments) if students else 0.0

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
        cost, assignments = rocPD(subjects, students)
        write_result_file(test, students, assignments)

