
import random
import pygame

# ініціалізація Pygame
pygame.init()

# Налаштування вікна гри
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("5 Слот-Ігор")

# Шаблон слоту (символи для барабанів)
symbols = ['🍒', '🍋', '🍊', '🍉', '🔔', '⭐']

# Функція для обертання барабанів
def spin():
    return [random.choice(symbols) for _ in range(3)]

# Основний цикл гри
running = True
counter = 0  # лічильник для гри
while running and counter < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Слот обертається при натисканні кнопки
    result = spin()

    # Очищення екрану
    screen.fill((255, 255, 255))

    # Виведення результатів на екран
    font = pygame.font.SysFont('Arial', 48)
    text = font.render(f"Гра {counter + 1}: {' | '.join(result)}", True, (0, 0, 0))
    screen.blit(text, (width // 3, height // 2))

    # Оновлення екрану
    pygame.display.update()

    # Тривалість кожного обертання (1 секунда)
    pygame.time.delay(1000)

    # Підвищення лічильника ігор
    counter += 1

# Закриття гри
pygame.quit()
