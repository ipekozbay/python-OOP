class worker:

    raise_rate = 1.05
    employee_number = 0
    def __init__(self,name,last_name,salary):
        self.name=name
        self.last_name=last_name
        self.salary=salary
        self.mail=self.name+self.last_name + "factory.com"
        worker.employee_number+=1

    def full_name(self):
        return  "name: {}, last name: {}".format(self.name,self.last_name) 

    def increase(self):   
        #self.salary=(self.salary * worker.raise_rate) 
        self.salary=(self.salary * self.raise_rate) 


employee1 = worker("ipek","ozbay",1000)
print(worker.employee_number)
employee2 = worker("zeynep","yarbasi",2000)
print(worker.employee_number)

print(employee2.full_name())
print(worker.full_name(employee1))

print(employee1.salary)
employee1.increase()
print(employee1.salary)

print(employee2.salary)
employee2.raise_rate=1.1 # raise rate changed externally
employee2.increase()
print(employee2.salary)