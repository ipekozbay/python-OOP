class worker:

    raise_rate = 1.05
    employee_number = 0

    def __init__(self,name,last_name,salary):
        self.name=name
        self.last_name=last_name
        self.salary=salary
        
        worker.employee_number+=1

    @property
    def email(self):
        self.mail = self.name+self.last_name + "factory.com"
        return self.mail
        
    @property
    def full_name(self):
        return  "name: {}, last name: {}".format(self.name,self.last_name) 

    @full_name.setter
    def full_name(self ,coming_name):
        name, last_name = coming_name.split(" ")
        self.name=name
        self.last_name=last_name
    
    @full_name.deleter
    def full_name(self):
        self.name=None
        self.last_name=None
        print("user's information deleted.")

    def increase(self):   
        #self.salary=(self.salary * worker.raise_rate) 
        self.salary=(self.salary * self.raise_rate) 


employee1 = worker("ipek","ozbay",1000)
employee2 = worker("zeynep","yarbasi",2000)

print(employee2.name)
print(employee2.email)
print(employee2.full_name)

employee2.full_name="ali veli"
print(employee2.name)
print(employee2.email)
print(employee2.full_name)

del employee2.full_name