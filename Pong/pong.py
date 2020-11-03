# Import the pygame library and initialise the game engine
import pygame
from random import randint
pygame.init()
 
# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (180,180,180)
clock = pygame.time.Clock()
# Open a new window
size = (1280,720)
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")





class Paddle(pygame.sprite.Sprite):
    #This class represents a paddle. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the paddle, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.speed=5
 
        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveUp(self, pixels):
        self.rect.y -= pixels
        #Check that you are not going too far (off the screen)
        if self.rect.y < 0:
          self.rect.y = 0
          
    def moveDown(self, pixels):
        self.rect.y += pixels
    #Check that you are not going too far (off the screen)
        if self.rect.y > 620:
          self.rect.y = 620
          
    def automove(self, bally):
        if self.rect.y>bally:
            self.rect.y-=self.speed
        if self.rect.y<bally:
            self.rect.y+=self.speed
        if self.rect.y < 0:
          self.rect.y = 0



class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)




def text_objects(text,font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

def button_1(msg1,xb1,yb1,wb1,hb1,icb1,acb1,action1=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if xb1+wb1 >mouse[0] > xb1 and yb1+hb1 > mouse[1] > yb1:
        pygame.draw.rect(screen, icb1,(xb1,yb1,wb1,hb1),5)
        if click[0] == 1 and action1 !=None:
            if action1 == "1":
                playeronegameloop()
            elif action1 == "2":
                playertwogameloop()
            elif action1 == "O":
                optionsloop()
            elif action1 == "Q":
                    pygame.quit()
    else:
        pygame.draw.rect(screen, acb1,(xb1,yb1,wb1,hb1),5)
        
    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg1, smallText)
    textRect.center = ( (xb1+(wb1/2)), (yb1+(hb1/2)) )
    screen.blit(textSurf, textRect)


def button_2(msg2,xb2,yb2,wb2,hb2,icb2,acb2,action2=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if xb2+wb2 >mouse[0] > xb2 and yb2+hb2 > mouse[1] > yb2:
        pygame.draw.rect(screen, icb2,(xb2,yb2,wb2,hb2),5)
        if click[0] == 1 and action2 !=None:
            if action2 == "E":
                
            elif action2 == "M":
                
            elif action2 == "H":
                
            elif action2 == "B":
                    game_intro()
    else:
        pygame.draw.rect(screen, acb2,(xb2,yb2,wb2,hb2),5)
        
    smallText = pygame.font.Font("freesansbold.ttf",30)
    textSurf, textRect = text_objects(msg1, smallText)
    textRect.center = ( (xb2+(wb2/2)), (yb2+(hb2/2)) )
    screen.blit(textSurf, textRect)
    
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
              intro = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: 
                         intro=False
                         
#Drawing the menu screen
        screen.fill(BLACK)
        font = pygame.font.Font('freesansbold.ttf', 84)
        text = font.render(str("PONG"), 1, WHITE)
        text_rect = text.get_rect(center=(screen_width/2, screen_height/6))
        screen.blit(text, text_rect)

        button_1("SINGLEPLAYER",510,250,250,60,WHITE,GREY,"1")
        button_1("MULTIPLAYER",510,330,250,60,WHITE,GREY,"2")
        button_1("OPTIONS",510,410,250,60,WHITE,GREY,"O")
        button_1("QUIT",510,490,250,60,WHITE,GREY,"Q")
            
        pygame.display.flip()
        clock.tick(60)



def optionsloop():
    options = True
    while options:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
              options = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: 
                         options = False
        screen.fill(BLACK)
        button_1("EASY",510,250,250,60,WHITE,GREY,"E")
        button_1("MEDIUM",510,330,250,60,WHITE,GREY,"M")
        button_1("HARD",510,410,250,60,WHITE,GREY,"H")
        button_1("BACK",510,490,250,60,WHITE,GREY,"B")
        pygame.display.flip()
        clock.tick(60)                 

def playertwogameloop():
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
 
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 1250
    paddleB.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 640
    ball.rect.y = 340
 
#This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
 
# Add thepaddles to the list of sprites
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
 
# The clock will be used to control how fast the screen updates

#Initialise player scores
    scoreA = 0
    scoreB = 0
# -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: #Pressing the x Key will quit the game
                         carryOn=False
 
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(pspeed)
        if keys[pygame.K_s]:
            paddleA.moveDown(pspeed)
        if keys[pygame.K_UP]:
            paddleB.moveUp(pspeed)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(pspeed)    
 
    # --- Game logic should go here
        all_sprites_list.update()
 
  #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=1270:
            scoreA+=1
            ball.rect.x = 640
            ball.rect.y = 340
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.rect.x = 640
            ball.rect.y = 340
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>710:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1] 

    #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
          ball.bounce()
    # --- Drawing code should go here
    # First, clear the screen to black. 
        screen.fill(BLACK)
    #Draw the net
        pygame.draw.line(screen, WHITE, [639, 0], [639, 720], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 

    #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (500,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (750,10))
    
    # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # --- Limit to 60 frames per second
        clock.tick(60)

         

def playeronegameloop():
    paddleA = Paddle(WHITE, 10, 100)
    paddleA.rect.x = 20
    paddleA.rect.y = 200
 
    paddleB = Paddle(WHITE, 10, 100)
    paddleB.rect.x = 1250
    paddleB.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 640
    ball.rect.y = 340
    
    
 
#This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()
 
# Add thepaddles to the list of sprites
    all_sprites_list.add(paddleA)
    all_sprites_list.add(paddleB)
    all_sprites_list.add(ball)

# The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
 
# The clock will be used to control how fast the screen updates

#Initialise player scores
    scoreA = 0
    scoreB = 0
# -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
              carryOn = False # Flag that we are done so we exit this loop
            elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE: #Pressing the x Key will quit the game
                         carryOn=False
 
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(7)
        if keys[pygame.K_s]:
            paddleA.moveDown(7)
        if keys[pygame.K_UP]:
            paddleB.moveUp(7)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(7)    
 
    # --- Game logic should go here
        bally=ball.rect.y
        paddleB.automove(bally)
        all_sprites_list.update()
 
  #Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x>=1270:
            scoreA+=1
            ball.rect.x = 640
            ball.rect.y = 340
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x<=0:
            scoreB+=1
            ball.rect.x = 640
            ball.rect.y = 340
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y>710:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y<0:
            ball.velocity[1] = -ball.velocity[1] 

    #Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
          ball.bounce()
    # --- Drawing code should go here
    # First, clear the screen to black. 
        screen.fill(BLACK)
    #Draw the net
        pygame.draw.line(screen, WHITE, [639, 0], [639, 720], 5)
    
    #Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen) 

    #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (500,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (750,10))
    
    # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
    # --- Limit to 60 frames per second
        clock.tick(60)

 
#Once we have exited the main program loop we can stop the game engine:
game_intro()
pygame.quit()
