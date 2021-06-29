import pygame

win_width = 600
win_height = 480

background_color = (0, 0, 255)

window = pygame.display.set_mode([win_width, win_height])

running = True 


def update():
    window.fill(background_color)
    pygame.display.flip()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update()
