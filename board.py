import cv2
import numpy as np
from utils import PIECES, COLOR_SCHEME

class Board():
    def __init__(self, size, mode=1, cell_length=100):   #задаёт значения резмера шахматной доски
        self.size = size
        self.cell_length = cell_length
        self.mode = mode
        self.create()

    def create(self):   #создаёт n x n шахматную доску на основе значений её размера
        get_row = lambda size, shift: [{"type": (cell_index + shift) % 2, "piece": None} for cell_index in range(size)]
        self.board = [get_row(self.size, _ % 2) for _ in range(self.size)]

        self.panel_length = self.cell_length * self.size
        self.panel = np.zeros([self.panel_length, self.panel_length, 3], dtype=np.uint8)
        self.panel.fill(255)
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                cell_start = (row_index * self.cell_length, column_index * self.cell_length)
                cell_end = ((row_index + 1) * self.cell_length, (column_index + 1) * self.cell_length)

                self.panel = cv2.rectangle(self.panel, cell_start, cell_end, COLOR_SCHEME[self.mode][column['type']], -1)

        self.panel = cv2.cvtColor(self.panel, cv2.COLOR_BGR2BGRA)

    def put(self, piece: str, cell: tuple) -> bool:   #ставит фигуру в нужную ячейку на шахматной доске; tuple это Координаты области на двухмерной шахматной доске, где нужно разместить фигуру; bool - задаём статус операции put как логический
        row, column = cell
        self.board[row][column]['piece'] = piece
        return True

    def draw(self):    #рисует и показываем доску на изображении
        for row_index, row in enumerate(self.board):
            for column_index, column in enumerate(row):
                if not column['piece']:
                    continue

                xmin = row_index * self.cell_length
                ymin = column_index * self.cell_length
                xmax = (row_index + 1) * self.cell_length
                ymax = (column_index + 1) * self.cell_length

                piece_img = self._get_piece(column['piece'])
                mask = piece_img[..., 3:] / 255.0
                self.panel[ymin:ymax, xmin:xmax] = (1.0 - mask) * self.panel[ymin:ymax, xmin:xmax] + mask * piece_img

    def show(self):
        cv2.imshow("Solution", self.panel)
        cv2.waitKey()

    def write(self, path):
        cv2.imwrite(path, self.panel)

    def _get_piece(self, piece_name):
        piece = PIECES.get(piece_name, None)
        if not piece:
            raise KeyError(f"Неверное значение фигур. Используйте: {PIECES.keys()}")

        piece_img = piece.get('img', None)

        if piece_img is None:
            piece_path = piece['path']

            piece_img = cv2.imread(piece_path, cv2.IMREAD_UNCHANGED)
            piece_img = cv2.resize(piece_img, (self.cell_length, self.cell_length))

            PIECES[piece_name]['img'] = piece_img

        return piece_img


if __name__ == '__main__':
    board = Board(size=8)
    board.draw()