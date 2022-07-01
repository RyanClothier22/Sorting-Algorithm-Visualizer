import pygame
import random

pygame.init()
rects = 300
typeStr = "BUBBLE"
num = 0
done_sorting = True

class Line:
    def __init__(self):
        self.pos = 0
        self.height = 0

    def draw(self):
        pygame.draw.line(SCREEN, RED, (self.pos, 322), (self.pos, self.height), int(WIDTH / rects))

class Graph:
    def __init__(self):
        self.num = 25
        self.arr = []
        self.poss = []
        self.build()
        # self.shuffle()

    def build(self):
        for i in range(1,rects+1):
            line = Line()
            line.pos = (WIDTH / rects) * i -(WIDTH/(2*rects))
            line.height = 322 - (282/rects) * i
            line.index = i
            self.arr.append(line)
            self.poss.append(line.pos)

    def shuffle(self):
        random.shuffle(self.poss)
        for i in range(len(self.arr)):
            self.arr[i].pos = self.poss[i]
    def sort(self,num):
        if num%5 == 0:
            for i in range(len(self.poss) - 1):
                for j in range(len(self.poss) - i - 1):
                    if self.poss[j] > self.poss[j + 1]:
                        self.poss[j], self.poss[j + 1] = self.poss[j + 1], self.poss[j]
                        for i in range(len(self.arr)):
                            self.arr[i].pos = self.poss[i]
                        graph.refresh()
                        pygame.time.delay(5)
        elif num%5 == 1:
            for i in range(len(self.poss) - 1):
                min_index = i
                for j in range(i + 1, len(self.poss)):
                    if self.poss[j] < self.poss[min_index]:
                        min_index = j
                self.poss[min_index], self.poss[i] = self.poss[i], self.poss[min_index]
                for i in range(len(self.arr)):
                    self.arr[i].pos = self.poss[i]
                graph.refresh()
                pygame.time.delay(5)
        elif num%5 == 2:
            pygame.display.update()
            for i in range(1, len(self.poss)):
                key = self.poss[i]
                j = i - 1
                while j >= 0 and key < self.poss[j]:
                    self.poss[j + 1] = self.poss[j]
                    j -= 1
                self.poss[j + 1] = key
                for i in range(len(self.arr)):
                    self.arr[i].pos = self.poss[i]
                graph.refresh()
                pygame.time.delay(5)
        elif num%5 == 3:
            def getNextGap(gap):
                # Shrink gap by Shrink factor
                gap = (gap * 10) / 13
                if gap < 1:
                    return 1
                return int(gap)
            n = len(self.poss)

            # Initialize gap
            gap = n

            # Initialize swapped as true to make sure that
            # loop runs
            swapped = True

            # Keep running while gap is more than 1 and last
            # iteration caused a swap
            while gap != 1 or swapped == 1:

                # Find next gap
                gap = getNextGap(gap)

                # Initialize swapped as false so that we can
                # check if swap happened or not
                swapped = False

                # Compare all elements with current gap
                for i in range(0, n - gap):
                    if self.poss[i] > self.poss[i + gap]:
                        self.poss[i], self.poss[i + gap] = self.poss[i + gap], self.poss[i]
                        swapped = True
                        for j in range(len(self.arr)):
                            self.arr[j].pos = self.poss[j]
                        graph.refresh()
                        pygame.time.delay(5)
        elif num%5 == 4:
            n = len(self.poss)
            gap = n / 2

            # Do a gapped insertion sort for this gap size.
            # The first gap elements a[0..gap-1] are already in gapped
            # order keep adding one more element until the entire array
            # is gap sorted
            while int(gap) > 0:

                for i in range(int(gap), n):

                    # add a[i] to the elements that have been gap sorted
                    # save a[i] in temp and make a hole at position i
                    temp = self.poss[i]

                    # shift earlier gap-sorted elements up until the correct
                    # location for a[i] is found
                    j = i
                    while j >= gap and self.poss[j - int(gap)] > temp:
                        self.poss[j] = self.poss[j - int(gap)]
                        j -= int(gap)

                    # put temp (the original a[i]) in its correct location
                    self.poss[j] = temp
                    for j in range(len(self.arr)):
                        self.arr[j].pos = self.poss[j]
                    graph.refresh()
                    pygame.time.delay(5)
                gap = int(gap / 2)
    def refresh(self):
        SCREEN.fill(BG_COLOR)
        shuffle_button = pygame.draw.rect(SCREEN, WHITE, box)
        sort_button = pygame.draw.rect(SCREEN, GREEN, pygame.Rect(50, 340, 100, 50))
        type_button = pygame.draw.rect(SCREEN, PURPLE, pygame.Rect(450, 340, 100, 50))
        pygame.draw.line(SCREEN, BLACK, (0, 324), (600, 324), 3)
        for i in range(len(self.arr)):
            self.arr[i].draw()
        pygame.display.flip()


WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Sorting Algos')

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (232, 81, 81)
GREEN = (46, 230, 46)
PURPLE = (182, 74, 212)
BG_COLOR = (83, 166, 160)

# init screen
SCREEN.fill(BG_COLOR)
pygame.draw.line(SCREEN, BLACK, (0, 324), (600, 324), 3)



# BUTTONS
box = pygame.Rect(250, 340, 100, 50)
graph = Graph()
graph.refresh()
shuffle_button = pygame.draw.rect(SCREEN, WHITE, pygame.Rect(250, 340, 100, 50))
sort_button = pygame.draw.rect(SCREEN, GREEN, pygame.Rect(50, 340, 100, 50))
type_button = pygame.draw.rect(SCREEN, PURPLE, pygame.Rect(450, 340, 100, 50))
#text
shuffle_font = pygame.font.SysFont('Arial Black', 15)
shuffle_text = shuffle_font.render('SHUFFLE', False, BLACK)
sort_font = pygame.font.SysFont('Arial Black', 15)
sort_text = sort_font.render("SORT", False, BLACK)
type_font = shuffle_font
type_text = type_font.render(typeStr, False, BLACK)



is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if shuffle_button.collidepoint(mouse):
                graph.shuffle()
                graph.refresh()
                done_sorting = False
            if sort_button.collidepoint(mouse) and done_sorting == False:
                graph.sort(num)
                done_sorting = True
            if type_button.collidepoint(mouse):
                num+=1
                if num%5 == 0:
                    graph.refresh()
                    typeStr = "BUBBLE"
                    type_text = type_font.render(typeStr, False, BLACK)
                    SCREEN.blit(type_text, (460, 350))
                if num%5 == 1:
                    graph.refresh()
                    typeStr = "SELECT"
                    type_text = type_font.render(typeStr, False, BLACK)
                    SCREEN.blit(type_text, (460, 350))
                if num%5 == 2:
                    graph.refresh()
                    typeStr = "INSERT"
                    type_text = type_font.render(typeStr, False, BLACK)
                    SCREEN.blit(type_text, (460, 350))
                if num%5 == 3:
                    graph.refresh()
                    typeStr = "COMB"
                    type_text = type_font.render(typeStr, False, BLACK)
                    SCREEN.blit(type_text, (460, 350))
                if num%5 == 4:
                    graph.refresh()
                    typeStr = "SHELL"
                    type_text = type_font.render(typeStr, False, BLACK)
                    SCREEN.blit(type_text, (460, 350))

    SCREEN.blit(shuffle_text, (260, 350))
    SCREEN.blit(sort_text, (75, 350))
    SCREEN.blit(type_text, (460, 350))
    pygame.display.update()
pygame.quit()
