class sportswomen():
    def __init__(self, name, major, gold_medal, silver_medal, bronze_medal):
        self.name = name
        self.major = major
        self.__gold_medal = gold_medal  # privat variable
        self._silver_medal = silver_medal  # protected variable
        self.bronze_medal = bronze_medal  # public variable

    def athlete_information(self):
        return "name : {} major: {}".format(athlete.name, athlete.major)

    def gold_print(self):
        g_medal = self.__gold_medal
        return g_medal


athlete = sportswomen("jack", "100m", 2, 3, 9)
print(athlete.athlete_information())

print("number of bronze medals:", athlete.bronze_medal)
print("number of silver medals:", athlete._silver_medal)
print("number of gold medals:", athlete.gold_print())
