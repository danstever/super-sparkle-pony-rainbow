import pygame, sys, time
pygame.init()

X_SZ = 700
Y_SZ = 500
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
ORANGE = (255,127,0)
YELLOW = (255,255,0)
BLUE = (0,255,255)
INDIGO = (0,0,255)
VIOLET = (255,0,255)
SKYBLUE = (127,255,255)
SPECTRUM = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET]

def drawRainbow(xMin, yMin, xMax, yMax, width):
    for ndx in range(0,7):
        minOffset = width * ndx
        maxOffset = (2 * width * ndx)
        pygame.draw.ellipse(screen, SPECTRUM[ndx], [xMin + minOffset, yMin + minOffset, xMax - maxOffset - width, yMax - maxOffset], width)
    
def drawTitleScreen():
    screen.fill(SKYBLUE)
    drawRainbow(-X_SZ, 20, X_SZ * 3, Y_SZ*2, 50)
    font = pygame.font.SysFont('Calibri', 100, True, False)
    textSS = font.render("Super Sparkle", True, WHITE)
    textPR = font.render("Pony Rainbow", True, WHITE)
    
    screen.blit(textSS, [100,100])
    screen.blit(textPR, [100,250])

def eventLoop():
    # Loop until the user clicks the close button.
    done = False
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
            
            # --- Game logic should go here
            
            # --- Drawing code should go here
            #  First, clear the screen to white. Don't put other drawing commands
            #  above this, or they will be erased with this command.
            screen.fill(SKYBLUE)
            
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
            # --- Limit to 60 frames per second
            clock.tick(60)


size = (X_SZ, Y_SZ)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Super Sparkle Pony Rainbow")
drawTitleScreen()
pygame.display.flip()
time.sleep(10)

# game event loop
eventLoop()

# shut it down
pygame.quit