from itertools import combinations

from classes import Student
from functions import dissatisfaction

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
