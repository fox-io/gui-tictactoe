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

    is_player_turn = True

    def __init__(self):
        """Initializes the game.
        """
        pygame.init()
        self.window = pygame.display.set_mode((200, 200))
        pygame.display.set_caption('Tic Tac Toe')
        self.background = pygame.image.load('board.png')
        self.font = pygame.font.Font(None, 64)
        self.define_spaces()

    def define_spaces(self):
        """Define the clickable play areas.
        """
        for space in self.board:
            self.board[space]['rect'] = pygame.Rect(self.board[space]['coords'], (66, 66))

    def on_update(self):
        """Draws the board onto the screen, including moves that have been made.
        """
        self.window.blit(self.background, (0, 0))
        for space in self.board:
            if self.board[space]['value'] is not None:
                self.board[space]['surface'] = self.font.render(self.board[space]['value'], True, (0, 0, 0))

                self.window.blit(self.board[space]['surface'], self.board[space]['rect'].move(19, 12))

        pygame.display.flip()

    def on_click(self, pos):
        """Called when player clicks on a space.

        Checks if it is the player's turn and if the space is empty.

        :param pos: The position of the mouse click.
        """
        if not self.is_player_turn:
            print("Not your turn.")
            return
        else:
            for space in self.board:
                if self.board[space]['rect'].collidepoint(pos):
                    if self.board[space]['value'] is None:
                        self.board[space]['value'] = 'X'
                        self.is_player_turn = False
                    else:
                        print("Space already taken.")

    def make_computer_turn(self):
        """Perform logic needed for the computer player to make a turn.
        """
        pass  # TODO: Implement this.


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
