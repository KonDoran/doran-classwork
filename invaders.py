import pygame
import random
import math

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Snow")
# -- Exit game flag set to false
done = False
# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()

## -- Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # Set the speed of the sprite
        self.speed = speed
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = 1
    #End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
#End Class

## -- Define the class snow which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        # Set the speed of the sprite
        self.speed = 0
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
        self.speed = 1
    #End Procedure
    def update(self):
        if 
    def player_set_speed(val):
        self.speed = val
#End Class

        
# Create the snowflakes
number_of_invaders = 50 # we are creating 50 snowflakes
for x in range (number_of_invaders):
    my_invaders = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_group.add(my_invaders) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add(my_invaders) # adds it to the group of all Sprites
#Next
player = Player(YELLOW, 10, 10)
all_sprites_group.add(player)
### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN: # - a key is down
            if event.key == pygame.K_LEFT: # - if the left key pressed
                player.player_set_speed(-3) # speed set to -3
            elif event.key == pygame.K_RIGHT: # - if the right key pressed
                player.player_set_speed(3) # speed set to 3
        elif event.type == pygame.KEYUP: # - a key released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.player_set_speed(0) # speed set to 0
        #End If
    #Next event
    # -- Game logic goes after this comment
    all_sprites_group.update()
    player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    all_sprites_group.draw(screen)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
     # - The clock ticks over
    clock.tick(60)
    #End While - End of game loop
pygame.quit()
