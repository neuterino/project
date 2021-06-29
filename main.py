import pygame

# init
pygame.init()
clock = pygame.time.Clock()

# display
win_width = 600
win_height = 480

window = pygame.display.set_mode([win_width, win_height])

pygame.display.set_caption("big project")


# variables for easy understanding
fps = 60

# colors
background_color = (0, 0, 255)


# other variables
running = True

# code
def update():
    """things to do every frame"""

    window.fill(background_color)
    pygame.display.flip()


while running: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update()

    clock.tick(fps)
