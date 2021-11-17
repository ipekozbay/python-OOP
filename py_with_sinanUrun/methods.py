class worker:

    raise_rate = 1.05
    employee_number = 0

    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary
        self.mail = self.name+self.last_name + "@factory.com"
        worker.employee_number += 1

    def full_name(self):
        return "name: {}, last name: {}".format(self.name, self.last_name)

    def increase(self):
        #self.salary=(self.salary * worker.raise_rate)
        self.salary = (self.salary * self.raise_rate)

    @classmethod
    def raise_rate_change(cls, new_rate):
        cls.raise_rate = new_rate

    @classmethod
    def new_employee(cls, employee_information):
        name, last_name, salary = Memployee1.split("-")
        return cls(name, last_name, salary)

    @staticmethod
    def phone_number(phone):
        return phone.split()


employee1 = worker("ipek", "ozbay", 1000)
employee2 = worker("zeynep", "yarbasi", 2000)

Memployee1 = "veli-can-400"
Memployee2 = "ali-mert-100"

worker.raise_rate_change(1.5)
employee1.increase()
print(employee1.salary)

worker.raise_rate_change(1.5)
employee2.increase()
print(employee2.salary)

new_employee1 = worker.new_employee(Memployee1)
print(new_employee1.mail)

phone1 = "0123 654 78 88 "
print(worker.phone_number(phone1))