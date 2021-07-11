class Travel():
  
    def __init__(self, departure,arrival): 
      self.departure=departure
      self.arrival=arrival

    def announcement(self):
        print(" welcome to {}-{} trip".format(self.departure , self.arrival)) 


class Ship(Travel):

  def __init__(self, breaking_places ):
    Travel.__init__(self , "FR", "TR")

    self.breaking_places = breaking_places

travel_1 = Travel("deu","tr")

departure=travel_1.departure
print(departure)

travel_1.announcement()

ship_1 = Ship(["tr","deu"])

departure_ship_1 = ship_1.departure
print(departure_ship_1)

arrival_ship_1 = ship_1.arrival
print(arrival_ship_1)

breaking_places_ship = ship_1.breaking_places
print(breaking_places_ship)