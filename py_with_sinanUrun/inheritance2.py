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
        self.salary=(self.salary * worker.raise_rate)
        #self.salary = (self.salary * self.raise_rate)

class developer(worker):
    def __init__(self, name, last_name, salary,language):
        # worker.__init__(self,name,last_name,salary)
        super().__init__( name, last_name,salary)
        self.language=language
        self.raise_rate=2

class manager(worker):
    def __init__(self, name, last_name, salary,workers=None):
        super().__init__(name, last_name, salary)

        if workers is None:
            self.workers = []
        else :
            self.workers = workers 

    def personel_add(self,personel):
        self.workers.append(personel)

    def personel_delete(self,personel):
        self.workers.remove(personel)

    def list_employees(self):
        for personel in self.workers:
            print(personel.full_name())
                  
employee1 = worker("ali", "veli", 1000)
employee2 = worker("memehmet", "aslan", 1000)

dev1 = developer("lale","cicek",10000,"python")

#print(dev1.full_name())
# print(dev1.salary)
# dev1.increase()
# print(dev1.salary)

manager1 = manager("rüveyha","sahin",10000,[dev1,employee1])
print(manager1.list_employees())
manager1.personel_add(employee2)
print(manager1.list_employees())
manager1.personel_delete(employee1)
print(manager1.list_employees())

print(isinstance(employee1,worker))
print(issubclass(worker,developer))