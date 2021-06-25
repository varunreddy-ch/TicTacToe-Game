import sys
import time
import pygame
import colors

pygame.init()

# Height and width of the game screen
width, height = 500, 600
screen = pygame.display.set_mode((width, height))

# caption and icon
pygame.display.set_caption("Tic Tac Toe")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

# defining Fonts
very_small_font = pygame.font.SysFont('corbel', 20)
small_font = pygame.font.SysFont('corbel', 35)
medium_font = pygame.font.SysFont('corbel', 50)

# Text with above fonts
text = small_font.render('Start', True, colors.white)
player1 = small_font.render('Player 1', True, colors.white)
player2 = small_font.render('Player 2', True, colors.white)
score = medium_font.render("0:0", True, colors.red)

# Images
tic_tac_toe_board = pygame.image.load("images/board.png")  # Grid image
tic_tac_toe_board = pygame.transform.scale(tic_tac_toe_board, (300, 300))
x = pygame.image.load("images/x.png")  # X image
x = pygame.transform.scale(x, (60, 60))
o = pygame.image.load("images/o.png")  # O image
o = pygame.transform.scale(o, (60, 60))
red_line = pygame.image.load("images/red_line.png")  # red line image
black_line = pygame.image.load("images/black_line.png")  # black line image

# board to record the positions of choice
board = dict()

# initial score
player1_score = 0
player2_score = 0
turn = "player1"
player1_with_x = True

x_o = []
# Numbers for 1 to 9 with the font stored in x_o list
for i in range(9):
    x_o.append(very_small_font.render(str(i + 1), True, colors.red))


# Making the score to change and appear
def winner(win):
    global board
    global score
    global player1_score
    global player2_score
    if win == "player1":
        player1_score += 1
    else:
        player2_score += 1
    # Score is changed
    score = medium_font.render(f"{player1_score}:{player2_score}", True, colors.red)
    board = dict()


# Winner line
def cross_line(black_line_position, red_line_position, black_line, red_line):
    if turn == "player1":
        if player1_with_x:
            screen.blit(black_line, black_line_position)
        else:
            screen.blit(red_line, red_line_position)
    else:
        if player1_with_x:
            screen.blit(red_line, red_line_position)
        else:
            screen.blit(black_line, black_line_position)
    pygame.display.update()
    time.sleep(1)


# Function to check winner
def check_winner():
    global board
    global red_line
    global black_line

    # Column Check
    for i in range(3):
        if board.get(str(i + 1)) == board.get(str(i + 4)) and board.get(str(i + 4)) == board.get(
                str(i + 7)) and board.get(str(i + 7)):
            winner(board.get(str(i + 1)))

            black_line_position = (100 + (i % 3) * 90, -50)  # and change = 90
            red_line_position = (60 + (i % 3) * 90, 60)

            # Transforming and rotating the lines accordingly
            temp_red_line = pygame.transform.scale(red_line, (260, 100))
            temp_red_line = pygame.transform.rotate(temp_red_line, -70)

            temp_black_line = pygame.transform.scale(black_line, (510, 100))
            temp_black_line = pygame.transform.rotate(temp_black_line, - 90)

            cross_line(black_line_position, red_line_position, temp_black_line, temp_red_line)

            return

    # Row check
    for i in range(0, 7, 3):
        if board.get(str(i + 1)) == board.get(str(i + 2)) and board.get(str(i + 2)) == board.get(
                str(i + 3)) and board.get(str(i + 3)):
            winner(board.get(str(i + 1)))

            black_line_position = (-20, 245 - (i // 3) * 100)  # and change = 100
            red_line_position = (95, 205 - (i // 3) * 100)

            # Transforming and rotating the lines accordingly
            temp_red_line = pygame.transform.scale(red_line, (260, 100))
            temp_red_line = pygame.transform.rotate(temp_red_line, 20)
            temp_black_line = pygame.transform.scale(black_line, (510, 100))

            cross_line(black_line_position, red_line_position, temp_black_line, temp_red_line)
            return

    # Diagonal
    if board.get('1') == board.get('5') and board.get('5') == board.get('9') and board.get('9'):
        winner(board.get('1'))

        black_line_position = (-20, -40)
        red_line_position = (110, 50)

        # Transforming and rotating the lines accordingly
        temp_red_line = pygame.transform.scale(red_line, (320, 80))
        temp_red_line = pygame.transform.rotate(temp_red_line, 20 + 38)

        temp_black_line = pygame.transform.scale(black_line, (610, 100))
        temp_black_line = pygame.transform.rotate(temp_black_line, 45)

        cross_line(black_line_position, red_line_position, temp_black_line, temp_red_line)
        return

    # Diagonal
    if board.get('3') == board.get('5') and board.get('5') == board.get('7') and board.get('7'):
        winner(board.get('3'))

        black_line_position = (-10, -60)
        red_line_position = (85, 75)

        # Transforming and rotating the lines accordingly
        temp_red_line = pygame.transform.scale(red_line, (320, 80))
        temp_red_line = pygame.transform.rotate(temp_red_line, 20 + 38 - 90)

        temp_black_line = pygame.transform.scale(black_line, (610, 100))
        temp_black_line = pygame.transform.rotate(temp_black_line, 45 - 90)

        cross_line(black_line_position, red_line_position, temp_black_line, temp_red_line)
        return

    # Its a draw
    if len(board) == 9:
        board = dict()


# Swapping between players
def swap():
    global turn
    # print(turn)
    if turn == "player1":
        turn = "player2"
    else:
        turn = "player1"


# X, O positions in the grid
def x_o_position(num, co):
    if board[num] == "player1":
        if player1_with_x:
            screen.blit(x, co)
        else:
            screen.blit(o, co)
    else:
        if player1_with_x:
            screen.blit(o, co)
        else:
            screen.blit(x, co)


def game_selection():
    global board
    length = len(board)
    while True:
        for event in pygame.event.get():
            # Quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Input press and It will not work for keypad numbers
            # if event.type == pygame.KEYDOWN:
            #     for i in range(9):
            #         if event.key == ord(str(i + 1)) and not board.get(str(i + 1)):
            #             board[str(i + 1)] = turn
            #             print("in swap")
            #             swap()

            if event.type == pygame.KEYDOWN:
                if (event.key == ord("1") or event.key == pygame.K_KP1) and not board.get("1"):
                    board["1"] = turn
                    swap()
                elif (event.key == ord("2") or event.key == pygame.K_KP2) and not board.get("2"):
                    board["2"] = turn
                    swap()
                elif (event.key == ord("3") or event.key == pygame.K_KP3) and not board.get("3"):
                    board["3"] = turn
                    swap()
                elif (event.key == ord("4") or event.key == pygame.K_KP4) and not board.get("4"):
                    board["4"] = turn
                    swap()
                elif (event.key == ord("5") or event.key == pygame.K_KP5) and not board.get("5"):
                    board["5"] = turn
                    swap()
                elif (event.key == ord("6") or event.key == pygame.K_KP6) and not board.get("6"):
                    board["6"] = turn
                    swap()
                elif (event.key == ord("7") or event.key == pygame.K_KP7) and not board.get("7"):
                    board["7"] = turn
                    swap()
                elif (event.key == ord("8") or event.key == pygame.K_KP8) and not board.get("8"):
                    board["8"] = turn
                    swap()
                elif (event.key == ord("9") or event.key == pygame.K_KP9) and not board.get("9"):
                    board["9"] = turn
                    swap()

        # Tic Tac Toe Grid
        screen.fill((100, 100, 100))
        screen.blit(tic_tac_toe_board, (90, 50))

        # Players and Score
        screen.blit(player1, (80, 420))
        screen.blit(player2, (310, 420))
        screen.blit(score, (215, 390))

        # Making the Numbers for position reference for the players if there is an empty slot
        for i in range(9):
            if not board.get(str(i + 1)):
                screen.blit(x_o[i], (90 + (i % 3) * 105, 320 - (i // 3) * 100))
            else:
                coordinates = (110 + (i % 3) * 100, 270 - (i // 3) * 100)
                x_o_position(str(i + 1), coordinates)

        # It shows the turn of the players with corresponding to their X or O
        if turn == "player1":
            if player1_with_x:
                screen.blit(x, (90, 490))
            else:
                screen.blit(o, (90, 490))
        else:
            if player1_with_x:
                screen.blit(o, (340, 490))
            else:
                screen.blit(x, (340, 490))

        pygame.display.update()

        # If any changes in board length then we check for the winner
        if len(board) != length:
            length = len(board)
            check_winner()
            print(board)


# Start Button in Home page
# On clicking the button, goes to game() function
def home_page():
    clicked = False
    while not clicked:
        # Mouse position
        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            # Quit option
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked on the button
                if 190 <= mouse[0] <= 300 and 270 <= mouse[1] <= 310:
                    clicked = True
            # Check if a button is pressed on keyboard
            if event.type == pygame.KEYDOWN:
                # If enter is pressed
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    clicked = True

        # Background color
        screen.fill((60, 25, 60))

        # if mouse is hovered on a button it changes to lighter shade
        if 190 <= mouse[0] <= 300 and 270 <= mouse[1] <= 310:
            pygame.draw.rect(screen, colors.color_light, [190, 270, 110, 50])
        else:
            pygame.draw.rect(screen, colors.color_dark, [190, 270, 110, 50])

        # Start text
        screen.blit(text, (210, 280))
        pygame.display.update()

    game_selection()


# Starting the game
home_page()
