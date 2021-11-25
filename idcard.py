import pygame, sys,random

pygame.init()

clock=pygame.time.Clock()
width=405
height=235
screen = pygame.display.set_mode((width,height))
images={}
images["boy"] = pygame.image.load("boy.png").convert_alpha()
images["girl"] = pygame.image.load("girl.png").convert_alpha()

score_font=pygame.font.Font('freesansbold.ttf', 15)
               

screen.blit( images["boy"]         ,[0,0])   

while True:       
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit() 

    school_text=score_font.render("WhiteHatJr school", False, (255,25,0))  
    
    name_text=score_font.render("Shubham Verma", False, (255,25,0))  
    
    grade_text=score_font.render("9", False, (255,25,0))  
    
    screen.blit(school_text,[230,80])
    screen.blit(name_text,[220,117])
    screen.blit(grade_text,[220,153])
    
    pygame.display.update() 
    clock.tick(30) 
    
    
    
    
    

 