class Hero:
    def __init__(self, name):
        self.name = name
        self.lives = 3
        self.level = 1
    def hallo(self):
        print("Привет я "  + self.name)


hero1 = Hero('Superman')
hero1.hallo()
hero2 = Hero ('RocketBoss')




