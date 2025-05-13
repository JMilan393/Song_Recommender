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
#Results1Song = pygame.mixer.Sound("Insomnia.mp3")
#Results2Song = pygame.mixer.Sound("Owari_Hajimari.mp3")

#Failed Video player



class Button():

    def __init__(self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "black")
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

"""class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = main_font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
            self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
            self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
            screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

#button_surface = pygame.image.load("twewy_tb.png")
#button_surface = pygame.transform.scale(button_surface, (400, 150))"""


demo_quiz_data = {
    "What are you in the mood for today?": "Techno" "Not feeling techno today...",
    "Japanese or english?": "Japanese" "English please!",
    "Older or Newer?": "Old school, foo" "New school bro",
    
}

def question1():
    pygame.display.set_caption("Question 1")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        question1 = Button(button_surface, 400, 300, "What are you in the mood for today?")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(400, 300), 
            #text_input="What are you in the mood for today?", font=main_font, base_color="black", hovering_color="green")
        #Button(button_surface, 400, 300, "What are you in the mood for today?")
        answer1 = Button(button_surface, 200, 600, "Techno, duh.")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(200, 600), 
            #text_input="Techno, duh.", font=main_font, base_color="black", hovering_color="green")
        answer2 = Button(button_surface, 600, 600, "Not feeling techno today...")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(600, 600), 
            #text_input="Not feeling techno today...", font=main_font, base_color="black", hovering_color="green")

        for button in [question1, answer1, answer2]:
            button.changeColor(mouse_pos)
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if question1.checkForInput(mouse_pos):
                    Click.play()
                if answer1.checkForInput(mouse_pos):
                    results1()
                if answer2.checkForInput(mouse_pos):
                    results2()

                    
                
        pygame.display.update()
        
        #return score1, score2
def results1():
    pygame.mixer.pause()

    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Insomnia, from NEO: TWEWY!")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(400, 300), 
            #text_input="What are you in the mood for today?", font=main_font, base_color="black", hovering_color="green")
        #Button(button_surface, 400, 300, "What are you in the mood for today?")
        quit = Button(button_surface, 200, 600, "QUIT")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(200, 600), 
            #text_input="Techno, duh.", font=main_font, base_color="black", hovering_color="green")
        restart = Button(button_surface, 600, 600, "Restart?")
        #Button(image=pygame.image.load("twewy_tb.png"), pos=(600, 600), 
            #text_input="Not feeling techno today...", font=main_font, base_color="black", hovering_color="green")

        for button in [reccomended_song, quit, restart]:
            button.changeColor(mouse_pos)
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if question1.checkForInput(mouse_pos):
                    Click.play()
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    question1()
            
                
        pygame.display.update()  

def results2():
    pygame.mixer.pause()

    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Owari Hajimari, from NEO: TWEWY!")
        quit = Button(button_surface, 200, 600, "QUIT")
        restart = Button(button_surface, 600, 600, "Restart?")

        for button in [reccomended_song, quit, restart]:
            button.changeColor(mouse_pos)
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if question1.checkForInput(mouse_pos):
                    Click.play()
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    question1()
            
                
        pygame.display.update()          




def twewy_song_quiz():
    Startsong.play()
    
    while True:
        for event in pygame.event.get():
            question1()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        
            
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #question1.checkForInput(pygame.mouse.get_pos())
                #Question_button.checkForInput(pygame.mouse.get_pos())
                #Answer_button_A.checkForInput(pygame.mouse.get_pos())
                #Answer_button_B.checkForInput(pygame.mouse.get_pos())
        #if Start_buttoncheckForInput(pygame.mouse.get_pos()):
            
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
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
