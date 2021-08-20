import pygame
import numpy


WINDOW_WIDTH = 630
WINDOW_HEIGHT = 600
IMAGE = 'Connect4_Empty.png'
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
PLAYER_1 = 1
PLAYER_2 = 2


def create_game():
    game = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return game


def grader(game):
    numpy.random.seed(3)
    grader = numpy.ones((69, 4))
    counter = 0
    for i in range(6):
        for j in range(4):
            grader[counter] = [int(game[i][j]), int(game[i][j + 1]), int(game[i][j + 2]), int(game[i][j + 3])]
            counter += 1
    for i in range(3):
        for j in range(7):
            grader[counter] = [int(game[i][j]), int(game[i + 1][j]), int(game[i + 2][j]), int(game[i + 3][j])]
            counter += 1
    for i in range(3):
        for j in range(4):
            grader[counter] = [int(game[i][j]), int(game[i + 1][j + 1]), int(game[i + 2][j + 2]),
                               int(game[i + 3][j + 3])]
            counter += 1
    for i in range(3):
        for j in range(4):
            grader[counter] = [int(game[i + 3][j]), int(game[i + 2][j + 1]), int(game[i + 1][j + 2]),
                               int(game[i][j + 3])]
            counter += 1
    return grader


def check_grade(game):
    com_grade = 0
    player_grade = 0
    grad_tester = grader(game)
    for i in grad_tester:
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for j in range(4):
            if i[j] == 0:
                count_0 += 1
            if i[j] == 1:
                count_1 += 1
            if i[j] == 2:
                count_2 += 1
        if count_1 > 0 and count_2 == 0:
            player_grade = player_grade + count_1 ^ 3
        if count_2 > 0 and count_1 == 0:
            com_grade = com_grade + count_2 ^ 3
        if count_2 == 4:
            com_grade = 400
        if count_1 == 4:
            player_grade = 400
    grade = com_grade - player_grade
    return grade


def computer_play(game):
    best_column = 4
    best_grade = -1000000
    for column in range(1, 8):
        count1 = 0
        game_1 = game
        for i in range(6):
            if game_1[5 - i][int(column) - 1] == 0:
                game_1[5 - i][int(column) - 1] = 2
                flag_i1 = 5 - i
                flag_j1 = int(column) - 1
                count1 = 1
                break
        if count1 == 1:
            grade = check_grade(game_1)
            for column1 in range(1, 8):
                count2 = 0
                for i in range(6):
                    if game_1[5 - i][int(column1) - 1] == 0:
                        game_1[5 - i][int(column1) - 1] = 1
                        flag_i2 = 5 - i
                        flag_j2 = int(column1) - 1
                        count2 = 1
                        break
                if count2 == 1:
                    grade = grade + check_grade(game_1)
                    for column2 in range(1, 8):
                        count3 = 0
                        for i in range(6):
                            if game_1[5 - i][int(column2) - 1] == 0:
                                game_1[5 - i][int(column2) - 1] = 2
                                flag_i3 = 5 - i
                                flag_j3 = int(column2) - 1
                                count3 = 1
                                break
                        if count3 == 1:
                            grade = grade + check_grade(game_1)
                            for column3 in range(1, 8):
                                count4 = 0
                                for i in range(6):
                                    if game_1[5 - i][int(column3) - 1] == 0:
                                        game_1[5 - i][int(column3) - 1] = 1
                                        flag_i4 = 5 - i
                                        flag_j4 = int(column3) - 1
                                        count4 = 1
                                        break
                                if count4 == 1:
                                    grade = grade + check_grade(game_1)
                                    game_1[flag_i4][flag_j4] = 0
                            game_1[flag_i3][flag_j3] = 0
                    game_1[flag_i2][flag_j2] = 0
            game_1[flag_i1][flag_j1] = 0
            if grade > best_grade:
                best_grade = grade
                best_column = column
    return best_column


def play(game, player, screen, is_computer):
    if player == PLAYER_1:
        color = RED
    if player == PLAYER_2:
        color = GREEN
    if is_computer:
        column = computer_play(game)
    else:
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse = pygame.mouse.get_pos()
                    if 0 < mouse[0] < 90:
                        column = 1
                        flag = False
                        break
                    if 90 < mouse[0] < 180:
                        column = 2
                        flag = False
                        break
                    if 180 < mouse[0] < 270:
                        column = 3
                        flag = False
                        break
                    if 270 < mouse[0] < 360:
                        column = 4
                        flag = False
                        break
                    if 360 < mouse[0] < 450:
                        column = 5
                        flag = False
                        break
                    if 450 < mouse[0] < 540:
                        column = 6
                        flag = False
                        break
                    if 540 < mouse[0] < 630:
                        column = 7
                        flag = False
                        break
    if int(column) > 7 or int(column) < 1:
        return game
    for i in range(6):
        if game[5 - i][int(column) - 1] == 0:
            game[5 - i][int(column) - 1] = player
            pygame.draw.circle(screen, color, ((column - 1) * 87 + 58, (5 - i) * 87 + 58), 30)
            return game
    return game


def did_won(game, player):
    for i in range(6):
        for j in range(7):
            if game[i][j] == player:
                if i + 3 < 6:
                    if game[i + 1][j] == player and game[i + 2][j] == player and game[i + 3][j] == player:
                        return True
                if i + 2 < 6 and i - 1 >= 0:
                    if game[i + 1][j] == player and game[i + 2][j] == player and game[i - 1][j] == player:
                        return True
                if i + 1 < 6 and i - 2 >= 0:
                    if game[i + 1][j] == player and game[i - 1][j] == player and game[i - 2][j] == player:
                        return True
                if i - 3 >= 0:
                    if game[i - 1][j] == player and game[i - 2][j] == player and game[i - 3][j] == player:
                        return True
                if j + 3 < 7:
                    if game[i][j + 1] == player and game[i][j + 2] == player and game[i][j + 3] == player:
                        return True
                if j + 2 < 7 and j - 1 >= 0:
                    if game[i][j + 1] == player and game[i][j + 2] == player and game[i][j - 1] == player:
                        return True
                if j + 1 < 7 and j - 2 >= 0:
                    if game[i][j + 1] == player and game[i][j - 1] == player and game[i][j - 2] == player:
                        return True
                if j + 3 < 7 and i + 3 < 6:
                    if game[i + 1][j + 1] == player and game[i + 2][j + 2] == player and game[i + 3][j + 3] == player:
                        return True
                if i + 2 < 6 and j + 2 < 7 and i - 1 >= 0 and j - 1 >= 0:
                    if game[i + 1][j + 1] == player and game[i + 2][j + 2] == player and game[i - 1][j - 1] == player:
                        return True
                if i + 1 < 6 and j + 1 < 7 and i - 2 > +0 and j - 2 >= 0:
                    if game[i + 1][j + 1] == player and game[i - 1][j - 1] == player and game[i - 2][j - 2] == player:
                        return True
                if i - 3 >= 0 and j - 3 >= 0:
                    if game[i - 1][j - 1] == player and game[i - 2][j - 2] == player and game[i - 3][j - 3] == player:
                        return True
                if j - 3 >= 0:
                    if game[i][j - 1] == player and game[i][j - 2] == player and game[i][j - 3] == player:
                        return True
                if i + 3 < 6 and j - 3 >= 0:
                    if game[i + 1][j - 1] == player and game[i + 2][j - 2] == player and game[i + 3][j - 3] == player:
                        return True
                if i + 2 < 6 and j - 2 >= 0 and i - 1 >= 0 and j + 1 < 7:
                    if game[i + 1][j - 1] == player and game[i + 2][j - 2] == player and game[i - 1][j + 1] == player:
                        return True
                if i + 1 < 6 and i - 2 >= 0 and j - 1 >= 0 and j + 2 < 7:
                    if game[i + 1][j - 1] == player and game[i - 1][j + 1] == player and game[i - 2][j + 2] == player:
                        return True
                if i - 3 >= 0 and j + 3 < 7:
                    if game[i - 1][j + 1] == player and game[i - 2][j + 2] == player and game[i - 3][j + 3] == player:
                        return True
    return False



def two_players(screen, img, is_one_player):
    font = pygame.font.Font('freesansbold.ttf', 28)
    text1 = font.render('player 1:', WHITE, WHITE)
    text2 = font.render('player 2:', WHITE, WHITE)
    text3 = font.render('player 1 is the winner!!', WHITE, WHITE)
    text4 = font.render('player 2 is the winner!!', WHITE, WHITE)
    screen.blit(img, (0, 0))
    game = create_game()
    while True:
        pygame.draw.rect(screen, BLACK, [0, 560, 630, 30])
        screen.blit(text1, (250, 560))
        pygame.display.flip()
        game = play(game, PLAYER_1, screen, False)
        if did_won(game, PLAYER_1):
            pygame.draw.rect(screen, BLACK, [0, 560, 630, 30])
            screen.blit(text3, (250, 560))
            break
        pygame.draw.rect(screen, BLACK, [0, 560, 630, 30])
        screen.blit(text2, (150, 560))
        pygame.display.flip()
        game = play(game, PLAYER_2, screen, is_one_player)
        if did_won(game, PLAYER_2):
            pygame.draw.rect(screen, BLACK, [0, 560, 630, 30])
            screen.blit(text4, (150, 560))
            break
    return


def main():
    pygame.init()
    size = (WINDOW_WIDTH, WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("game")
    img = pygame.image.load(IMAGE)
    screen.blit(img, (0, 0))
    while True:

        font = pygame.font.Font('freesansbold.ttf', 28)
        text1 = font.render('One player', WHITE, WHITE)
        text2 = font.render('Two players', WHITE, WHITE)
        text3 = font.render('QUIT', WHITE, WHITE)
        pygame.draw.rect(screen, RED, [100, 100, 170, 30])
        pygame.draw.rect(screen, RED, [400, 100, 170, 30])
        pygame.draw.rect(screen, RED, [250, 300, 140, 40])
        screen.blit(text1, (100, 100))
        screen.blit(text2, (400, 100))
        screen.blit(text3, (280, 305))

        for event in pygame.event.get():
            pygame.display.flip()
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 100 < mouse[0] < 270 and 100 < mouse[1] < 130:
                    two_players(screen, img, True)
                if 400 < mouse[0] < 570 and 100 < mouse[1] < 130:
                    two_players(screen, img, False)
    pygame.quit()


if __name__ == '__main__':
    main()
