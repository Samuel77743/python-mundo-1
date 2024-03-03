import pygame

print('Tocando trilha sonora de GTA VI...')

pygame.init()

pygame.mixer.music.load('exercicios\ex021-audio.mp3')
pygame.mixer.music.play()

while True:
    pygame.event.wait()