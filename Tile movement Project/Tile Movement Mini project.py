import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1000, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tile Movement Game")

# Create a Player Class

class Player(pygame.sprite.Sprite):
    #define the constructor for the player
    def __init__(self,color , width, height):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [500, 500, width, height])
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        
    #end procedure
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.moveLeft(20)
        if keys[pygame.K_d]:
            self.moveRight(20)
        if keys[pygame.K_w]:
            self.moveForward(20)
        if keys[pygame.K_s]:
            self.MoveBackward(20)
        #end if
    #end procedure
    def moveLeft(self, speed):
        #move to the left
        self.rect.x -= speed
    #end procedure
    def moveRight(self, speed):
        #move to the right
        self.rect.x += speed
    #end procedure
    def moveForward(self, speed):
        #move up the screen
        self.rect.y -= speed
    #end procedure
    def MoveBackward(self, speed):
        #move down the screen
        self.rect.y += speed
    #end procedure
             
#end class

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([40,40])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [x ,y ,width, height])
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #end procedure
    def update(self):
        pass
    #end procedure

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
outsidewall_group = pygame.sprite.Group()
#Create an instance of player
player = Player(BLACK, 25, 25)
all_sprites_group.add(player)
for i in range(0,25):
    for j in range(0,24,24):
        outsidewall = Wall(RED,40,40,i*40, j*40)
        all_sprites_group.add(outsidewall)
        outsidewall_group.add(outsidewall)
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    all_sprites_group.update()
    # --- Screen-clearing code goes here


    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()