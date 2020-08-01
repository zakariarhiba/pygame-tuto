import pygame

# initialize the game
pygame.init()

# darori t7aded i7datiyat deal screen
screen = pygame.display.set_mode((800, 600))
# smiya & icon
pygame.display.set_caption("space game")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('nan.png')
playerx = 370
playery = 480

def player(x, y):
    screen.blit(playerimg, (x, y))

# darori dir loop bach matw9afch lgame
running = True
while running:
    # rgb change color
    screen.fill((0,0,0))
    """ ayi clique 3la chi button kate3tabr event o bach t5roj 5as darori te3ayt 3la event dealo houya hada """
    for event in  pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("up")

    player(playerx, playery)
    pygame.display.update()

    