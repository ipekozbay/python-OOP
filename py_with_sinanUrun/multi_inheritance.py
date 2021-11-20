class footballer():
    running = "can run"
    outrun = "can outrun"
    salary = 5000

    def __init__(self,foot="right") :
        self.position = "striker"
        self.foot=foot
      
class basketball_player():
    tourniquet = "can tourniquet"
    three_point = "can throw threee point"

    def __init__(self) :
        self.region = "Further"
    
class multi_sportsman(footballer,basketball_player):

    def __init__(self,foot):
        basketball_player.__init__(self)
        footballer.__init__(self,foot)

eva = multi_sportsman("left") 

print(eva.tourniquet)
print(eva.salary) 
print(eva.position)
print(eva.region)
print(eva.foot)