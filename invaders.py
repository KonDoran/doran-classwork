import pygame
import random
import math

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Invaders")

score = 0  

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
        self.rect.y = random.randrange(-150, 0)
        self.speed = 1
    #End Procedure
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y > 480:
            self.rect.x = random.randrange(0, 600)
            self.rect.y = random.randrange(-50, 0)
#End Class

## -- Define the class snow which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [300, 400, width, height])
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 400
        self.speed = 1
    #End Procedure
    def update(self):
        if self.rect.x > 630:
            self.rect.x = 630
        elif self.rect.x < 0:
            self.rect.x = 0
        #endif

    def moveRight(self, speed):
        self.rect.x += speed
    #End Procedure
        
    def moveLeft(self, speed):
        self.rect.x -= speed
    #End Procedure
#End Class
#Define class for bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, speed):
        #Call the sprite constructor
        super().__init__()
        self.image = pygame.Surface([2,2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.remove()


        
# ------game over screen function
def game_over(score):
    done = False
    clock = pygame.time.Clock()
    while not done:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_ESCAPE: # - if the escape key pressed
                    pygame.quit()
            #End If
        #Next event
        screen.fill (BLACK)
        font = pygame.font.Font(None, 74)
        text1 = font.render('GAME OVER', 1, WHITE)
        text2 = font.render('SCORE:'+str(score), 1, WHITE)
        screen.blit(text1, (180,100))
        screen.blit(text2, (180,300))
        pygame.display.flip()
        clock.tick(60)

def game():
    done = False
    # Create a list of the snow blocks
    invader_group = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    bullet_group = pygame.sprite.Group()
    # Create a list of all sprites
    all_sprites_group = pygame.sprite.Group()
    score = 0
    # -- Manages how fast screen refreshes
    clock = pygame.time.Clock()     
    # Create the snowflakes
    number_of_invaders = 50 # we are creating 50 snowflakes
    for x in range (number_of_invaders):
        my_invader = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
        invader_group.add(my_invader) # adds the new snowflake to the group of snowflakes
        all_sprites_group.add(my_invader) # adds it to the group of all Sprites
    #Next

    player = Player(YELLOW, 10, 10)
    player_group.add(player)
    all_sprites_group.add(player)
    ### -- Game Loop
    while not done:
        # -- User input and controls
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN: # - a key is down
                if event.key == pygame.K_ESCAPE: # - if the escape key pressed
                    done = True
            #End If
        #Next event

        #moving the player when the user presses a key
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                bullet = Bullet(RED, 5)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet.rect.x = (player.rect.x) + 4
                bullet.rect.y = 400
        if keys[pygame.K_a]:
            player.moveLeft(3)
        if keys[pygame.K_d]:
            player.moveRight(3)
            
    
        # -- Game logic goes after this comment
        all_sprites_group.update()
        player_hit_group = pygame.sprite.groupcollide(player_group,invader_group, True, True)
        if len(player_group) == 0:
            game_over(score)
        if pygame.sprite.groupcollide(bullet_group, invader_group, True, True):
            score += 100

        # -- Screen background is BLACK
        screen.fill (BLACK)
        # -- Draw here
        all_sprites_group.draw(screen)
        # -- Display Score
        font = pygame.font.Font(None, 34)
        text = font.render('Score:'+str(score), 1, WHITE)
        screen.blit(text, (500,10))
        # -- flip display to reveal new position of objects
        pygame.display.flip()
        # - The clock ticks over
        clock.tick(60)
        #End While - End of game loop
    
    #End Function
game()
pygame.quit()
