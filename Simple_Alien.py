class Alien:
    def __init__(self, x_coordinate, y_coordinate, health=3):
        super(self, Alien).__init__
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        
        self.alive = True

    def hit(self) -> int:
        self.health = self.health - 1
        return self.health
    
    def is_alive(self) -> bool:

        if self.health > 0:
            return self.alive
        else:
            self.alive = False
            return self.alive
        
    def collision_detection(self, other_object) -> None:
        pass


alien = Alien(2,0)
print(alien.x_coordinate)
print(alien.y_coordinate)
print(alien.health)
print(alien.hit())
print(alien.health)
print(alien.is_alive())