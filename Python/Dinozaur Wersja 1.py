import pygame
import random

# Inicjowanie Pygame
pygame.init()

# Ustawienia okna gry
window_width = 800
window_height = 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Dinozaur w Google")

# Kolory
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Funkcja rysująca dinozaura
def draw_dinosaur(x, y):
    pygame.draw.rect(window, green, [x, y, 50, 50])
 
# Funkcja rysująca przeszkodę  
def draw_obstacle(x, y, width, height):
    pygame.draw.rect(window, white, [x, y, width, height])

# Główna funkcja gry
def game_loop():
    # Współrzędne dinozaura
    dino_x = 50
    dino_y = window_height - 100

    # Współrzędne pierwszej przeszkody
    obstacle_x = window_width
    obstacle_y = window_height - 50
    obstacle_width = 50
    obstacle_height = 50

    # Prędkość gry
    speed = 1

    # Pętla gry
    game_over = False
    while not game_over:
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    dino_y -= 100

        # Rysowanie tła
        window.fill(black)

        # Rysowanie dinozaura
        draw_dinosaur(dino_x, dino_y)

        # Rysowanie przeszkody
        draw_obstacle(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

        # Poruszanie przeszkody
        obstacle_x -= speed

        # Sprawdzanie kolizji
        if obstacle_x < dino_x + 50 and obstacle_x + obstacle_width > dino_x and obstacle_y < dino_y + 50 and obstacle_y + obstacle_height > dino_y:
            print("Game over!")
            game_over = True

        # Tworzenie nowych przeszkód
        if obstacle_x < -obstacle_width:
            obstacle_x = window_width
            obstacle_y = window_height - 50 - random.randint(0, 200)
            obstacle_width = random.randint(50, 100)
            obstacle_height = random.randint(50, 100)

        # Wyświetlanie okna gry
        pygame.display.update()

    # Zamknięcie Pygame
    pygame.quit()
    quit()

# Rozpoczęcie gry
game_loop()


    
