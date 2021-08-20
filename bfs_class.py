from settings import *

class BreadthFirst():
    def __init__(self, app, start_node_x, start_node_y, end_node_x, end_node_y, wall_pos):
        self.app = app
        self.start_node_x = start_node_x
        self.start_node_y = start_node_y
        self.end_node_x = end_node_x
        self.end_node_y = end_node_y
        self.wall_pos = wall_pos
        self.visited = [(self.start_node_x, self.start_node_y)]
        self.route = None
        self.route_found = False

    def draw_all_paths(self, i, j):
        
        pygame.draw.rect(self.app.screen, TAN, (i * 24 + 240, j * 24, 24, 24), 0)


        pygame.draw.rect(self.app.screen, TOMATO, (240 + self.start_node_x * 24, self.start_node_y * 24, 24, 24), 0)
        pygame.draw.rect(self.app.screen, ROYALBLUE, (240 + self.end_node_x * 24, self.end_node_y * 24, 24, 24), 0)

        for x in range(52):
            pygame.draw.line(self.app.screen, MRIGANK, (GS_X + x * 24, GS_Y), (GS_X + x * 24, GE_Y))
        for y in range(30):
            pygame.draw.line(self.app.screen, MRIGANK, (GS_X, GS_Y + y * 24), (GE_X, GS_Y + y * 24))

        pygame.display.update()

    def checkValid(self, move):
        if move not in self.wall_pos and move not in self.visited:
            self.visited.append(move)
            return True
        return False

    def findEnd(self, first_out):
        if first_out == (self.end_node_x, self.end_node_y):
            return True
        return False

    def bfs_execute(self):
        queue = [(self.start_node_x, self.start_node_y)]
        moves_queue = ['']
        first_out = ''
        first_moves = ''

        while len(queue) > 0:
            
            first_out = queue.pop(0)
            first_moves = moves_queue.pop(0)
            for m in ['L', 'R', 'U', 'D']:
                i, j = first_out
                # print('parent:', i, j)
                if m == 'L':
                    i -= 1
                elif m == 'R':
                    i += 1
                elif m == 'U':
                    j -= 1
                elif m == 'D':
                    j += 1

                
                latest_moves = first_moves + m
                if self.checkValid((i, j)):
                    self.draw_all_paths(i, j)
                    queue.append((i, j))
                    moves_queue.append(latest_moves)

                if self.findEnd((i, j)):
                    self.route = latest_moves
                    self.route_found = True
                    break

            if self.route_found:
                break

