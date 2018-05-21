import pygame
import imageio
import math
import sys
import os

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWSIZE = [WINDOWWIDTH, WINDOWHEIGHT]

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
AQUAMARINE = (112, 219, 147)
BRASS = (181, 166, 66)
CADET_BLUE = (95, 159, 159)
COPPER = (184, 115, 51)
DARK_GREEN = (47, 79, 47)
DARK_ORCHID = (153, 50, 205)
DARK_PURPLE = (135, 31, 120)
DARK_WOOD = (133, 94, 66)
DIM_GREY = (84, 84, 84)
FIREBRICK = (142, 35, 35)
FLESH = (245, 204, 176)
FOREST_GREEN = (35, 142, 35)
GOLD = (205, 127, 50)
GOLDENROD = (219, 219, 112)
GREY = (192, 192, 192)
GREEN_COPPER = (82, 127, 118)
KHAKI = (159, 159, 95)
MAROON = (142, 35, 107)
MIDNIGHT_BLUE = (47, 47, 79)
NEW_TAN = (235, 199, 158)
OLD_GOLD = (207, 181, 59)
ORANGE = (255, 127, 0)
ORCHID = (219, 112, 219)
QUARTZ = (217, 217, 243)
RICH_BLUE = (89, 89, 171)
SCARLET = (140, 23, 23)
SEA_GREEN = (35, 142, 104)
SEMI_SWEET_CHOCOLATE = (107, 66, 38)
SIENNA = (142, 107, 35)
SLATE_BLUE = (0, 127, 255)
SPRING_GREEN = (0, 255, 127)
STEEL_BLUE = (35, 107, 142)
SUMMER_SKY = (56, 176, 222)
TAN = (219, 147, 112)
TURQUOISE = (173, 234, 234)
VERY_DARK_BROWN = (92, 64, 51)
VIOLET = (79, 47, 79)
VIOLET_RED = (204, 50, 153)
YELLOW_GREEN = (153, 204, 50)
COLORS = [WHITE, RED, GREEN, BLUE, MAGENTA, CYAN, YELLOW, BLACK, AQUAMARINE, BRASS, CADET_BLUE, COPPER, DARK_GREEN,
          DARK_ORCHID, DARK_PURPLE, DARK_WOOD, DIM_GREY, FIREBRICK, FLESH, FOREST_GREEN, GOLD, GOLDENROD, GREY,
          GREEN_COPPER, KHAKI, MAROON, MIDNIGHT_BLUE, NEW_TAN, OLD_GOLD, ORANGE, ORCHID, QUARTZ, RICH_BLUE, SCARLET,
          SEA_GREEN, SEMI_SWEET_CHOCOLATE, SIENNA, SLATE_BLUE, SPRING_GREEN, STEEL_BLUE, SUMMER_SKY, TAN, TURQUOISE,
          VERY_DARK_BROWN, VIOLET, VIOLET_RED, YELLOW_GREEN]



# Classes Go Here
class Wheel(pygame.sprite.Sprite):

    def __init__(self,radius):

        super().__init__()

        self.image = pygame.Surface([radius,radius])
        self.image.fill(BLACK)
        pygame.draw.circle(self.image,WHITE,[radius//2,radius//2],radius//2,8)
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOWWIDTH//4
        self.rect.bottom = 2/3 * WINDOWHEIGHT

class RotatingCircle(pygame.sprite.Sprite):

        def __init__(self,A,B,C,D,size,color):

            super().__init__()

            self.A = A
            self.B = B
            self.C = C
            self.D = D
            self.color = color
            if size == 'Big':
                self.displacement = [WINDOWWIDTH // 8, WINDOWHEIGHT // 2 + self.D * 10-self.A*10]
            if size == 'Small':
                self.displacement = [WINDOWWIDTH * 5 // 8, WINDOWHEIGHT // 2 + self.D*10 - self.A*10]

            self.image = pygame.Surface([10,10])
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.time = 0

        def update(self):
            self.time += .001
            self.y = (self.A * math.sin(self.B * (self.time - self.C)) + self.D) * -10 + self.displacement[1]
            self.x = (self.A * math.cos(self.B * (self.time - self.C)) + self.D) * 10 + self.displacement[0]
            self.rect.centery = self.y
            self.rect.centerx = self.x
            pygame.draw.circle(DISPLAYSURF,WHITE,[int(self.displacement[0] + 10 *self.D),int(self.displacement[1] - 10 * self.D)],int(self.A*10),10)
            pygame.draw.line(DISPLAYSURF,self.color,[0,self.y],[WINDOWWIDTH,self.y])

# Main Loop Code Go Here

def main():
    global COLORS, WINDOWSIZE, DISPLAYSURF, FPSCLOCK, FONT
    #[As1,Bs1,Cs1,Ds1] = input("Input the first set of data, seperated by spaces \n").split()
    #[As2, Bs2, Cs2, Ds2] = input("Input the second set of data, seperated by spaces \n").split()
    [As1, Bs1, Cs1, Ds1] = [10,11,12,13]
    [As2, Bs2, Cs2, Ds2] = [2,6,7,12]
    pygame.init()
    FONT = pygame.font.SysFont('Georgia', 25, True, False)
    DISPLAYSURF = pygame.display.set_mode(WINDOWSIZE)
    FPSCLOCK = pygame.time.Clock()

    # Initializations go here

    filelist = [f for f in os.listdir('GIFs') if f.endswith(".bak")]
    for f in filelist:
        os.remove(os.path.join('GIFs', f))

    dot_group = pygame.sprite.Group()
    #formulas should all be given in the positive sin form
    #dot1 = RotatingCircle(12,math.pi/2,1,12,'Big')
    #dot2 = RotatingCircle(3,2*math.pi,2.16,3,'Small')
    dot1 = RotatingCircle(float(As1),float(Bs1),float(Cs1),float(Ds1), 'Big',GREEN)
    dot2 = RotatingCircle(float(As2),float(Bs2),float(Cs2),float(Ds2),'Small',ORANGE)
    dot_group.add(dot1)
    dot_group.add(dot2)
    tick = 0
    files_names = []
    printed = False
    while True:
        pause = False
        for event in pygame.event.get():
            # Controls go here
            if event.type == pygame.KEYDOWN:
                pass
            if event.type == pygame.KEYUP:
                pass
            if event.type == pygame.QUIT:
                quit()
        DISPLAYSURF.fill(BLACK)
        pygame.draw.line(DISPLAYSURF,WHITE,[0,WINDOWHEIGHT//2],[WINDOWWIDTH,WINDOWHEIGHT//2])
        # Update positions
        dot_group.update()

        # Drawing new objects go here
        time_text = FONT.render(str(round(dot1.time, 4)), True, RED)
        DISPLAYSURF.blit(time_text, [300, 62])

        dot_group.draw(DISPLAYSURF)
        if abs(dot1.y-dot2.y) < 1:
            pause = True
            hit_text = FONT.render('Hit', True, RED)
            DISPLAYSURF.blit(hit_text, [300, 12])

        FPSCLOCK.tick()
        pygame.display.flip()
        if pause:
            pygame.time.delay(500)
        if dot1.time < 10:
            tick+=1
            files_names.append('GIFs//'+'gif'+str(tick)+'.png')
            pygame.image.save(DISPLAYSURF,'GIFs//'+'gif'+str(tick)+'.png')
        elif printed:
            printed=True
            finish(files_names)
            quit()



# Additional Modules go here
def finish(filenames):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('GIFs//final.gif', images)

def quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()

