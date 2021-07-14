class Customer():

    def __init__(self, id, customer_number):
        self.id = id
        self.customer_number = customer_number

    def register() :
        option = int(input("if you are a corporate customer press 1 or if you are a individual customer press 2 : "))

        if option == 1 :
                
                companİES = []
                company_numberS = []

                company = input("enter your company name :")
                comp_num = int(input("enter your company number :"))

                if (company in companİES) : 
                    print("this company is already registered  ")
                    
                else:
                    print("this company registered.")    
                    companİES.append(company)

                if comp_num in company_numberS: 
                    print("this company number is already registered  ")

                else:
                    print("this company number registered.")    
                    companİES.append(comp_num)

        else: # for indıvidual customer 

                person_nationaity_numberS = []
                person_mailS = []
                person_telephone_numberS = []

                nation_num = int(input("enter your nationality number: "))
                e_mail = input("enter your mail : ")
                tel_number = int(input("entr your telephone number "))

                if nation_num in  person_nationaity_numberS:
                    print("this nationality number is already registered.")


                else:
                    print("this nationality number registered.")
                    person_nationaity_numberS.append(nation_num)    

                if e_mail in person_mailS  :
                    print("this mail is already registered.")

                else:
                    print("this mail registered.")
                    person_mailS.append(e_mail)  

                if tel_number in person_telephone_numberS  :
                    print("this telephone number is already registered.")

                else:
                    print("this telephone number registered.")
                    person_telephone_numberS.append(tel_number)      
                       

class individual_customer(Customer):
    def __init__(self, nationality_id, name,telephone_number, password, mail ):
        Customer.__init__(self, 1,147852963)

        self.nationality_id = nationality_id
        self.name = name
        self.telephone_number = telephone_number
        self.password = password
        self.mail = mail

class corporate_customer(Customer):
    def __init__(self, company_name, company_number):
        Customer.__init__(self ,2,145214521)

        self.company_name = company_name
        self.company_number = company_number

customer_1 = Customer(1,1451452145)
individual_customer_1 = individual_customer(123456789111 , "ipek",552555255,"1111","ipek@gmail.com")
corporate_customer_1 = corporate_customer("microsoft","03214555")
individual_customer_2 = individual_customer

print(customer_1.id, "-" ,customer_1.customer_number)
print(individual_customer_1.name)
print(corporate_customer_1.company_name)

individual_customer_2.register() 
