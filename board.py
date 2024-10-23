 # Списки фигур игрока 
        self.pl_figures = []
        
class Board:

    def __init__(self, pl_side):
        self.pl_side = pl_side
        self.cmp_side = OPPOSITE_SIDE[pl_side]
    
     # Создаем клетки поля
        self.cells = []
        for i in range(0, 7):
            self.cells.append([None] * 7)
        for figure in (self.cmp_figures + self.pl_figures):
            self.cells[figure.row][figure.col] = figure   
             
 class Figure(pygame.sprite.Sprite):

    def __init__(self, filename, r, c, side, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.dirname(__file__) + '/' + filename).convert_alpha()
        self.rect = self.image.get_rect(topleft=(c * CELL_SIZE, r * CELL_SIZE))
        self.row = r
        self.col = c
        self.side = side
        self.board = board
        self.is_drop = False

    def set_pos(self, r, c):
        self.row = r
        self.col = c
        self.rect.left = c * CELL_SIZE
        self.rect.top = r * CELL_SIZE

    @staticmethod
    def is_valid_pos(r, c):
        if 0 <= r <= 7 and 0 <= c <= 7:
            return True
        else:
            return False       
       