import pygame

pygame.init()

clock = pygame.time.Clock()
speed = 30

display_width = 500
display_height = 300

x = 100
y = 100
radius = 10
dx = 3
dy = 3

display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("That's A Ball, For Sure!")

while True:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((0,0,0))
    x += dx
    y += dy

    pygame.draw.circle(display, (255,255,255), (x,y), radius)

    if (x < radius) or (x > display_width - radius):
        dx *= -1
    if (y < radius) or (y > display_height - radius):
        dy *= -1

    pygame.display.update()

