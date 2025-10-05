# === Clases y funciones base ===
class Subject:
    def __init__(self, code, quote):
        self.code = code
        self.quote = quote


class Request:
    def __init__(self, code, priority):
        self.code = code
        self.priority = priority

    def __eq__(self, other):
        return self.code == other.code and self.priority == other.priority


class Student:
    def __init__(self, code, requests):
        self.code = code
        self.requests = requests
        self.priorityCapacity = 3 * len(requests) - 1


def dissatisfaction(student, assignations):
    priorityCapacity = student.priorityCapacity
    requests = student.requests
    unassignedPrioritySum = sum(r.priority for r in requests if r not in assignations)

    return (1 - len(assignations) / len(requests)) * (
        unassignedPrioritySum / priorityCapacity
    )


# === Generador manual de combinaciones ===
def get_combinations(elements, r):
    if r == 0:
        return [[]]
    if len(elements) < r:
        return []
    first = elements[0]
    rest = elements[1:]
    with_first = [[first] + c for c in get_combinations(rest, r - 1)]
    without_first = get_combinations(rest, r)
    return with_first + without_first


# === Datos ===
M = [Subject("m1", 3), Subject("m2", 4), Subject("m3", 2)]
E = [
    Student("e1", [Request("m1", 5), Request("m2", 2), Request("m3", 1)]),
    Student("e2", [Request("m1", 4), Request("m2", 1), Request("m3", 3)]),
    Student("e3", [Request("m2", 3), Request("m3", 2)]),
    Student("e4", [Request("m1", 2), Request("m3", 3)]),
    Student("e5", [Request("m1", 3), Request("m2", 2), Request("m3", 3)]),
]

initial_cupos = tuple(m.quote for m in M)

# === DP sin lru_cache ===
memo = {}


def dp(i, cupos):
    key = (i, cupos)
    if key in memo:
        return memo[key]

    if i == len(E):
        return (0, [])

    student = E[i]
    best_score = float("inf")
    best_assign = []

    # Caso 1: no asignar materias
    score_no = dissatisfaction(student, [])
    score_rest, assign_rest = dp(i + 1, cupos)
    total = score_no + score_rest
    best_score = total
    best_assign = [[]] + assign_rest

    # Caso 2: probar todas las combinaciones de materias posibles
    for r in range(1, len(student.requests) + 1):
        for subset in get_combinations(student.requests, r):
            new_cupos = list(cupos)
            valid = True
            for req in subset:
                idx = next((j for j, m in enumerate(M) if m.code == req.code), None)
                if idx is None or new_cupos[idx] <= 0:
                    valid = False
                    break
                new_cupos[idx] -= 1
            if not valid:
                continue

            score_here = dissatisfaction(student, subset)
            score_next, assign_next = dp(i + 1, tuple(new_cupos))
            total = score_here + score_next

            if total < best_score:
                best_score = total
                best_assign = [subset] + assign_next

    memo[key] = (best_score, best_assign)
    return memo[key]


# === Ejecutar ===
min_dissatisfaction, best_assignments = dp(0, initial_cupos)

print(f"\nInconformidad mínima total: {min_dissatisfaction:.4f}\n")
for student, assigned in zip(E, best_assignments):
    codes = [req.code for req in assigned]
    print(f"{student.code}: {codes}")
