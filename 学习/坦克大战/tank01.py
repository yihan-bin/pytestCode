import pygame


SCREEN_WIDTH=700
SCREEN_HIGH=500
BG_COLOUR=pygame.Color(0,0,0)

Text_Color=pygame.Color(225,0,0)
class MianGame():
    #my_Tank = Tank(350, 250)
    def __init__(self):
        my_Tank = None
        pygame.display.init()
        pygame.display.set_caption('坦克大战1.0')
        MianGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HIGH])
        MianGame.my_Tank = Tank(350, 250)
    def startGame(self):
        # pygame.display.init()
        # pygame.display.set_caption('坦克大战1.0')
        # MianGame.window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HIGH])
        # MianGame.my_Tank = Tank(350, 250)

        while True:
            MianGame.window.fill(BG_COLOUR)
            self.getEvent()
            text_Surface=self.getTextSurface('敌方坦克剩余数量%d'%6)
            MianGame.window.blit(text_Surface,(100,100))
            MianGame.my_Tank.displayTank()
            pygame.display.update()

    def endGame(self):
        print('欢迎再次使用！！')
        exit()
    def getEvent(self):
        eventList=pygame.event.get()
        for event in eventList:
            if event.type==pygame.QUIT:
                self.endGame()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.my_Tank.direction = 'L'
                    self.my_Tank.move()

                    print('按下左键,坦克向左移动')
                if event.key==pygame.K_RIGHT:
                    MianGame.my_Tank.direction = 'R'
                    MianGame.my_Tank.move()
                    print('向右运动,坦克向右移动')
                if event.key==pygame.K_UP:
                    self.my_Tank.direction = 'U'
                    self.my_Tank.move()
                    print('向上运动,坦克向上运动')

                if event.key==pygame.K_DOWN:
                    print('向下运动,坦克向下运动')
                    MianGame.my_Tank.direction = 'D'
                    MianGame.my_Tank.move()
    def getTextSurface(self,num):
        pygame.font.init()
       # print(pygame.get_fonts())
        font=pygame.font.SysFont('kaiti',18)
        textSurface= font.render(num,True,Text_Color)
        return textSurface

class Tank():
    def __init__(self,left,top):
        self.images={
            'U':pygame.image.load('image/EU.gif'),
            'D': pygame.image.load('image/ED.gif'),
            'L': pygame.image.load('image/EL.gif'),
            'R':pygame.image.load('image/ER.gif'),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 10
    def move(self):
        if self.direction == 'L':
            self.rect.left -=self.speed
            return
        elif self.direction == 'R':
            self.rect.left +=self.speed
            return
        elif self.direction == 'U':
            self.rect.top -= self.speed
            return
        elif self.direction == 'D':
            self.rect.top +=self.speed
            return

    def shot(self):
        pass
    def displayTank(self):
        self.image=self.images[self.direction]
        MianGame.window.blit(self.image,self.rect)








if __name__=='__main__':
   mainGame= MianGame()
   mainGame.startGame()
