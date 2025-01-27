class CollisionDetector(object):

    def __init__(self, ship, generator, projectiles):
        self.ship = ship
        self.generator = generator
        self.projectiles = projectiles  # list

    '''
    Check if the ship has been hit by an specific asteroid
    '''

    def ship_hits_asteroid(self, a, asteroid):
        return a.pos.distance(asteroid.pos) <= asteroid.size + a.size

    '''
    Checks if an specific asteroid has been hit by an 
    specific projectle
    '''

    def projectile_hits_asteroid(self, projectile, asteroid):
        return projectile.pos.distance(asteroid.pos) <= asteroid.size

    '''
    Handles the given MUTABLE types (asteroids and projectiles) when
    both collide.
    '''
    def handle_ship_hits_asteroid(self):
        for a in self.generator.asteroids:
            if self.ship_hits_asteroid(self.ship, a):
                return True
        return False

    def handle_projectile_hits_asteroid(self):
        # hit_asteroids = []
        for a in self.generator.asteroids:
                # self.generator.generate_debris(a.pos)
            for p in self.projectiles:
                if self.projectile_hits_asteroid(p, a):
                    self.generator.asteroids.remove(a)
                    self.projectiles.remove(p)
                    # self.generator.generate_debris(a.pos)
