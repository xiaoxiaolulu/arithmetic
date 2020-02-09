"""

"""


class EmployeeManagement:

    raise_pct = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return "{}{}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_pct)

    def __repr__(self):
        return "EmployeeManagement('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{}-{}".format(self.fullname(), self.pay)
