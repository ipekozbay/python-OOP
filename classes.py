<<<<<<< HEAD
class Flying():
    airline = "THY"

    def __init__(self, code,departure,arrival,time,capacity,passenger):
        self.code=code
        self.departure=departure
        self.arrival=arrival
        self.time=time
        self.capacity=capacity
        self.passenger=passenger

    def __repr__(self):
        print("{} coded plane was introduced to the system ".format(self.code))    

    def make_announcement(self ):

        return "code: {} , flying {} - {} ,time: {} min".format(
            self.code,
            self.departure,
            self.arrival,
            self.time)

    def number_of_seats_update(self):
        return self.capacity - self.passenger

    def ticket_sales(self , ticket_amount=1):

        if self.passenger + ticket_amount <= self.capacity:

            self.passenger += ticket_amount 
            self.number_of_seats_update()

            print("{} amount ticket saled , number of seats remaining {} . ".format(
                  ticket_amount,
                   self.number_of_seats_update()
            ))
        else:
            print("transaction did not occur")    

    def ticket_cancellation(self , ticket_amount=1):
        if self.passenger >= ticket_amount:

            self.passenger -= ticket_amount
            print("{} amount ticket has been canceled , current number of seats {} . ".format(
                ticket_amount,
                self.number_of_seats_update()
            ))

        else:
            print("transaction did not occur")  

flying_1 = Flying('TK78','23.00','01.55',175,200,150)

announcement = flying_1.make_announcement()
current_issue = flying_1.number_of_seats_update()

flying_1

print(announcement)
print("remaining ticket ",current_issue)

flying_1.ticket_sales(75)
flying_1.ticket_sales(5)
flying_1.ticket_cancellation(5)
=======
class Ucus():
    havayolu = "THY"

    def __init__(self, kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons_yap(self ):

        return "{} sefer sayılı  {} - {} ucusumuz {} dk surecek".format(
            self.kod,
            self.kalkis,
            self.varis,
            self.sure)

ucus2 = Ucus('TK78','23.00','01.55',175,200,150)
cikti=ucus2.anons_yap()
print(cikti)
>>>>>>> 22be60fa3573a02d3ba29af614fbcd176f072294
