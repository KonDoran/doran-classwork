import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
 
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
    def __init__(self,color , width, height, x, y, health, score, money, gamekeys):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.health = health
        self.score = score
        self.money = money
        self.gamekeys = gamekeys
        self.rect.x = x
        self.rect.y = y
        
    #end procedure
    def gethealth(self):
        return self.health
    #endprocedure

    def sethealth(self, newhealth):
        self.health = newhealth
    #endfunction

    def getscore(self):
        return self.score
    #endprocedure

    def setscore(self, score):
        self.score = score
    #endfunction

    def getkeys(self):
        return self.gamekeys
    #endprocedure

    def setkeys(self, keys):
        self.gamekeys = keys
    #endfunction

    def getmoney(self):
        return self.money
    #endprocedure

    def setmoney(self, money):
        self.money = money
    #endfunction

    def changespeed(self, x, y):
        self.speed_x += x
        self.speed_y += y
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.changespeed(-5,0)
            if keys[pygame.K_SPACE]:
                bullet = Bullet(RED, -5,0)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet.rect.x = (player.rect.x) + 4
        if keys[pygame.K_d]:
            self.changespeed(5,0)
            if keys[pygame.K_SPACE]:
                bullet = Bullet(RED, 5,0)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet.rect.x = (player.rect.x) + 4
        if keys[pygame.K_w]:
            self.changespeed(0,-5)
            if keys[pygame.K_SPACE]:
                bullet = Bullet(RED,0, -5)
                bullet_group.add(bullet)
                all_sprites_group.add(bullet)
                bullet.rect.x = (player.rect.x) + 4
        if keys[pygame.K_s]:
            self.changespeed(0,5)
            if keys[pygame.K_SPACE]:
                    bullet = Bullet(RED, 0,5)
                    bullet_group.add(bullet)
                    all_sprites_group.add(bullet)
                    bullet.rect.x = (player.rect.x) + 4
        #end if
        self.move(self.speed_x,self.speed_y)
        self.speed_x = 0
        self.speed_y = 0
    #end procedure\
    
    def move(self, speedx, speedy):
        #move along x
        self.rect.x += self.speed_x

        wallcollision = pygame.sprite.spritecollide(self,wall_group, False)
        for wall in wallcollision:
            if self.speed_x > 0:
                self.rect.right = wall.rect.left
            else:
                self.rect.left = wall.rect.right    
    
    
    
        #move the player up and down the screen
        self.rect.y += self.speed_y
        #check for collision
        wallcollision = pygame.sprite.spritecollide(self, wall_group, False) 
        for wall in wallcollision:
            #if there is a collision while moving up then set the speed to 0
            if self.speed_y > 0: 
                #i
                self.rect.bottom = wall.rect.top
            else:
                self.rect.top = wall.rect.bottom
    #end procedure
    
             
#end class

#class Sword(pygame.sprite.Sprite):
 #   def __init__(self, color, width, height):
 #       super().__init__()
 #       self.image = pygame.Surface([width,height])
 #       self.image.fill(color)
 #       self.rect = self.image.get_rect()
 #       self.rect.x = player.rect.x
 #       self.rect.y = player.rect.y
 #   #end procedure

#    def update(self):
 #       self.rect.x = player.rect.x
 #       self.rect.y = player.rect.y

#Define class for bullet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, speedx, speedy):
        #Call the sprite constructor
        super().__init__()
        self.image = pygame.Surface([6,4])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.speedx = speedx
        self.speedy = speedy
        self.rect.y = player.rect.y
        self.rect.x = player.rect.x 



    def update(self):
        self.rect.y += self.speedy
        if self.rect.y < 0 or self.rect.y > 1000:
            self.remove()
        self.rect.x += self.speedx
        if self.rect.x < 0 or self.rect.x > 1000:
            self.remove()

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, posx, posy):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.positionx = posx
        self.positiony = posy
    #end procedure
    def update(self):
        pass
    #end procedure

    def getpos(self):
        return [self.positionx, self.positiony]

class InnerWall(Wall):

        #wallhits = durability
    pass
    #endprocedure
    def update(self):
        pass
        

class Enemy(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y, health):
        #call sprite constructor
        super().__init__()
        #create a sprite
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        #set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = health
    #end procedure
    def update(self):
        pass
    #end procedure

    def gethealth(self):
        return self.health
    #endprocedure

    def sethealth(self, newhealth):
        self.health = newhealth
    #endfunction


level1 = [
   [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
   
    ]


            

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
outsidewall_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
innerwall_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
#Create an instance of player

for enemies in range(0,3):
    xpos = random.randint(1,24)
    ypos = random.randint(1,24)
    if level1[xpos][ypos] == 0:
        level1[xpos][ypos] = 4

for j in range(len(level1)):
    for i in range(len(level1[j])):
        print(i,j)
        char = level1[j][i]
        if char == 1:
            outsidewall = Wall(RED,40,40,i*40, j*40, i, j)
            all_sprites_group.add(outsidewall)
            wall_group.add(outsidewall)
            outsidewall_group.add(outsidewall)
        if char == 2:
            innerwall = InnerWall(RED,40,40,i*40, j*40, i, j)
            all_sprites_group.add(innerwall)
            wall_group.add(innerwall)
            innerwall_group.add(innerwall)
        if char == 3:
            player = Player(WHITE, 40, 40,i*40,j*40,100,0,0,0)
            all_sprites_group.add(player)
            player_group.add(player)
        if char == 4:
            enemy = Enemy(YELLOW,40,40, i*40, j*40, 40)
            all_sprites_group.add(enemy)

#sword = Sword(YELLOW,80,80)
#all_sprites_group.add(sword)
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
    
    
    all_sprites_group.update()
    
    # --- Screen-clearing code goes here


    # background image.
    screen.fill(BLACK)
    # --- Drawing code should go here
    all_sprites_group.draw(screen)
    
    font = pygame.font.Font(None, 24)
    health = font.render('HEALTH:'+str(player.gethealth()), 1, WHITE)
    score = font.render('SCORE:'+str(player.getscore()), 1, WHITE)
    money = font.render('MONEY:'+str(player.getmoney()), 1, WHITE)
    keys = font.render('KEYS:'+str(player.getkeys()), 1, WHITE)
    screen.blit(health, (1050,450))
    screen.blit(score, (1050,500))
    screen.blit(money, (1050,550))
    screen.blit(keys, (1050,600))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()