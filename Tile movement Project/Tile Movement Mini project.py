import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PINK = (255,20,147)
PURPLE = (75,0,130)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1200, 1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tile Movement Game")

#Loop until the user clicks the close button.
done = False
    
    # Used to manage how fast the screen updates
clock = pygame.time.Clock()
    






class Game(object):
    def __init__(self):
        self.score = 0
        self.game_over = False
        self.level = 0
        # Create a list of all sprites
        self.all_sprites_group = pygame.sprite.Group()
        self.outsidewall_group = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.innerwall_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.Group()
        self.portal_group = pygame.sprite.Group()
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
                self.directionx = 0
                self.directiony = 5
                
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
                    self.directionx = -5
                    self.directiony = 0
                if keys[pygame.K_d]:
                    self.changespeed(5,0)
                    self.directionx = 5
                    self.directiony = 0      
                if keys[pygame.K_w]:
                    self.changespeed(0,-5)
                    self.directionx = 0
                    self.directiony = -5
                if keys[pygame.K_s]:
                    self.changespeed(0,5)
                    self.directionx = 0
                    self.directiony = 5
                if keys[pygame.K_SPACE]:
                    if len(game.bullet_group) == 0:
                        print("held down")
                        bullet = Bullet(RED, self.directionx, self.directiony)
                        game.bullet_group.add(bullet)
                        game.all_sprites_group.add(bullet)
                        
                #end if
                self.move(self.speed_x,self.speed_y)
                self.speed_x = 0
                self.speed_y = 0
                player_hit_group = pygame.sprite.groupcollide(game.player_group, game.enemy_group, False, False)
                for self in player_hit_group:
                    self.health -= 1
                    if self.health < 1:

                        self.kill()
                

                    



            #end procedure

            def move(self, speedx, speedy):
                #move along x
                self.rect.x += self.speed_x

                wallcollision = pygame.sprite.spritecollide(self,game.wall_group, False)
                for wall in wallcollision:
                    if self.speed_x > 0:
                        self.rect.right = wall.rect.left
                    else:
                        self.rect.left = wall.rect.right    
            
            
            
                #move the player up and down the screen
                self.rect.y += self.speed_y
                #check for collision
                wallcollision = pygame.sprite.spritecollide(self, game.wall_group, False) 
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
        class Key(pygame.sprite.Sprite):
            def __init__(self,color,x,y):
                super().__init__()
                self.image = pygame.Surface([10,10])
                self.image.fill(color)
                self.rect = self.image.get_rect()
                self.rect.y = y
                self.rect.x = x

            def update(self):
                key_hit_group = pygame.sprite.groupcollide(game.key_group, game.player_group, True, False)
                for self in key_hit_group:
                    game.player.gamekeys += 1
                    if  game.player.gamekeys == 3:
                        game.portal = Portal(PURPLE, 23*40, 23*40)
                        game.all_sprites_group.add(game.portal)
                        game.portal_group.add(game.portal)

        class Bullet(pygame.sprite.Sprite):
            def __init__(self, color, speedx, speedy):
                #Call the sprite constructor
                super().__init__()
                self.image = pygame.Surface([6,4])
                self.image.fill(color)
                self.rect = self.image.get_rect()
                self.speedx = speedx
                self.speedy = speedy
                self.rect.y = game.player.rect.y + 18
                self.rect.x = game.player.rect.x  + 18



            def update(self):
                self.rect.y += self.speedy
                if pygame.sprite.groupcollide(game.bullet_group, game.wall_group, True, False) == True:
                    self.remove()
                self.rect.x += self.speedx
                if pygame.sprite.groupcollide(game.bullet_group, game.wall_group, True, False) == True:
                    self.remove()
                
        class Portal(pygame.sprite.Sprite):
            def __init__(self,color,x,y):
                super().__init__()
                self.image = pygame.Surface([40,40])
                self.image.fill(color)
                self.rect = self.image.get_rect()
                self.rect.y = y
                self.rect.x = x
            #end procedure    
            def update(self):
                pass

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
                enemy_hit_group = pygame.sprite.pygame.sprite.groupcollide(game.enemy_group, game.bullet_group, False, True)
                for self in enemy_hit_group:
                    self.health -= 20
                    print(self.health)
                    if self.health < 1:
                        gamekey = Key(PINK, self.rect.x + 18, self.rect.y + 18)
                        game.all_sprites_group.add(gamekey)
                        game.key_group.add(gamekey)
                        self.kill()


            #end procedure

            def gethealth(self):
                return self.health
            #endprocedure

            def sethealth(self, newhealth):
                self.health = newhealth
            #endfunction

        

        self.level1 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0,0,0,0,0,1],
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
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        
            ]

        self.level2 = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,0,0,0,0,0,0,0,0,1],
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
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        
            ]
                    
        self.levels = [self.level1, self.level2]

        #Create an instance of player

        enemies = 0
        while enemies != 3:
            xpos = random.randint(1,23)
            ypos = random.randint(1,23)
            if self.levels[self.level][xpos][ypos] == 0:
                self.levels[self.level][xpos][ypos] = 4
                enemies = enemies +1

        for j in range(len(self.levels[self.level])):
            for i in range(len(self.levels[self.level][j])):
                print(i,j)
                char = self.levels[self.level][j][i]
                if char == 1:
                    self.outsidewall = Wall(RED,40,40,i*40, j*40, i, j)
                    self.all_sprites_group.add(self.outsidewall)
                    self.wall_group.add(self.outsidewall)
                    self.outsidewall_group.add(self.outsidewall)
                if char == 2:
                    self.innerwall = InnerWall(RED,40,40,i*40, j*40, i, j)
                    self.all_sprites_group.add(self.innerwall)
                    self.wall_group.add(self.innerwall)
                    self.innerwall_group.add(self.innerwall)
                if char == 3:
                    self.player = Player(WHITE, 40, 40,i*40,j*40,100,0,0,0)
                    self.all_sprites_group.add(self.player)
                    self.player_group.add(self.player)
                if char == 4:
                    self.enemy = Enemy(YELLOW,40,40, i*40, j*40, 40)
                    self.all_sprites_group.add(self.enemy)
                    self.enemy_group.add(self.enemy)

        #sword = Sword(YELLOW,80,80)
        #all_sprites_group.add(sword)
        #for i in range(0,25):
        #   for j in range(0,25):
            #  if (i == 0 or i == 24) or (j==0 or j == 24):
            #      outsidewall = Wall(RED,40,40,i*40, j*40)
            #      all_sprites_group.add(outsidewall)
            #      outsidewall_group.add(outsidewall)
    def eventprocess(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False            


    def runlogic(self):
        if not self.game_over:
            # Move all the sprites
            self.all_sprites_group.update()
            if len(self.player_group) == 0:
                self.game_over = True
            portal_hit = pygame.sprite.groupcollide(self.portal_group, self.player_group, True, False)
            for self.portal in portal_hit:
                self.level += 1
                print(self.level)


    def display(self, screen):
        # background image.
        screen.fill(BLACK)

        if self.game_over:
            pass
        if not self.game_over:
            font = pygame.font.Font(None, 24)
            health = font.render('HEALTH:'+str(self.player.gethealth()), 1, WHITE)
            score = font.render('SCORE:'+str(self.player.getscore()), 1, WHITE)
            money = font.render('MONEY:'+str(self.player.getmoney()), 1, WHITE)
            keys = font.render('KEYS:'+str(self.player.getkeys()), 1, WHITE)
            screen.blit(health, (1050,450))
            screen.blit(score, (1050,500))
            screen.blit(money, (1050,550))
            screen.blit(keys, (1050,600))
            # --- Drawing code should go here
            self.all_sprites_group.draw(screen)
            #endif
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
    #end procedure


game = Game()
# -------- Main Program Loop -----------
while not done:
        # --- Main event loop
    done = game.eventprocess()
    
        # --- Game logic should go here
    game.runlogic()

        #draw the screen
    game.display(screen)
        
        # --- Limit to 60 frames per second
    clock.tick(60)
    
    # Close the window and quit.
pygame.quit()

