"""
***
Word Up! (ver. 1.0) by Ratrio101
This is my remake/adaptation of the game "Соображарий" by Nikolai Pegasov.
All rights to the original idea and design belong to Nikolai Pegasov.
***
"""

# Imports
import pygame
import random

# pygame initialization
pygame.init()

# Window parameters
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Word Up! (by Ratrio101)")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 102, 204)

# Fonts
font_large = pygame.font.Font(None, 74)
font_medium = pygame.font.Font(None, 50)
font_small = pygame.font.Font(None, 36)

# Question list (You can add or change questions here...)
questions = [
    "Гора, река, озеро, море",
    "Вещь, которую можно встретить в школе / институте",
    "Вещь, которую можно сделать из металла",
    "Можно увидеть в больнице",
    "Можно положить в карман",
    "То, на что Вы можете посмотреть прямо сейчас",
    "Страна",
    "Животное",
    "Город",
    "Еда",
    "Наречие",
    "Растение",
    "Профессия",
    "Одежда",
    "Вымышленный персонаж",
    "Слово, в котором есть 'Ь'",
    "Вещь, которая есть у Вашей семьи",
    "Вещь дороже 1 млн. рублей",
    "Вещь дешевле 100 рублей",
    "Абстрактное понятие (то, что нельзя потрогать)",
    "Вещь, которую запрещено проносить в самолет",
    "Произведение (книга, песня, фильм, ...)",
    "Связано с игрушками и играми",
    "Вещь - орудие преступления",
    "Можно коллекционировать",
    "Тоньше сантиметра",
    "Вещество, материал",
    "Связано с музыкой",
    "Вещь, которой нет у Вашей семьи",
    "Знаменитая личность (фамилия, псевдоним, прозвище)",
    "Часть тела человека или животного",
    "Можно поломать или испортить руками",
    "Техническое устройство",
    "Продается в супермаркете",
    "Напиток",
    "Мужское имя",
    "Женское имя",
    "Не стоит давать детям",
    "Слово, что заканчивается на эту букву",
    "Весит больше тонны",
    "Бренд",
    "Слово из шести букв",
    "Аббревиатура",
    "Можно увидеть в деревне",
    "Слово, где эта буква встречается 2 раза",
    "Вещь, которую можно сделать из древесины",
    "Может быть красного цвета",
    "Вещь, которая не могла существовать 100 лет назад",
    "Связано с войной",
    "Связано со спортом",
    "Вещь, которую могли изготовить 1000 лет назад"
]

# Letters list (You can add or change letters here...)
letters = list("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ")

# Shuffle cards
random.shuffle(questions)
random.shuffle(letters)

# Draw text
def draw_text(text, font, color, x, y, center=False):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y) if center else (x, y))
    screen.blit(text_obj, text_rect)

# Draw button
def draw_button(text, font, color, rect, active=False):
    pygame.draw.rect(screen, DARK_BLUE if active else GRAY, rect, border_radius=10)
    text_obj = font.render(text, True, WHITE)
    text_rect = text_obj.get_rect(center=rect.center)
    screen.blit(text_obj, text_rect)

# Draw BG
def draw_gradient_background():
    for i in range(HEIGHT):
        color = (
            LIGHT_BLUE[0] + (DARK_BLUE[0] - LIGHT_BLUE[0]) * i // HEIGHT,
            LIGHT_BLUE[1] + (DARK_BLUE[1] - LIGHT_BLUE[1]) * i // HEIGHT,
            LIGHT_BLUE[2] + (DARK_BLUE[2] - LIGHT_BLUE[2]) * i // HEIGHT
        )
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))

# Input names
def input_names():
    global screen, WIDTH, HEIGHT

    input_boxes = [
        pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 - 80, 400, 50),
        pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 20, 400, 50)
    ]
    active_box = None
    colors = [GRAY, GRAY]
    names = ["", ""]
    running = True
    clock = pygame.time.Clock()

    print("Ожидаем ввод имен игроков...")

    while running:
        screen.fill(WHITE)
        draw_gradient_background()

        # Text
        draw_text("Введите имена игроков:", font_medium, BLACK, WIDTH // 2, HEIGHT // 2 - 150, center=True)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Выход из игры через pygame.QUIT")
                pygame.quit()
                return None

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Click check
                for i, box in enumerate(input_boxes):
                    if box.collidepoint(event.pos):
                        active_box = i
                        break
                else:
                    active_box = None

            if event.type == pygame.KEYDOWN:
                if active_box is not None:
                    if event.key == pygame.K_RETURN:  # You can complete input by pressing Enter
                        running = False
                    elif event.key == pygame.K_BACKSPACE:  # Delete symbols
                        names[active_box] = names[active_box][:-1]
                    else:
                        text_width = font_medium.size(names[active_box] + event.unicode)[0]
                        if text_width < input_boxes[active_box].width - 20:
                            names[active_box] += event.unicode

        # Draw input fields
        for i, box in enumerate(input_boxes):
            colors[i] = BLUE if active_box == i else GRAY
            pygame.draw.rect(screen, colors[i], box, 2)

            text_surface = font_medium.render(names[i], True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (box.x + 10, box.y + (box.height - text_rect.height) // 2)
            screen.blit(text_surface, text_rect)

            # Player name tags
            draw_text(f"Игрок {i + 1}:", font_small, BLACK, box.x - 110, box.y + 10)

        # Complete button
        finish_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 120, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = finish_button.collidepoint(mouse_pos)
        draw_button("Начать", font_small, WHITE, finish_button, active=is_hovered)

        if pygame.mouse.get_pressed()[0] and is_hovered:
            running = False

        pygame.display.flip()
        clock.tick(30)

    print(f"Имена игроков: {names}")
    return names

def main():
    global screen, WIDTH, HEIGHT

    running = True
    fullscreen = False
    clock = pygame.time.Clock()

    # Get names
    player_names = input_names()
    if not player_names:
        print("Имена игроков не введены. Завершаем игру.")
        return

    # Current question and letters
    current_question = random.choice(questions)
    player_letters = [random.choice(letters) for _ in range(2)]

    print(f"Начинаем игру: {player_names}")

    while running:
        screen.fill(WHITE)
        draw_gradient_background()

        # manage events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Выход из игры через pygame.QUIT")
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:  # Fullscreen
                    fullscreen = not fullscreen
                    if fullscreen:
                        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        print("Полноэкранный режим включен")
                    else:
                        screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                        print("Полноэкранный режим отключен")

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Change question
                if next_button.collidepoint(event.pos):
                    current_question = random.choice(questions)
                    player_letters = [random.choice(letters) for _ in range(2)]
                    print(f"Новый вопрос: {current_question}, буквы: {player_letters}")

            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                print(f"Изменен размер окна: {WIDTH}x{HEIGHT}")

        # question
        draw_text("Вопрос:", font_medium, BLACK, WIDTH // 2, HEIGHT // 10, center=True)
        draw_text(current_question, font_large, BLACK, WIDTH // 2, HEIGHT // 5, center=True)

        # Names and letters
        draw_text(f"{player_names[0]}:", font_small, BLACK, WIDTH // 4, HEIGHT // 2 - 100, center=True)
        draw_text(player_letters[0], font_large, RED, WIDTH // 4, HEIGHT // 2 - 50, center=True)

        draw_text(f"{player_names[1]}:", font_small, BLACK, 3 * WIDTH // 4, HEIGHT // 2 - 100, center=True)
        draw_text(player_letters[1], font_large, GREEN, 3 * WIDTH // 4, HEIGHT // 2 - 50, center=True)

        # "NEXT" button (next question)
        next_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)
        mouse_pos = pygame.mouse.get_pos()
        is_hovered = next_button.collidepoint(mouse_pos)
        draw_button("Следующий", font_small, WHITE, next_button, active=is_hovered)

        # Screen update
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    print("Игра завершена.")

if __name__ == "__main__":
    main()