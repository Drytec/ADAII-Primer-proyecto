from classes import Student
import itertools
from functions import generalDissatisfaction


def generate_subject_comb(subjects):
    subsets = []
    for r in range(len(subjects) + 1):
        subsets.extend(itertools.combinations(subjects, r))
    return subsets


def create_dictionary(subjects):
    dict = {}
    for subject in subjects:
        dict[subject.code] = subject.quota
    return dict


def is_comb_valid(combination, subject_dict):
    local_dict = subject_dict.copy()
    for student_comb in combination:
        if student_comb:
            for request in student_comb:
                if local_dict[request.code] != 0:
                    local_dict[request.code] -= 1
                else:
                    return False
    return True


def create_students(requests_list):
    students_list = []
    for i in range(len(requests_list)):
        i_to_str = i + 1
        student = Student("e" + str(i_to_str), requests_list[i])
        students_list.append(student)

    return students_list


def rocFB(initial_subjects, initial_students):
    # All possible subject combinations for each student
    subsets_list = [
        generate_subject_comb(student.requests) for student in initial_students
    ]

    subject_dictionary = create_dictionary(
        initial_subjects
    )  # Dictionary to access subjects easily

    solution_array = []  # List to store each solution
    for combination in itertools.product(*subsets_list):
        if is_comb_valid(combination, subject_dictionary):
            students = create_students(combination)
            solution_array.append(students)
    dissatisfaction_array = []

    for i in range(len(solution_array)):
        dissatisfaction_array.append(
            generalDissatisfaction(initial_students, solution_array[i])
        )
    best_dissatisfaction = min(dissatisfaction_array)
    print(best_dissatisfaction)
    return best_dissatisfaction, solution_array[
        dissatisfaction_array.index(best_dissatisfaction)
    ]
