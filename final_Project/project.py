from ctypes.wintypes import HFONT
import pygame
import sys
from pyvidplayer2 import Video

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Twewy Music Quiz!")
main_font = pygame.font.SysFont("ShinGoPro-ExLight", 50)
bg = pygame.image.load("udagawa.jpg")
Startsong = pygame.mixer.Sound("bird_in_the_hand.mp3")
FONT = pygame.font.SysFont("ShinGoPro-ExLight", 50)
#Failed Video player
'''WIDTH, HEIGHT = 900, 900
#SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))'''


class Button():
    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            print("Button Press!")
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "black")

button_surface = pygame.image.load("twewy_tb.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))
Question_button = Button(button_surface, 400, 300, "Click")
Answer_button_A = Button(button_surface, 400, 300, "Click")

current_question = ""
current_answer = ""

index = 0

demo_quiz_data = {
    "What are you in the mood for today?": "Techno" "Not feeling techno today...",
    "Japanese or english?": "Japanese" "English please!",
    "Older or Newer?": "Old school, foo" "New school bro",
    
}

current_question = list(demo_quiz_data)[index]
current_answer = list(demo_quiz_data.values())[index]
current_question_object = FONT.render(current_question, True, "white")
current_question_rect = current_question_object.get_rect(center=(400, 400))
current_answer_object = FONT.render(current_answer, True, "white")
current_answer_rect = current_answer_object.get_rect(center=(400, 400))
current_index_object = FONT.render(f"{index+1}/{len(demo_quiz_data)}", True, "white")
current_index_rect = current_index_object.get_rect(center=(400, 600))

def twewy_song_quiz():
    while True:
        for event in pygame.event.get():
            Startsong.play()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #if event.type == pygame.MOUSEBUTTONDOWN:
                #Start_button.checkForInput(pygame.mouse.get_pos(), 400, 300)
            
            #Testsong = pygame.mixer.Sound("Click_sound.mp3")
        #if Start_buttoncheckForInput(pygame.mouse.get_pos()):
            

        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        #Start_button.update()
        #Start_button.changeColor(pygame.mouse.get_pos())
        pygame.display.update()

        
#I Tried adding a video, It's too much to install
"""def startup():
    for event in pygame.event.get():
        vid = Video("Shiki_Fusion.mp4")
        vid.draw(SCREEN, (0, 0))
        twewy_song_quiz()
        pygame.display.update()
        if event.type == pygame.QUIT:
            vid.stop()"""

twewy_song_quiz()
