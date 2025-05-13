from ctypes.wintypes import HFONT
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Twewy Music Quiz!")
main_font = pygame.font.SysFont("ShinGoPro-ExLight", 50)
bg = pygame.image.load("udagawa.jpg")
Startsong = pygame.mixer.Sound("bird_in_the_hand.mp3")
Click = pygame.mixer.Sound("Click_sound.mp3")
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
Answer_button_A = Button(button_surface, 200, 600, "Click")
Answer_button_B = Button(button_surface, 600, 600, "Click")

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
current_question_text = FONT.render(current_question, True, "black")
current_question_rect = current_question_text.get_rect(center=(400, 400))
current_answer_text = FONT.render(current_answer, True, "black")
current_answer_rect = current_answer_text.get_rect(center=(400, 400))
current_index_text = FONT.render(f"{index+1}/{len(demo_quiz_data)}", True, "black")
current_index_rect = current_index_text.get_rect(center=(400, 600))

def question1():
    pygame.display.set_caption("Question 1")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        score1 = 0
        score2 = 0
        mouse_pos = pygame.mouse.get_pos()
        question1 = Button(button_surface, 400, 300, "What are you in the mood for today?")
        answer1 = Button(button_surface, 200, 600, "Techno, duh.")
        answer2 = Button(button_surface, 600, 600, "Not feeling techno today...")

        for button in [question1, answer1, answer2]:
            button.changeColor(mouse_pos)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if question1.checkForInput(mouse_pos):
                    Click.play()
                if answer1.checkForInput(mouse_pos):
                    score1 = score1 + 1
                if answer2.checkForInput(mouse_pos):
                    score2 = score2 + 1
        pygame.display.update()
        
        return score1, score2
                    



def twewy_song_quiz(score1, score2):
    Startsong.play()
    while True:
        for event in pygame.event.get():
            screen.blit(current_question_text, (400, 300))
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Question_button.checkForInput(pygame.mouse.get_pos())
                Answer_button_A.checkForInput(pygame.mouse.get_pos())
                Answer_button_B.checkForInput(pygame.mouse.get_pos())
            

            
            
        #if Start_buttoncheckForInput(pygame.mouse.get_pos()):
            '''if score1 > score2:
                #stop playing
                #Results screen
                #Play song
            elif:'''

        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        Question_button.update()
        Answer_button_A.update()
        Answer_button_B.update()
        Question_button.changeColor(pygame.mouse.get_pos())
        Answer_button_A.changeColor(pygame.mouse.get_pos())
        Answer_button_B.changeColor(pygame.mouse.get_pos())
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
