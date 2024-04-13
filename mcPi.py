import numpy as np
import pygame
from time import sleep

# Parameters

numIterations = 100_000_000
coordinates = []

# Colors 
RED = (193, 18, 31)
BLUE = (102, 155, 188)
YELLOW = (255, 186, 8)
WHITE = (253, 240, 213)
BLACK = (3, 7, 30)
DARKRED = (120, 0, 0)
DARKBLUE = (0, 48, 73)






# Functions
def calculate_pi(coordinates):
  numberInside = 0
  for x,y in coordinates:
    position = (x-400)**2 + (y-400)**2
    if position <= 300**2:
      numberInside+=1
  
  return 4*numberInside/len(coordinates)

def create_random_coordinates():
  return np.random.randint(100,700,size=2)

def draw_pi(screen, font, pi, i):
  text = font.render(f'Aproximación π ≈ {np.round(pi,5)}', True, DARKBLUE)
  textRect = text.get_rect()
  textRect.centerx +=10 
  screen.blit(text, textRect)

  text2 = font.render(f'No. de iteración: {i}', True, DARKBLUE)
  textRect2 = text2.get_rect()
  textRect2.centery = textRect2.centery + textRect.bottom
  textRect2.centerx +=10 

  screen.blit(text2, textRect2)
  return


def draw_points(screen, coordinates):
  for point in coordinates:
    pygame.draw.circle(screen, BLUE, point, 3 )
  return

def draw_base_window(screen):
  screen.fill(WHITE)
  pygame.draw.circle(screen, RED, (400, 400), 300, 5)
  return

def draw_circle(screen):
  pygame.draw.circle(screen, RED, (400, 400), 300, 5)
  return




# Main Loop
pygame.init()
screen = pygame.display.set_mode((800,800))
font = pygame.font.Font('default.ttf', 20)


i = 0

run = True

while run: 
    # Eventos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run= False
  

    # Chequea iteraciones
  if i<numIterations:
    coordinates.append(create_random_coordinates())
    i += 1
  
  if i%10 == 0: # Dibuja cada 10 (lo hace más eficiente)
      # Dibuja la base
    draw_base_window(screen)  
    
      # Dibuja los puntos
    draw_points(screen, coordinates)

      # Calcula y escribe Pi
    draw_pi(screen, font,  calculate_pi(coordinates), i)

      # Dibuja de nuevo el círculo para que no se oculte
    draw_circle(screen)

      # Update
    pygame.display.update()

  #sleep(0.1)