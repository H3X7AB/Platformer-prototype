import pygame
import time

# constant
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPRITE_WIDTH = 20
SPRITE_HEIGHT = 20

# pygame window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Platforming prototpye")
clock = pygame.time.Clock()

# variables
moveL = False
moveR = False
moveU = False
moveD = False
collision = False
# jumping variables
jumping = False
jumpgravity = 2
jumps = 0
jumpHeight = 28
jumpvelocity = jumpHeight
# gravity varaibles
fallGravity = 2
fallVelocity = 0.0001



# sprite class
class user(pygame.sprite.Sprite):
    def __init__(self, image, width, height, startx, starty):
        super().__init__()
        self.__width = width
        self.__height = height
        self.__image = pygame.image.load(image).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (width, height))
        self.rect = self.__image.get_rect()
        self.rect.x = startx
        self.rect.y = starty

    def draw(self):
        screen.blit(self.__image, (self.rect.x, self.rect.y))
        

    def move(self):
        if moveL and player.rect.x >= -6:
            player.rect.x -=3
        if moveR and player.rect.x <= SCREEN_WIDTH-player.rect.width:
            player.rect.x +=3
        if moveD and player.rect.y <= SCREEN_HEIGHT-player.rect.height:
            player.rect.y +=3
    def jump(self, jumpvelocity,jumping,jumpHeight,jumpgravity):
        player.rect.y -= jumpvelocity
        if jumpvelocity < -jumpHeight+jumpgravity+2:
            jumping=False
            return jumping

            
        
# sprite player and position
player = user("goose.png",100,100,400,0)


# main loop
running = True
while running:
    screen.fill((135,206,235))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # key board movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveL = True
                
            elif event.key == pygame.K_RIGHT:
                moveR = True
            
            elif event.key == pygame.K_UP:
                if jumps>0:
                    jumping=True
                    jumps -=1
                    
                
            elif event.key == pygame.K_DOWN:
                if collision==False:
                    moveD = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveL = False
                
            elif event.key == pygame.K_RIGHT:
                moveR = False
            
            elif event.key == pygame.K_UP:
                moveU = False
                
            elif event.key == pygame.K_DOWN:
                moveD = False   

    # movement
    if moveL:
        player.move()
    if moveR:
        player.move()
    if moveD:
        player.move()



    # draw player
    sprite = player.draw()

    # draw platforms
    block=[]
    platform=pygame.draw.rect(screen,(0,0,0),(100,500,400,10))
    platform2=pygame.draw.rect(screen,(0,0,0),(500,450,200,10))
    block.append(platform)
    block.append(platform2)

    # fall off platform
    if player.rect.y>600:
        print("You died")
        time.sleep(1)
        sprite = player.rect.update(400,0,100,100)

    # platform collision
    if player.rect.collidelistall(block):
        collision=True
        fallVelocity = 0.0001
        fallGravity = 1
        jumpvelocity = jumpHeight
        if jumps==1:
            pass
        else:
            jumps=1


    # falling
    if not(player.rect.collidelistall(block)):
        player.rect.y += fallVelocity
        fallVelocity += fallGravity
        



    # jumping 
    if jumps>0:
        if jumping:
            spritejump = player.jump(jumpvelocity,jumping,jumpHeight,jumpgravity)
            jumpvelocity -= jumpgravity
            if player.rect.collidelistall(block):
                jumping=False
            if spritejump==False:
                jumpvelocity=jumpHeight
                jumping = False
            
    pygame.display.update()
    clock.tick(60) # fps

pygame.quit()
