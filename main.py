import pygame, random

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screenWidth = 800
screenHeight = 600

itcolor = black
runcolor = white
player1It = False
filler = random.randint(0, 1)%2
if filler == 1:
    player1Color = itcolor
    player2Color = runcolor
    player1It = True
else:
    player1Color = itcolor
    player2Color = runcolor
    player1It = False

# speed = int(input(print("input speed: ")))
speed = 6

class PlayerOne(pygame.sprite.Sprite):
    
    def __init__(self, color, isIt = False):
        super().__init__()
        
        width = 32
        height = 32
        self.image = pygame.Surface([width, height])
        
        if (isIt):
            self.image = pygame.image.load('Player1It.png')
        else:
            self.image = pygame.image.load('Player1NotIt.png')
        
        self.rect = self.image.get_rect()
        
        self.changeX = 0
        self.changeY = 0
        
        self.level = None
        
    def update(self):
        
        # self.calcGrav()
        
        self.rect.x += self.changeX
        blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in blockHitList:
            if self.changeX > 0:
                self.rect.right = block.rect.left
            elif self.changeX < 0:
                self.rect.left = block.rect.right
                
            self.changeX = 0
        
        self.rect.y += self.changeY
        blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in blockHitList:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                self.rect.top = block.rect.bottom
            
            self.changeY = 0
    
    # def calcGrav(self):
    #     if self.changeY == 0:
    #         self.changeY = 1
    #     else:
    #         self.changeY += 0.35
    
    #     if self.rect.y >= screenHeight - self.rect.height and self.changeY >= 0:
    #         self.changeY = 0
    #         self.rect.y = screenHeight - self.rect.height
        
    def goUp(self):
        # self.rect.y += 2
        # platformHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        # self.rect.y -= 2
        
        # if len(platformHitList) > 0 or self.rect.bottom >= screenHeight:
        #     self.changeY -= 10
        self.changeY -= speed
    
    def goDown(self):
        self.changeY += speed
    
    def goLeft(self):
        self.changeX -= speed
    
    def goRight(self):
        self.changeX += speed
    
    def stopHorizontal(self):
        self.changeX = 0
    
    def stopVertical(self):
        self.changeY = 0
        
    # def stop(self):
    #     self.changeY = 0
    #     self.changeX = 0

class PlayerTwo(pygame.sprite.Sprite):
    
    def __init__(self, color, isIt = False):
        super().__init__()
        
        width = 32
        height = 32
        self.image = pygame.Surface([width, height])
        
        if (isIt):
            self.image = pygame.image.load('Player2It.png')
        else:
            self.image = pygame.image.load('Player2NotIt.png')
        
        self.rect = self.image.get_rect()
        
        self.changeX = 0
        self.changeY = 0
        
        self.level = None
        
    def update(self):
        
        # self.calcGrav()
        
        self.rect.x += self.changeX
        blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in blockHitList:
            if self.changeX > 0:
                self.rect.right = block.rect.left
            elif self.changeX < 0:
                self.rect.left = block.rect.right
                
            self.changeX = 0
        
        self.rect.y += self.changeY
        blockHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        for block in blockHitList:
            if self.changeY > 0:
                self.rect.bottom = block.rect.top
            elif self.changeY < 0:
                self.rect.top = block.rect.bottom
            
            self.changeY = 0
    
    # def calcGrav(self):
    #     if self.changeY == 0:
    #         self.changeY = 1
    #     else:
    #         self.changeY += 0.35
    
    #     if self.rect.y >= screenHeight - self.rect.height and self.changeY >= 0:
    #         self.changeY = 0
    #         self.rect.y = screenHeight - self.rect.height
        
    def goUp(self):
        # self.rect.y += 2
        # platformHitList = pygame.sprite.spritecollide(self, self.level.platformList, False)
        # self.rect.y -= 2
        
        # if len(platformHitList) > 0 or self.rect.bottom >= screenHeight:
        #     self.changeY -= 10
        self.changeY -= speed
    
    def goDown(self):
        self.changeY += speed
    
    def goLeft(self):
        self.changeX -= speed
    
    def goRight(self):
        self.changeX += speed
    
    def stopHorizontal(self):
        self.changeX = 0
    
    def stopVertical(self):
        self.changeY = 0
        
    # def stop(self):
    #     self.changeY = 0
    #     self.changeX = 0
        
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(green)
        
        self.rect = self.image.get_rect()

class Level(object):
    
    def __init__(self, player):
        self.platformList = pygame.sprite.Group()
        self.enemyList = pygame.sprite.Group()
        self.player = player
        
        self.background = None
        
    def update(self):
        self.platformList.update()
        self.enemyList.update()
        
    def draw(self, screen):
        screen.fill(blue)
        
        self.platformList.draw(screen)
        self.enemyList.draw(screen)
        
class levelOne(Level):
    
    def __init__(self, player1, player2):
        
        Level.__init__(self, player1)
        Level.__init__(self, player2)
        
        level = []
        
        for i in range(random.randint(2, 6)):
            newBlock = [40, 40, random.randint(0, 76) * 10, random.randint(0, 56) * 10]
            level.append(newBlock)
        
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.player = self.player
            self.platformList.add(block)

def main():
    global player1It
    global player1Color
    global player2Color
    pygame.init()
    
    size = [screenWidth, screenHeight]
    screen = pygame.display.set_mode(size)
    screen.set_alpha(None)
    
    pygame.display.set_caption("Tag")
    
    player1 = PlayerOne(player1Color, isIt = player1It)
    player2 = PlayerTwo(player2Color, isIt = not player1It)
    
    levelList = []
    levelList.append(levelOne(player1, player2))
    
    currentLevelNumber = 0
    currentLevel = levelList[currentLevelNumber]
    
    activeSpriteList = pygame.sprite.Group()
    player1.level = currentLevel
    player2.level = currentLevel
    
    player1.rect.x = 80
    player1.rect.y = screenHeight - player1.rect.height
    activeSpriteList.add(player1)
    
    player2.rect.x = 200
    player2.rect.y = screenWidth - player2.rect.width
    activeSpriteList.add(player2)
    
    done = False
    collisionOccurred = False
    
    clock = pygame.time.Clock()
    pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])
    
    while not done:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player1.goLeft()
                if event.key == pygame.K_RIGHT:
                    player1.goRight()
                if event.key == pygame.K_UP:
                    player1.goUp()
                if event.key == pygame.K_DOWN:
                    player1.goDown()
                    
                if event.key == pygame.K_a:
                    player2.goLeft()
                if event.key == pygame.K_d:
                    player2.goRight()
                if event.key == pygame.K_w:
                    player2.goUp()
                if event.key == pygame.K_s:
                    player2.goDown()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player1.stopHorizontal()
                if event.key == pygame.K_RIGHT:  
                    player1.stopHorizontal()
                if event.key == pygame.K_UP:
                    player1.stopVertical()
                if event.key == pygame.K_DOWN:
                    player1.stopVertical()
                
                if event.key == pygame.K_a:
                    player2.stopHorizontal()
                if event.key == pygame.K_d:  
                    player2.stopHorizontal()
                if event.key == pygame.K_w:
                    player2.stopVertical()
                if event.key == pygame.K_s:
                    player2.stopVertical()
        
        pygame.event.pump()
        
        # player1.update()
        # player2.update()
        activeSpriteList.update()
        currentLevel.update()
        
        if player1.rect.right > screenWidth:
            player1.rect.right = screenWidth
        if player1.rect.left < 0:
            player1.rect.left = 0
        if player1.rect.bottom > screenHeight:
            player1.rect.bottom = screenHeight
        if player1.rect.top < 0:
            player1.rect.top = 0
            
        if player2.rect.right > screenWidth:
            player2.rect.right = screenWidth
        if player2.rect.left < 0:
            player2.rect.left = 0
        if player2.rect.bottom > screenHeight:
            player2.rect.bottom = screenHeight
        if player2.rect.top < 0:
            player2.rect.top = 0
        
        # other drawing code below
        currentLevel.draw(screen)
        activeSpriteList.draw(screen)
        
        if player1.rect.colliderect(player2.rect) and not collisionOccurred:
            if player1It:
                player1It = False
                player1.image = pygame.image.load('Player1NotIt.png')
                player2.image = pygame.image.load('Player2It.png')
                # player1.image.fill(runcolor)
                # player2.image.fill(itcolor)
            else:
                player1It = True
                player1.image = pygame.image.load('Player1It.png')
                player2.image = pygame.image.load('Player2NotIt.png')
                # player1.image.fill(itcolor)
                # player2.image.fill(runcolor)
            
            collisionOccurred = True
        elif not player1.rect.colliderect(player2.rect):
            collisionOccurred = False
        
        # drawing code shd be above
        
        clock.tick(60)
        pygame.display.flip()
        print(clock)
        
    pygame.quit()

        
if __name__ == "__main__":
    main()        