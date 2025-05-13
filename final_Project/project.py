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
Results1Song = pygame.mixer.Sound("Insomnia.mp3")
Results2Song = pygame.mixer.Sound("OWARI-HAJIMARI -NEO MIX-.mp3")
Results3Song = pygame.mixer.Sound("Revelation -NEO MIX-.mp3")
Results4Song = pygame.mixer.Sound("The World Ends With You - Lullaby For You.mp3")

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
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = main_font.render(self.text_input, True, "green")
        else:
            self.text = main_font.render(self.text_input, True, "black")

button_surface = pygame.image.load("twewy_tb.png")
button_surface = pygame.transform.scale(button_surface, (400, 150))

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
                if answer1.checkForInput(mouse_pos):
                    question2A()
                if answer2.checkForInput(mouse_pos):
                    question2B()

                    
                
        pygame.display.update()

def question2A():
    pygame.display.set_caption("Question 2A")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        question = Button(button_surface, 400, 300, "Ah Techno! Great choice! Are you feeling more amped or more lowkey?")
 
        answer1 = Button(button_surface, 200, 600, "AMPED TO THE MAX!")

        answer2 = Button(button_surface, 600, 600, "please keep it chill.")

        for button in [question, answer1, answer2]:
            button.changeColor(mouse_pos)
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answer1.checkForInput(mouse_pos):
                    results1() #Insomnia
                if answer2.checkForInput(mouse_pos):
                    results3() #Revelation 

        pygame.display.update()

def question2B():
    pygame.display.set_caption("Question 2B")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        question = Button(button_surface, 400, 300, "No Techno? No problem! JRock or R&B?")
   
        answer1 = Button(button_surface, 200, 600, "JRock is my life.")
    
        answer2 = Button(button_surface, 600, 600, "R&B all day, any day!")
   

        for button in [question, answer1, answer2]:
            button.changeColor(mouse_pos)
            button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if answer1.checkForInput(mouse_pos):
                    results2() #Owari Hajimari
                if answer2.checkForInput(mouse_pos):
                    results4() #Lulaby for You 

        pygame.display.update()       
        #return score1, score2
def results1():
    pygame.mixer.pause()
    Results1Song.play()
    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Insomnia, from NEO: TWEWY! Sit back and listen!")
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
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    twewy_song_quiz()
            
                
        pygame.display.update()  

def results2():
    pygame.mixer.pause()
    Results2Song.play()
    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Owari Hajimari, from NEO: TWEWY! Sit back and listen!")
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
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    twewy_song_quiz()
            
                
        pygame.display.update()       

def results3():
    pygame.mixer.pause()
    Results3Song.play()
    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Revelation, from NEO: TWEWY! (This is one of my personal favorites), Sit back and listen!")
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
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    twewy_song_quiz()
            
                
        pygame.display.update()         

def results4():
    pygame.mixer.pause()
    Results4Song.play()
    pygame.display.set_caption("Results!")
    while True:
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        mouse_pos = pygame.mouse.get_pos()
        reccomended_song = Button(button_surface, 400, 300, "You should listen to Lulaby for You, from TWEWY! It's a very sweet song. Sit back and listen!")
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
                if quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()
                if restart.checkForInput(mouse_pos):
                    twewy_song_quiz()
            
                
        pygame.display.update()   

    
def twewy_song_quiz():
    pygame.mixer.pause()
    Startsong.play()
    while True:
        for event in pygame.event.get():
            question1()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        screen.fill("#004166")
        screen.blit(bg, (75, 0))
        pygame.display.update()
            

twewy_song_quiz()
