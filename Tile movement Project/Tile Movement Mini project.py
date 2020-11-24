import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1200, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Tile Movement Game")

# Create a Player Class

class Player(pygame.sprite.Sprite):
    #define the constructor for the player
    speed_x = 0
    speed_y = 0
    def __init__(self,color , width, height, x, y):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        pygame.draw.rect(self.image, color, [500, 500, width, height])
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    #end procedure
    def changespeed(self, x, y):
        self.speed_x += x
        self.speed_y += y
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.changespeed(-5,0)
        if keys[pygame.K_d]:
            self.changespeed(5,0)
        if keys[pygame.K_w]:
            self.changespeed(0,-5)
        if keys[pygame.K_s]:
            self.changespeed(0,5)
        #end if
        self.move(self.speed_x,self.speed_y)
        self.speed_x = 0
        self.speed_y = 0
    #end procedure
    def move(self, speedx, speedy):
        #move along x
        self.rect.x += self.speed_x

        wallcollision = pygame.sprite.spritecollide(self,wall_group, False)
        for wall in wallcollision:
            if self.speed_x > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right    
    
    
    
        #move up the screen
        self.rect.y += self.speed_y
        wallcollision = pygame.sprite.spritecollide(self, wall_group, False)
        for wall in wallcollision:
            if self.speed_y > 0:
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
    #end procedure
    
             
#end class

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
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

class InnerWall(Wall):

        #wallhits = durability
    pass
    #endprocedure
    def update(self):
        pass
        

level1 = [
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
   
    ]


            

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
outsidewall_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
innerwall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
#Create an instance of player


for j in range(len(level1)):
    for i in range(len(level1[j])):
        print(i,j)
        char = level1[j][i]
        if char == 1:
            outsidewall = Wall(RED,40,40,i*40, j*40)
            all_sprites_group.add(outsidewall)
            wall_group.add(outsidewall)
            outsidewall_group.add(outsidewall)
        if char == 2:
            innerwall = InnerWall(RED,40,40,i*40, j*40)
            all_sprites_group.add(innerwall)
            wall_group.add(innerwall)
            innerwall_group.add(innerwall)
        if char == 3:
            player = Player(BLACK, 40, 40,i*40,j*40)
            all_sprites_group.add(player)
            player_group.add(player)

#for i in range(0,25):
 #   for j in range(0,25):
      #  if (i == 0 or i == 24) or (j==0 or j == 24):
      #      outsidewall = Wall(RED,40,40,i*40, j*40)
      #      all_sprites_group.add(outsidewall)
      #      outsidewall_group.add(outsidewall)
            
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
    wallcollision = pygame.sprite.spritecollide(player, outsidewall_group, False, False)
    
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