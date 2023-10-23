import time
import cv2
from board import Board


class QueenPlaces:
    def __init__(self, size):   # присваивает значение размера мест для ферзя
        self.size = size

        self.solutions = []

    def solve(self):   # решает задачу о 8 ферзях
        rows = [""] * self.size
        self.find_queens(rows, 0)

    def find_queens(self, rows, column_index):   # ищет все возможные места размещения ферзя и проверяем их
        if column_index == self.size:
            self.solutions.append(rows.copy())
            self.show(rows)
            return True

        for column in range(self.size):
            if self.check_position(rows, column_index, column):
                rows[column_index] = column
                self.find_queens(rows, column_index + 1)

    def check_position(self, rows, column_index, column) -> bool:   # проверяет наличие пересечений ферзей по вертикали, горизонтали и диагонали; bool - Верно, нет пересечения/Ложь, есть пересечение
        for i in range(column_index):
            if rows[i] == column or rows[i] - i == column - column_index or rows[i] + i == column + column_index:
                return False
        return True

    def show(self, rows: list):   # показывает найденные результаты(список столбцов с правильно найденными позициями)
        rows2d = [["Ф" if column == rows[row] else "-" for column in range(self.size)] for row in range(self.size)] # обозначает в списке буквой 'Ф' места, где стоит ферзь, '' места, где его нет
        print(f"Решение {len(self.solutions)}:")   # печатает номер решения перед списком
        for row in rows2d:
            print(row)
        print("\n", "-" * 50, "\n")   # печатает разделение между списками/решениями

if __name__ == '__main__':
    size = 8 

    qp = QueenPlaces(size)

    start_time = time.time()

    qp.solve()

    end_time = time.time()

    print(f"Найдено {len(qp.solutions)} решения за {str(end_time - start_time)[:7]} секунды.")   # печатает время, за которое были найдены все возможные решения

    for solution_index, rows in enumerate(qp.solutions):   
        board = Board(size=size)   # задаёт размер визуализируемой доски
        
        for row_index, column_index in enumerate(rows):   # расставляет ферзей на шахматной доске
            board.put('queen', (row_index, column_index))

        board.draw()   # визуализирует ферзей с помощью OpenCV                                                                    

        board.panel = cv2.putText(board.panel, f'Solution {solution_index}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)   # показывает номер решения в левом углу изображения

        board.show()   # визуализирует шахматную доску с помощью OpenCV
