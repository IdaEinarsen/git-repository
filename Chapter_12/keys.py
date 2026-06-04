import pygame
import sys


pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Key Test")

# Main loop
while True:
    for event in pygame.event.get():

        # Quit the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
        elif event.type == pygame.KEYDOWN:
            print(event.key)

    # screen color
    screen.fill((0, 0, 0))

    # Update display
    pygame.display.flip()