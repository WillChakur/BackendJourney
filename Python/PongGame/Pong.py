import pygame

pygame.init()
#First we are gone initialize our variables

#Size of the window
WIDTH, HEIGHT = 900, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")


# Object to track time
CLOCK = pygame.time.Clock()
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100

class Striker: 
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        
        # object that holds the rectangle coordinates
        self.playerRect = pygame.Rect(posx, posy, width, height)
         
    def display(self):
        #Here we construct the rectangle figure that will appear on the screen
        self.player = pygame.draw.rect(SCREEN, self.color, self.playerRect)
    
    def update(self, yFac):
        #yFac = -1 upwards 
        #yFac = 1 downwards
        self.posy = self.posy + self.speed*yFac
        
        #Here we are going to check if the rect is going to go off the screen
        
        # top edge if of the top boundarie of the screen
        if self.posy <= 0:
            self.posy = 0
            
        # is off the bottom boundarie of the screen    
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        


        
def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        
        pygame.display.flip()

    pygame.quit()
        
if __name__ == "__main__":
    main()