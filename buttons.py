from settings import *


class Buttons:
    def __init__(self, app, colour, x, y, width, height, text=''):
        self.app = app
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw_button(self, outline=None):
        if outline:
            pygame.draw.rect(self.app.screen, outline, (self.x - 2, self.y - 2, self.width + 5, self.height + 5), 0)
        pygame.draw.rect(self.app.screen, self.colour, (self.x, self.y, self.width, self.height), 0)


        if self.text != '':
            font = pygame.font.SysFont(FONT, 22)
            text = font.render(self.text, 1, (0, 0, 0))
            self.app.screen.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))



    def isOver(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
