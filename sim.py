import pygame

TILE_SIZE = 100

def melon_spredning(koordinat, meloner):
    grense = 2
    antall = 0
    if koordinat in meloner:
        return False
    for melon in meloner:
        if abs(melon[0] - koordinat[0]) < 2 and abs(melon[1] - koordinat[1]) < 2:
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

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    meloner = []
    flodhester = []

    meloner.append((2, 2))
    flodhester.append((0, 0))

    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        screen.fill((100, 100, 255))

        for melon in meloner:
            screen.fill((255,0,0), (melon[0] * TILE_SIZE, melon[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for flodhest in flodhester:
            screen.fill((155,155,155), (flodhest[0] * TILE_SIZE, flodhest[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        for i in range(len(flodhester)):
            f = flodhester[i]
            flodhester[i] = (f[0] + 1, f[1] + 1)

        for melon in meloner:
            print(naboer(melon))

        pygame.display.update()
        pygame.time.delay(1000)


