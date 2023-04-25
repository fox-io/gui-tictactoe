import pygame


class Game:
    """The game class.
    """
    board = {
        1: {
            'value': None,
            'coords': (0, 0),
            'rect': None,
            'surface': None
        },
        2: {
            'value': None,
            'coords': (67, 0),
            'rect': None,
            'surface': None
        },
        3: {
            'value': None,
            'coords': (134, 0),
            'rect': None,
            'surface': None
        },
        4: {
            'value': None,
            'coords': (0, 67),
            'rect': None,
            'surface': None
        },
        5: {
            'value': None,
            'coords': (67, 67),
            'rect': None,
            'surface': None
        },
        6: {
            'value': None,
            'coords': (134, 67),
            'rect': None,
            'surface': None
        },
        7: {
            'value': None,
            'coords': (0, 134),
            'rect': None,
            'surface': None
        },
        8: {
            'value': None,
            'coords': (67, 134),
            'rect': None,
            'surface': None
        },
        9: {
            'value': None,
            'coords': (134, 134),
            'rect': None,
            'surface': None
        }
    }

    winning_lines = {
        1: [1, 2, 3],
        2: [4, 5, 6],
        3: [7, 8, 9],
        4: [1, 4, 7],
        5: [2, 5, 8],
        6: [3, 6, 9],
        7: [1, 5, 9],
        8: [3, 5, 7]
    }

    is_player_turn = True       # Is true when it is the player's turn.
    is_active = True            # Is false when game is over.
    game_over_screen = None     # The game over screen.
    game_over_button = None     # The game over button.

    def __init__(self):
        """Initializes the game.
        """
        pygame.init()
        self.window = pygame.display.set_mode((200, 200))
        pygame.display.set_caption('Tic Tac Toe')
        self.background = pygame.image.load('assets/board.png')
        self.font = pygame.font.Font(None, 64)

        self.define_spaces()

    def create_game_over_screen(self, winner):
        """Creates a game over screen.

        :param winner: The winner of the game.
        """
        # Create necessary surfaces.
        self.game_over_screen = {
            'background': pygame.Surface((200, 200)),
            'button_border': pygame.Surface((101, 51)),
            'button': pygame.Surface((100, 50))
        }

        # Fill the background with white.
        self.game_over_screen['background'].fill((255, 255, 255))
        self.game_over_screen['background'].set_alpha(200)

        # Fill the button border with black.
        self.game_over_screen['button_border'].fill((0, 0, 0))
        self.game_over_screen['button_border'].set_alpha(200)

        # Fill the button with white.
        self.game_over_screen['button'].fill((255, 255, 255))
        self.game_over_screen['button'].set_alpha(200)

        # Add the text for the winner and the play button.
        if not winner:
            self.game_over_screen['background'].blit(self.font.render("Tie!", True, (0, 0, 0)), (60, 20))
        else:
            self.game_over_screen['background'].blit(self.font.render(winner + " wins!", True, (0, 0, 0)), (20, 20))
        self.game_over_screen['button'].blit(self.font.render("Play", True, (0, 0, 0)), (4, 2))

        # Add the button to the button border.
        self.game_over_screen['button_border'].blit(self.game_over_screen['button'], (0, 0))

        # Add the button border to the background.
        self.game_over_screen['background'].blit(self.game_over_screen['button_border'], (50, 100))

        # Add the background to the window.
        self.window.blit(self.game_over_screen['background'], (0, 0))

        # Update the display.
        pygame.display.flip()

    def define_spaces(self):
        """Define the clickable play areas.
        """
        for space in self.board:
            self.board[space]['rect'] = pygame.Rect(self.board[space]['coords'], (66, 66))

    def on_update(self):
        """Draws the board onto the screen, including moves that have been made.
        """
        if not self.is_player_turn:
            self.make_computer_turn()
            self.is_player_turn = True

        self.window.blit(self.background, (0, 0))
        for space in self.board:
            if self.board[space]['value'] is not None:
                self.board[space]['surface'] = self.font.render(self.board[space]['value'], True, (0, 0, 0))

                self.window.blit(self.board[space]['surface'], self.board[space]['rect'].move(19, 12))

        if not self.is_active:
            self.create_game_over_screen(self.check_for_winner())

        pygame.display.flip()

    def reset_game(self):
        """Resets the game.
        """
        for space in self.board:
            self.board[space]['value'] = None

        self.is_active = True
        self.is_player_turn = True

    def on_click(self, pos):
        """Called when player clicks on a space.

        Checks if it is the player's turn and if the space is empty.

        :param pos: The position of the mouse click.
        """
        if not self.is_player_turn:
            print("Not your turn.")
        elif not self.is_active:
            if self.game_over_screen['button'].get_rect().move(50, 100).collidepoint(pos):
                self.reset_game()
            else:
                print("Game is not active.")
        else:
            for space in self.board:
                if self.board[space]['rect'].collidepoint(pos):
                    if self.board[space]['value'] is None:
                        self.board[space]['value'] = 'X'
                        self.is_player_turn = False
                        if self.check_for_winner() == 'X':
                            print("You win!")
                    else:
                        print("Space already taken.")

    def make_winning_move(self):
        """Check for a winning move for the computer player.
        """
        for line in self.winning_lines:
            if self.board[self.winning_lines[line][0]]['value'] == 'O' and self.board[self.winning_lines[line][1]]['value'] == 'O' and self.board[self.winning_lines[line][2]]['value'] is None:
                self.board[self.winning_lines[line][2]]['value'] = 'O'
                return True
            if self.board[self.winning_lines[line][0]]['value'] == 'O' and self.board[self.winning_lines[line][1]]['value'] is None and self.board[self.winning_lines[line][2]]['value'] == 'O':
                self.board[self.winning_lines[line][1]]['value'] = 'O'
                return True
            if self.board[self.winning_lines[line][0]]['value'] is None and self.board[self.winning_lines[line][1]]['value'] == 'O' and self.board[self.winning_lines[line][2]]['value'] == 'O':
                self.board[self.winning_lines[line][0]]['value'] = 'O'
                return True
        return False

    def make_blocking_move(self):
        """Check for a blocking move for the computer player.
        """
        for line in self.winning_lines:
            if self.board[self.winning_lines[line][0]]['value'] == 'X' and self.board[self.winning_lines[line][1]]['value'] == 'X' and self.board[self.winning_lines[line][2]]['value'] is None:
                self.board[self.winning_lines[line][2]]['value'] = 'O'
                return True
            elif self.board[self.winning_lines[line][0]]['value'] == 'X' and self.board[self.winning_lines[line][1]]['value'] is None and self.board[self.winning_lines[line][2]]['value'] == 'X':
                self.board[self.winning_lines[line][1]]['value'] = 'O'
                return True
            elif self.board[self.winning_lines[line][0]]['value'] is None and self.board[self.winning_lines[line][1]]['value'] == 'X' and self.board[self.winning_lines[line][2]]['value'] == 'X':
                self.board[self.winning_lines[line][0]]['value'] = 'O'
                return True

    def make_center_move(self):
        """Check if center space is available.
        """
        if self.board[5]['value'] is None:
            self.board[5]['value'] = 'O'
            return True
        return False

    def make_random_move(self):
        """Choose a random space.
        """
        for space in self.board:
            if self.board[space]['value'] is None:
                self.board[space]['value'] = 'O'
                return True
        return False

    def make_computer_turn(self):
        """Perform logic needed for the computer player to make a turn.
        """
        if not self.is_active:
            return

        if not self.make_winning_move():
            if not self.make_blocking_move():
                if not self.make_center_move():
                    if not self.make_random_move():
                        # Tie game
                        self.is_active = False

        if self.check_for_winner() == 'O':
            print("Computer wins!")

    def check_for_winner(self):
        """Check if there is a winner.
        """
        for line in self.winning_lines:
            if self.board[self.winning_lines[line][0]]['value'] == self.board[self.winning_lines[line][1]]['value'] == self.board[self.winning_lines[line][2]]['value']:
                if self.board[self.winning_lines[line][0]]['value'] == 'X':
                    self.is_active = False
                    return 'X'
                elif self.board[self.winning_lines[line][0]]['value'] == 'O':
                    self.is_active = False
                    return 'O'
        return None


# Main Loop
game = Game()

is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        # Intercept mouse clicks.
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.on_click(pygame.mouse.get_pos())

    game.on_update()
