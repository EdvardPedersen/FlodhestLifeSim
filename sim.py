import pygame


TILE_SIZE = 100

class Melon:
    def __init__(self, koordinat, bilde):
        self.image = bilde
        self.coordinates = koordinat
        self.age = 0


    def avstand(self, other):
        x_avstand = abs(self.coordinates[0] - other.coordinates[0])
        y_avstand = abs(self.coordinates[1] - other.coordinates[1])
        return max(x_avstand, y_avstand)

    def draw(self, target):
        self.age += 1
        target.blit(self.image, (self.coordinates[0] * self.image.get_width(), self.coordinates[1] * self.image.get_height()))


def melon_spredning(koordinat, meloner):
    ny_melon = Melon(koordinat, None)
    grense = 1
    antall = 0
    for melon in meloner:
        if melon.coordinates == koordinat:
            return False
        if ny_melon.avstand(melon) < 2 and melon.age > 2:
            antall += 1
    if antall > grense:
        return True
    return False

def naboer(koordinat):
    naboer = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            nabo = (koordinat[0] + x, koordinat[1] + y)
            if nabo != koordinat:
                naboer.append(nabo)
    return naboer

class Flodhest:
    def __init__(self, coordinates, image):
        self.coordinates = coordinates
        self.images = image
        self.state = "eating"

    def avstand(self, other):
        x_avstand = abs(self.coordinates[0] - other.coordinates[0])
        y_avstand = abs(self.coordinates[1] - other.coordinates[1])
        return max(x_avstand, y_avstand)

    def draw(self, target):
        target.blit(self.images[self.state], (self.coordinates[0] * self.images[self.state].get_width(), self.coordinates[1] * self.images[self.state].get_height()))

    def move(self, x, y):
        self.coordinates = (self.coordinates[0] + x, self.coordinates[1] + y)

    def simulate(self, melons):
        target = melons[0]
        min_avstand = self.avstand(melons[0])
        for melon in melons:
            avstand = self.avstand(melon)
            if avstand < min_avstand:
                target = melon
        x_move = target.coordinates[0] - self.coordinates[0]
        y_move = target.coordinates[1] - self.coordinates[1]
        x_move /= max(abs(x_move), 1)
        y_move /= max(abs(y_move), 1)
        if(abs(x_move) + abs(y_move) == 0):
            self.state = "eating"
        else:
            self.state = "idle"
        self.move(x_move, y_move)




def load_image(filename):
    return pygame.transform.scale(pygame.image.load(filename).convert_alpha(), (TILE_SIZE, TILE_SIZE))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    meloner = []
    flodhester = []

    flodhest_images = {"idle": load_image("sprites/flodhest.png"), 
                       "walking": load_image("sprites/standing_flodhest.png"),
                       "eating": load_image("sprites/flodhest_eating.png")}
    melon_img = load_image("sprites/melon.png")
    meloner.append(Melon((2, 2), melon_img))
    meloner.append(Melon((1, 2), melon_img))
    flodhester.append(Flodhest((8,8), flodhest_images))

    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((100, 100, 255))

        for melon in meloner:
            melon.draw(screen)

        for flodhest in flodhester:
            flodhest.draw(screen)
            flodhest.simulate(meloner)

        nye_meloner = []
        for melon in meloner:
            for nabo in naboer(melon.coordinates):
                if nabo in nye_meloner:
                    continue
                if melon_spredning(nabo, meloner):
                    nye_meloner.append(nabo)

        for c in nye_meloner:
            meloner.append(Melon(c, melon_img))

        print(len(meloner))

        pygame.display.update()
        pygame.time.delay(1000)


