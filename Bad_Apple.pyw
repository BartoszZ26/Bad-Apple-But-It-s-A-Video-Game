from turtle import color
import pygame
from pyvidplayer import Video
import sys

with open("Resources/settings.txt") as f:
    text = f.read()

text = text.split(' ')
pygame.font.init()
isHard = bool(int(text[5]))

if(isHard):
    vid = Video("Resources/BadAppleHard.mp4")
else:
    vid = Video("Resources/BadApple.mp4")
vid.set_size((int(text[1]), int(text[3])))
pygame.display.set_icon(pygame.image.load("Resources/icon.png"))
win = pygame.display.set_mode(vid.current_size)
pygame.display.set_caption("Bad Apple")

font = pygame.font.Font("Resources/Pixeltype.ttf", 40)

score = 0.0
pixel_color = (0,0,0)

while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vid.close()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    if key == "r":
        score = 0
        vid.restart()           #rewind video to beginning
    elif key == "up":
        vid.set_volume(vid.get_volume() + 0.1)     #max volume
    elif key == "down":
        vid.set_volume(vid.get_volume() - 0.1)     #min volume

    
    vid.draw(win, (0, 0), force_draw=False)
    pixel_color = win.get_at(pygame.mouse.get_pos())[:3]
    if (sum(pixel_color) > 250*3) and pygame.mouse.get_focused():
        if(isHard):
            score+=1.25
        else:
            score+=1
    text = font.render(str(int(score)), False, (150,150,150))
    win.blit(text, (0,0))
    pygame.display.update()
    pygame.time.wait(10) # 100fps, perfect score < 21900
