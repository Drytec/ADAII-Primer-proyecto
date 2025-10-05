class Subject:
    def __init__(self, code, quote):
        self.code = code
        self.quote = quote


class Student:
    def __init__(self, code, requests):
        self.code = code
        self.requests = requests
        self.priorityCapacity = 3 * len(requests) - 1


class Request:
    def __init__(self, code, priority):
        self.code = code
        self.priority = priority

    def __eq__(self, other):
        if not isinstance(other, Request):
            return NotImplemented

        return self.code == other.code and self.priority == other.priority
