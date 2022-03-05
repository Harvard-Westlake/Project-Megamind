import pygame
import time

pygame.init()

screenX = 1200
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

playerImg = pygame.image.load("spaceship.png")
playerImg = pygame.transform.scale(playerImg, (50, 50))
playerImg = pygame.transform.rotate(playerImg, 270)
player = [20, (screenY-150)/2 - 25, 0, 0]

planets = []

babyImg = pygame.image.load("Baby.png")
babyImg = pygame.transform.scale(babyImg, (20, 40))
babyImg = pygame.transform.rotate(babyImg, 270)

def drawBaby(x, y):
    screen.blit(babyImg, (x - 10, y - 20))

running = True

def drawBackground():
    screen.fill((0, 0, 0))

def drawPlayer(x, y):
    screen.blit(playerImg, (x, y))

def addPlanet(imageName,size):
    planets.append([imageName,size])

def importPlanets(planetArray): #planetArray must be a 2d array of planets
    planetLocations = []
    loc = [screenX - 20, screenY -75]  # x position of next planet; gets updated after every planet placement
    for planet in planetArray:
        planetLocations.append([planet[0], planet[1], loc[0]-planet[1], loc[1]])
        loc[0] = loc[0] - 50 - 2 * planet[1]
        print(loc)
    return planetLocations

def drawPlanet(planet):
    planetImg = pygame.image.load(planet[0])
    planetImg = pygame.transform.scale(planetImg, (planet[1]*2, planet[1]*2))
    planetImg = pygame.transform.rotate(planetImg, 270)
    planetImg = pygame.transform.rotate(planetImg, 270)
    screen.blit(planetImg,(planet[2]-planet[1], planet[3]-planet[1]))


def drawPlanetBarRect():
    planetBarRect = pygame.image.load("planetBar.png")
    planetBarRect = pygame.transform.scale(planetBarRect, (screenX,150))
    screen.blit(planetBarRect,(0,screenY - 150))




addPlanet("Planet1.png",70)
addPlanet("Planet2.png",40)
addPlanet("Planet3.png",50)
addPlanet("Planet4.png",60)
print(planets)
planets = importPlanets(planets)
print(planets)
prevTime = 0
currentTime = time.time()
speed = 100
babyCoords = [-200, -200, 0]
fired = False
while running:

    prevTime = currentTime
    currentTime = time.time()
    gap = currentTime - prevTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_s:
                player[3] = 5
            if event.key == pygame.K_w:
                player[3] = -5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player[3] = 0
            if event.key == pygame.K_SPACE:
                if not fired:
                    fired = True
                    babyCoords = []
                    for coord in player:
                        babyCoords.append(coord)
                    babyCoords.append(5)
                    babyCoords[0] += 70
                    babyCoords[1] += 35


    move = player[1] + player[3]*speed*gap
    if move < 400 and move > 0:
        player[1] = move

    babyCoords[0] += 3*gap*speed
    print(babyCoords[2])

    drawBackground()
    drawPlanetBarRect()
    drawPlayer(player[0], player[1])
    drawBaby(babyCoords[0], babyCoords[1])
    for planet in planets:
        drawPlanet(planet)
    pygame.display.update()
