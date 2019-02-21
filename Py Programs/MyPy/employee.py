class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self):
        return '{} {}'.format(self.first, self.last)

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

if __name__ == '__main__':
    emp_0 = Employee('Brandon', 'Rowe', '50000')
    emp_1 = Employee('Joe', 'McGinnis', '50000')
    emp_2 = Employee('Jimmy', 'Spann', '45000')
    print(emp_0.fullName())
    print(emp_0.email())
    print(emp_1.fullName())
    print(emp_1.email())
    print(emp_2.fullName())
    print(emp_2.email())
